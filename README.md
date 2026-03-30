# 📊 RiskLab USTA — Proyecto Integrador de Teoría del Riesgo

Tablero interactivo de análisis financiero cuantitativo para el portafolio **Economía Digital y Servicios Globales**.

**Materia:** Teoría del Riesgo · **Profesor:** Javier Mauricio Sierra · **Universidad:** USTA

---

## 🗂️ Estructura del proyecto

```
risklab/
│
├── app.py                  # Punto de entrada principal (Streamlit)
├── config.py               # Configuración central (tickers, parámetros)
├── requirements.txt        # Dependencias Python
├── .env.example            # Plantilla de variables de entorno
├── .gitignore
│
├── utils/
│   └── data_loader.py      # Descarga y caché de datos (yfinance + FRED)
│
├── modules/
│   ├── inicio.py           # Módulo 0: Dashboard de inicio
│   ├── tecnico.py          # Módulo 1: Análisis técnico
│   ├── rendimientos.py     # Módulo 2: Rendimientos y estadísticos
│   ├── garch.py            # Módulo 3: Modelos ARCH/GARCH
│   ├── capm.py             # Módulo 4: CAPM y Beta
│   ├── var.py              # Módulo 5: VaR y CVaR
│   ├── markowitz.py        # Módulo 6: Optimización de portafolio
│   ├── senales.py          # Módulo 7: Señales y alertas ⭐
│   └── macro.py            # Módulo 8: Macro y benchmark ⭐
│
└── data/
    └── cache/              # Caché local de datos (ignorado en Git)
```

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/risklab-usta.git
cd risklab-usta
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### 3. Configurar API Keys
```bash
cp .env.example .env
# Edita .env y agrega tu FRED_API_KEY
```

Obtén tu key gratuita en: https://fred.stlouisfed.org/docs/api/api_key.html

### 4. Ejecutar el tablero
```bash
streamlit run app.py
```

---

## 📌 Portafolio analizado

| Ticker | Empresa | Sector |
|--------|---------|--------|
| ACN | Accenture | Consultoría Tecnológica |
| MSFT | Microsoft | Cloud / Inteligencia Artificial |
| NVDA | NVIDIA | Semiconductores / IA |
| KO | Coca-Cola | Consumo Defensivo |
| JPM | JPMorgan Chase | Finanzas Digitales |
| SPY | S&P 500 ETF | Benchmark del mercado |

**Narrativa:** *Economía Digital y Servicios Globales* — empresas que transforman industrias mediante tecnología, datos y servicios, combinadas con un activo defensivo (KO) para diversificación real.

---

## 📡 APIs utilizadas

| API | Uso | Key requerida |
|-----|-----|---------------|
| [yfinance](https://pypi.org/project/yfinance/) | Precios históricos de acciones | ❌ No |
| [FRED](https://fred.stlouisfed.org/docs/api) | Tasa libre de riesgo, inflación, VIX | ✅ Gratis |

---

## 🤖 Uso de IA

Este proyecto fue desarrollado con asistencia de Claude (Anthropic) como herramienta de apoyo en la estructuración del código y revisión de conceptos. Todo el código fue revisado, comprendido y ajustado por los integrantes del grupo. La IA fue utilizada como asistente, no como sustituto del aprendizaje.

---

## 📚 Referencias

- Moscote Flórez, O. *Elementos de estadística en riesgo financiero*. USTA, 2013.
- Markowitz, H. (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- Tsay, R. S. (2010). *Analysis of Financial Time Series*. 3rd ed., Wiley.
- Hull, J. C. (2018). *Risk Management and Financial Institutions*. 5th ed., Wiley.
