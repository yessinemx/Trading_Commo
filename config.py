"""
config.py — Chemins centralisés du projet Trading Commodities
"""
import os

# ―― Racine du projet (dossier contenant ce fichier) ――――――――――――――――――――――――――
ROOT = os.path.dirname(os.path.abspath(__file__))

# ―― Dossiers ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
DATA_PATH         = os.path.join(ROOT, 'data')
OUTPUT_PATH       = os.path.join(ROOT, 'output')        
PRESENTATION_PATH = os.path.join(ROOT, 'presentation')  
NOTEBOOK_PATH     = os.path.join(ROOT, 'notebook')
DOCS_PATH         = os.path.join(ROOT, 'docs')

# ―― Fichiers de données ――――――――――――――――――――――――――――――――――――――――――――――――――――――
EXCEL_DATA = os.path.join(DATA_PATH, 'GSCI_Data.xlsx')

# ―― Fichiers de sortie — figures ―――――――――――――――――――――――――――――――――――――――――――
FIG_Q1   = os.path.join(OUTPUT_PATH, 'Q1_indices.png')
FIG_Q5   = os.path.join(OUTPUT_PATH, 'Q5_moving_averages.png')
FIG_Q6   = os.path.join(OUTPUT_PATH, 'Q6_strategies.png')
FIG_Q7   = os.path.join(OUTPUT_PATH, 'Q7_portfolio.png')
FIG_Q8   = os.path.join(OUTPUT_PATH, 'Q8_enhanced_strategy.png')

# ―― Fichiers de présentation ―――――――――――――――――――――――――――――――――――――――――――――――
EXCEL_RESULTS     = os.path.join(PRESENTATION_PATH, 'Projet_GSCI_2026.xlsx')
LATEX_SLIDES      = os.path.join(PRESENTATION_PATH, 'Slides_GSCI_2026.tex')
LATEX_RAPPORT     = os.path.join(PRESENTATION_PATH, 'Rapport_GSCI_2026.tex')

# ―― Dates Bloomberg ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
START_DATE = '19691231'
END_DATE   = '20251231'

# ―― Tickers Bloomberg ―――――――――――――――――――――――――――――――――――――――――――――――――――――
TICKERS = {
    'SPGSCI Index':   'GSCI_Spot',
    'SPGSCIP Index':  'GSCI_ER',
    'SPGSCITR Index': 'GSCI_TR',
}

# ―― Création automatique des dossiers ――――――――――――――――――――――――――――――――――――――
for _path in [DATA_PATH, OUTPUT_PATH, PRESENTATION_PATH, NOTEBOOK_PATH, DOCS_PATH]:
    os.makedirs(_path, exist_ok=True)
