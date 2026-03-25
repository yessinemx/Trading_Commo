# Projet Commodities 2026  Stratégies sur l'indice S&P GSCI ER

> Université Paris Dauphine  Master Finance  
> Auteurs : **Yassine Mannai**, **Issam Fradi**, **Antonin Bezard**  
> Période analysée : 31/12/1969  31/12/2025

---

## Structure du dépôt

```
Trading_Commo/
 Projet_GSCI_2026.ipynb    Notebook principal (Q1 à Q8)
 docs/
    Projet_2026.pdf       Énoncé du projet
    Commodity_2026.pdf    Cours R. Feraud (référence)
 data/                     Données Bloomberg (gitignorées)
    GSCI_Data.xlsx        Généré automatiquement au 1er run Bloomberg
 output/                   Graphiques & rapport (gitignorés)
     Q1_indices.png
     Q5_moving_averages.png
     Q6_strategies.png
     Q7_portfolio.png
     Q8_enhanced_strategy.png
     Rapport_GSCI_2026.docx
```

---

## Contenu du notebook

| Question | Description |
|---|---|
| **Q1** | Récupération des données Bloomberg / Excel + graphique (axe secondaire) |
| **Q2** | Métriques de performance : CAGR, volatilité, ratio Rdt/Vol |
| **Q3** | Explication des écarts Spot / ER / TR (roll yield, collatéral) |
| **Q4** | Fonction générique de calcul de moyenne mobile |
| **Q5** | Calcul des 5 MAs (25, 50, 100, 150, 200 jours) sur le GSCI ER |
| **Q6** | Backtest des 5 stratégies MA + tableau de performance |
| **Q7** | Portefeuille équi-pondéré des 5 stratégies |
| **Q8** | Stratégie améliorée : Golden Cross (MA50/200) + filtre RSI |
| **Export** | Génération automatique du rapport Word `Rapport_GSCI_2026.docx` |

---

## Prérequis

```bash
pip install pandas numpy matplotlib openpyxl python-docx blpapi
```

> **Bloomberg Terminal** requis pour le premier chargement des données.  
> Une fois `data/GSCI_Data.xlsx` généré, Bloomberg n'est plus nécessaire.

---

## Tickers Bloomberg

| Indice | Ticker |
|---|---|
| S&P GSCI Spot | `SPGSCI Index` |
| S&P GSCI ER (Excess Return) | `SPGSCIP Index` |
| S&P GSCI TR (Total Return) | `SPGSCITR Index` |
