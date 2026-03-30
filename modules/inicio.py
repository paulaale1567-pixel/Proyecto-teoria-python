# ============================================================
# modules/inicio.py — Página de inicio del tablero
# ============================================================

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

from config import TICKERS, BENCHMARK, TICKER_INFO, START_DATE


def render(precios: pd.DataFrame, rendimientos: pd.DataFrame):
    st.markdown("## 🏠 Bienvenido a nuestro proyecto")
    st.markdown(
        """
        **Proyecto Integrador — Teoría del Riesgo**  
        Tablero de análisis financiero cuantitativo para el portafolio *Economía Digital y Servicios Globales*.
        """
    )

    if precios.empty:
        st.error("No se pudieron cargar los datos. Verifica tu conexión a internet.")
        return

    # --- KPI cards por activo ---
    st.markdown("### 📌 Estado actual del portafolio")
    cambio_1d  = precios[TICKERS].pct_change().iloc[-1] * 100
    cambio_1y  = precios[TICKERS].pct_change(252).iloc[-1] * 100
    vol_anual  = rendimientos[TICKERS].std() * np.sqrt(252) * 100
    precio_act = precios[TICKERS].iloc[-1]

    cols = st.columns(len(TICKERS))
    for i, ticker in enumerate(TICKERS):
        info = TICKER_INFO[ticker]
        delta_color = "normal"
        with cols[i]:
            st.metric(
                label=f"**{ticker}** — {info['sector']}",
                value=f"${precio_act[ticker]:,.2f}",
                delta=f"{cambio_1d[ticker]:+.2f}% hoy",
            )
            st.caption(f"Vol. anual: {vol_anual[ticker]:.1f}%")

    # --- Gráfico de precios normalizados ---
    st.markdown("### 📈 Evolución de precios (base 100)")
    base = precios[TICKERS + [BENCHMARK]].div(precios[TICKERS + [BENCHMARK]].iloc[0]) * 100

    fig = go.Figure()
    colores = ["#6C63FF", "#00C2CB", "#FF6B6B", "#FFD93D", "#4ECDC4", "#A8A8A8"]
    for j, col in enumerate(base.columns):
        es_bench = col == BENCHMARK
        fig.add_trace(go.Scatter(
            x=base.index, y=base[col],
            name=col,
            line=dict(
                color=colores[j % len(colores)],
                width=1.5 if es_bench else 2,
                dash="dot" if es_bench else "solid",
            ),
            opacity=0.7 if es_bench else 1,
        ))

    fig.update_layout(
        template="plotly_white",
        height=420,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis_title="Fecha",
        yaxis_title="Valor (base 100)",
        hovermode="x unified",
        margin=dict(l=20, r=20, t=30, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Retornos acumulados ---
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Retorno acumulado (1 año)")
        ret_1y = cambio_1y.sort_values(ascending=True)
        colores_bar = ["#FF6B6B" if v < 0 else "#4ECDC4" for v in ret_1y]
        fig2 = go.Figure(go.Bar(
            x=ret_1y.values,
            y=ret_1y.index,
            orientation="h",
            marker_color=colores_bar,
            text=[f"{v:+.1f}%" for v in ret_1y.values],
            textposition="outside",
        ))
        fig2.update_layout(
            template="plotly_white", height=300,
            xaxis_title="Retorno (%)", yaxis_title="",
            margin=dict(l=20, r=40, t=10, b=20),
        )
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        st.markdown("### 🌡️ Mapa de correlación")
        corr = rendimientos[TICKERS].corr()
        fig3 = px.imshow(
            corr,
            color_continuous_scale="RdBu_r",
            zmin=-1, zmax=1,
            text_auto=".2f",
            aspect="auto",
        )
        fig3.update_layout(
            template="plotly_white", height=300,
            margin=dict(l=20, r=20, t=10, b=20),
            coloraxis_showscale=False,
        )
        st.plotly_chart(fig3, use_container_width=True)

    # --- Tabla resumen ---
    st.markdown("### 📋 Resumen estadístico")
    resumen = pd.DataFrame({
        "Precio actual": precio_act.map("${:,.2f}".format),
        "Cambio 1D":     cambio_1d.map("{:+.2f}%".format),
        "Retorno 1A":    cambio_1y.map("{:+.1f}%".format),
        "Vol. anual":    vol_anual.map("{:.1f}%".format),
        "Sector":        [TICKER_INFO[t]["sector"] for t in TICKERS],
    })
    resumen.index.name = "Ticker"
    st.dataframe(resumen, use_container_width=True)

    st.caption(
        f"📅 Datos desde {precios.index[0].strftime('%d %b %Y')} "
        f"hasta {precios.index[-1].strftime('%d %b %Y')} "
        f"({len(precios):,} días de trading) · Fuente: Yahoo Finance"
    )
