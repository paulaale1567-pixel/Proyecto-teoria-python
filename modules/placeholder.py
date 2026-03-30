# ============================================================
# modules/placeholder.py — Módulo en construcción (placeholder)
# Se reemplazará módulo por módulo en las siguientes sesiones.
# ============================================================

import streamlit as st


def render_placeholder(nombre_modulo: str, descripcion: str, items: list):
    st.markdown(f"## {nombre_modulo}")
    st.info(f"🚧 Este módulo está en construcción. Próximamente: **{descripcion}**")

    st.markdown("### Contenido que se implementará:")
    for item in items:
        st.markdown(f"- {item}")


# --- Módulo 1: Análisis Técnico ---
def render_tecnico(precios, rendimientos):
    render_placeholder(
        "📈 Módulo 1 — Análisis Técnico e Indicadores",
        "Indicadores técnicos interactivos por activo",
        [
            "RSI (Relative Strength Index)",
            "MACD y señal",
            "Bandas de Bollinger",
            "Medias móviles (SMA 20, 50, 200)",
            "Volumen de negociación",
        ]
    )


# --- Módulo 2: Rendimientos ---
def render_rendimientos(precios, rendimientos):
    render_placeholder(
        "📊 Módulo 2 — Rendimientos y Propiedades Empíricas",
        "Análisis estadístico de rendimientos logarítmicos",
        [
            "Rendimientos simples vs. logarítmicos",
            "Histograma con ajuste de distribución normal",
            "Q-Q plot y boxplot",
            "Pruebas de normalidad (Jarque-Bera, Shapiro-Wilk)",
            "Hechos estilizados: fat tails, volatility clustering",
        ]
    )


# --- Módulo 3: ARCH/GARCH ---
def render_garch(precios, rendimientos):
    render_placeholder(
        "🌊 Módulo 3 — Modelos ARCH/GARCH",
        "Modelado de volatilidad condicional",
        [
            "Test de efectos ARCH (LM test)",
            "Ajuste de ARCH(1), GARCH(1,1), EGARCH",
            "Comparación AIC/BIC en tabla",
            "Diagnóstico de residuos estandarizados",
            "Pronóstico de volatilidad rodante",
        ]
    )


# --- Módulo 4: CAPM ---
def render_capm(precios, rendimientos):
    render_placeholder(
        "🎯 Módulo 4 — CAPM y Riesgo Sistemático",
        "Beta, Alpha y línea del mercado de valores (SML)",
        [
            "Cálculo de Beta para cada activo vs. SPY",
            "Dispersión rendimiento vs. mercado con regresión",
            "Tasa libre de riesgo desde FRED (DGS3MO)",
            "Tabla: Beta, Alpha de Jensen, R²",
            "SML interactiva",
        ]
    )


# --- Módulo 5: VaR ---
def render_var(precios, rendimientos):
    render_placeholder(
        "🛡️ Módulo 5 — Valor en Riesgo (VaR) y CVaR",
        "Tres métodos de VaR + CVaR al 95% y 99%",
        [
            "VaR Paramétrico (distribución normal)",
            "VaR Histórico",
            "VaR por Simulación de Montecarlo (10,000 sim.)",
            "CVaR (Expected Shortfall)",
            "Tabla comparativa con visualización de distribución",
        ]
    )


# --- Módulo 6: Markowitz ---
def render_markowitz(precios, rendimientos):
    render_placeholder(
        "⚖️ Módulo 6 — Optimización de Portafolio (Markowitz)",
        "Frontera eficiente y portafolios óptimos",
        [
            "Heatmap de correlación interactivo",
            "Simulación de 10,000+ portafolios aleatorios",
            "Frontera eficiente (espacio riesgo-retorno)",
            "Portafolio de mínima varianza",
            "Portafolio de máximo Sharpe Ratio",
        ]
    )


# --- Módulo 7: Señales ---
def render_senales(precios, rendimientos):
    render_placeholder(
        "⚡ Módulo 7 — Señales y Alertas Automáticas ⭐",
        "Panel semáforo con señales automáticas por indicador",
        [
            "Señal RSI: sobrecompra / sobreventa",
            "Señal MACD: cruce alcista / bajista",
            "Señal Bollinger: ruptura de banda",
            "Señal VaR: alerta si pérdida > umbral",
            "Umbrales configurables por el usuario",
        ]
    )


# --- Módulo 8: Macro ---
def render_macro(precios, rendimientos):
    render_placeholder(
        "🌐 Módulo 8 — Contexto Macro y Benchmark ⭐",
        "Comparación vs. mercado y contexto macroeconómico",
        [
            "Rendimiento acumulado portafolio vs. SPY",
            "Alpha de Jensen, Tracking Error, Information Ratio",
            "Tasa libre de riesgo e inflación desde FRED",
            "Tabla de desempeño relativo completa",
        ]
    )
