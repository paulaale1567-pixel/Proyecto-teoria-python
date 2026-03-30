# ============================================================
# utils/data_loader.py — Descarga y caché de datos
# ============================================================

import os
import pickle
import hashlib
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import numpy as np
import yfinance as yf
import streamlit as st

from config import ALL_TICKERS, START_DATE, END_DATE, FRED_SERIES, RISK_FREE_RATE, TRADING_DAYS

# Directorio de caché local
CACHE_DIR = Path("data/cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)
CACHE_HOURS = 4  # Horas antes de refrescar datos


# ------------------------------------------------------------------
# Helpers de caché en disco
# ------------------------------------------------------------------

def _cache_path(key: str) -> Path:
    h = hashlib.md5(key.encode()).hexdigest()[:10]
    return CACHE_DIR / f"{h}.pkl"


def _load_cache(key: str):
    p = _cache_path(key)
    if p.exists():
        with open(p, "rb") as f:
            obj = pickle.load(f)
        if datetime.now() - obj["ts"] < timedelta(hours=CACHE_HOURS):
            return obj["data"]
    return None


def _save_cache(key: str, data):
    p = _cache_path(key)
    with open(p, "wb") as f:
        pickle.dump({"ts": datetime.now(), "data": data}, f)


# ------------------------------------------------------------------
# Descarga de precios con yfinance
# ------------------------------------------------------------------

@st.cache_data(ttl=CACHE_HOURS * 3600, show_spinner=False)
def cargar_precios(tickers=None, start=START_DATE, end=END_DATE) -> pd.DataFrame:
    """
    Descarga precios de cierre ajustados para todos los tickers.
    Retorna un DataFrame con columnas = tickers, índice = fecha.
    """
    if tickers is None:
        tickers = ALL_TICKERS

    cache_key = f"precios_{'_'.join(sorted(tickers))}_{start}_{end}"
    cached = _load_cache(cache_key)
    if cached is not None:
        return cached

    try:
        raw = yf.download(
            tickers,
            start=start,
            end=end,
            auto_adjust=True,
            progress=False,
            threads=True,
        )
        # yfinance devuelve MultiIndex cuando hay varios tickers
        if isinstance(raw.columns, pd.MultiIndex):
            precios = raw["Close"].copy()
        else:
            precios = raw[["Close"]].copy()
            precios.columns = tickers

        precios.dropna(how="all", inplace=True)
        _save_cache(cache_key, precios)
        return precios

    except Exception as e:
        st.error(f"❌ Error descargando precios con yfinance: {e}")
        return pd.DataFrame()


# ------------------------------------------------------------------
# Cálculo de rendimientos logarítmicos
# ------------------------------------------------------------------

def calcular_rendimientos(precios: pd.DataFrame) -> pd.DataFrame:
    """Retorna log-rendimientos diarios."""
    return np.log(precios / precios.shift(1)).dropna()


# ------------------------------------------------------------------
# Tasa libre de riesgo desde FRED
# ------------------------------------------------------------------

@st.cache_data(ttl=CACHE_HOURS * 3600, show_spinner=False)
def obtener_tasa_libre_riesgo() -> float:
    """
    Obtiene la tasa libre de riesgo anualizada desde FRED (DGS3MO).
    Si falla, usa el valor de fallback en config.py.
    """
    fred_key = os.getenv("FRED_API_KEY", "")
    if not fred_key or fred_key == "tu_key_aqui":
        return RISK_FREE_RATE

    try:
        from fredapi import Fred
        fred = Fred(api_key=fred_key)
        serie = fred.get_series(FRED_SERIES["rf_rate"]).dropna()
        tasa_anual = float(serie.iloc[-1]) / 100
        return tasa_anual
    except Exception as e:
        st.warning(f"⚠️ FRED no disponible ({e}). Usando tasa de referencia: {RISK_FREE_RATE:.2%}")
        return RISK_FREE_RATE


@st.cache_data(ttl=CACHE_HOURS * 3600, show_spinner=False)
def obtener_datos_macro() -> dict:
    """
    Descarga datos macroeconómicos desde FRED.
    Retorna un dict con DataFrames por serie.
    """
    fred_key = os.getenv("FRED_API_KEY", "")
    resultado = {}

    if not fred_key or fred_key == "tu_key_aqui":
        st.info("ℹ️ Configura FRED_API_KEY en .env para datos macro en tiempo real.")
        return resultado

    try:
        from fredapi import Fred
        fred = Fred(api_key=fred_key)
        for nombre, serie_id in FRED_SERIES.items():
            try:
                resultado[nombre] = fred.get_series(serie_id, observation_start=START_DATE)
            except Exception:
                pass
    except Exception as e:
        st.warning(f"⚠️ Error conectando a FRED: {e}")

    return resultado


# ------------------------------------------------------------------
# Resumen de datos para la página de inicio
# ------------------------------------------------------------------

def resumen_portafolio(precios: pd.DataFrame, rendimientos: pd.DataFrame) -> dict:
    """Genera estadísticas rápidas para el dashboard de inicio."""
    if precios.empty:
        return {}

    ultimos = precios.iloc[-1]
    cambio_1d = precios.pct_change().iloc[-1] * 100
    cambio_1y = precios.pct_change(252).iloc[-1] * 100
    vol_anual = rendimientos.std() * np.sqrt(252) * 100

    return {
        "precio_actual": ultimos,
        "cambio_1d":     cambio_1d,
        "cambio_1y":     cambio_1y,
        "vol_anual":     vol_anual,
        "fecha_inicio":  precios.index[0].strftime("%d %b %Y"),
        "fecha_fin":     precios.index[-1].strftime("%d %b %Y"),
        "n_dias":        len(precios),
    }
