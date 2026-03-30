# ============================================================
# config.py — Configuración central del proyecto RiskLab
# ============================================================

# --- Portafolio ---
TICKERS = ["ACN", "MSFT", "NVDA", "KO", "JPM"]
BENCHMARK = "SPY"
ALL_TICKERS = TICKERS + [BENCHMARK]

TICKER_INFO = {
    "ACN":  {"nombre": "Accenture",       "sector": "Consultoría Tech"},
    "MSFT": {"nombre": "Microsoft",        "sector": "Cloud / IA"},
    "NVDA": {"nombre": "NVIDIA",           "sector": "Semiconductores / IA"},
    "KO":   {"nombre": "Coca-Cola",        "sector": "Consumo Defensivo"},
    "JPM":  {"nombre": "JPMorgan Chase",   "sector": "Finanzas"},
    "SPY":  {"nombre": "S&P 500 ETF",      "sector": "Benchmark"},
}

# --- Periodo de datos ---
START_DATE = "2019-01-01"   # 5 años de historia
END_DATE   = None            # None = hoy

# --- Parámetros de riesgo ---
CONFIDENCE_LEVELS = [0.95, 0.99]   # Para VaR / CVaR
RISK_FREE_RATE    = 0.0525          # Fallback si FRED no responde (tasa Fed ~5.25%)
TRADING_DAYS      = 252

# --- FRED series ---
FRED_SERIES = {
    "rf_rate":   "DGS3MO",    # Treasury 3M (tasa libre de riesgo)
    "inflation": "CPIAUCSL",  # CPI USA
    "vix":       "VIXCLS",    # Índice de volatilidad
}

# --- Módulos del tablero ---
MODULES = [
    {"id": "inicio",      "label": "🏠 Inicio",              "icon": "🏠"},
    {"id": "tecnico",     "label": "📈 Análisis Técnico",     "icon": "📈"},
    {"id": "rendimientos","label": "📊 Rendimientos",         "icon": "📊"},
    {"id": "garch",       "label": "🌊 ARCH/GARCH",          "icon": "🌊"},
    {"id": "capm",        "label": "🎯 CAPM y Beta",          "icon": "🎯"},
    {"id": "var",         "label": "🛡️ VaR y CVaR",          "icon": "🛡️"},
    {"id": "markowitz",   "label": "⚖️ Markowitz",           "icon": "⚖️"},
    {"id": "senales",     "label": "⚡ Señales y Alertas",   "icon": "⚡"},
    {"id": "macro",       "label": "🌐 Macro & Benchmark",   "icon": "🌐"},
]
