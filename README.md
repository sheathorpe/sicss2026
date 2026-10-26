# Stargate Event Study
### SICSS 2026 · University of Rochester

Research code examining stock-market responses to events associated with the development of the Stargate data center in Abilene, Texas. This project supports a research paper presented at the **2026 Summer Institute in Computational Social Science (SICSS)** at the University of Rochester.

**Authors:** Shea Thorpe, Nathan Carpenter-Holmes, and Mateo Santalucia.

[Open the main analysis notebook](stargateFinal.ipynb) · [Browse the data](data/)

## Research Overview

How do companies connected to data-center infrastructure respond to major project announcements? This study examines three groups: electrical equipment manufacturers, power suppliers, and small modular reactor (SMR) developers.

The analysis constructs sector portfolios, estimates expected returns using Fama–French three- and five-factor models, and compares those estimates with observed returns around selected events. The objective is to identify abnormal returns and compare responses across sectors and model specifications.

The final notebook includes 11 selected events dated October 15, 2024, through March 27, 2026. Event dates and descriptions are defined in its opening configuration cell.

## Portfolios

The stock selection in `stargateFinal.ipynb` is:

| Portfolio | Tickers |
| --- | --- |
| Electrical equipment and infrastructure | ETN, GEV, PH, PWR, VRT |
| Power suppliers | VST, CEG, NRG, TLN |
| Small modular reactors | SMR, OKLO, NNE |
| Market comparison | SPY |

Sector portfolios use equal weights among constituents with nonzero return observations on each date. SPY is used for the market comparison charts; it is separate from the Fama–French market factor.

## Analytical Workflow

1. **Collect prices.** Download adjusted daily closing prices through `yfinance`, beginning in October 2023.
2. **Construct portfolios.** Calculate gross and log returns, then aggregate constituent returns into the three sector portfolios.
3. **Load factors.** Download daily Fama–French three- and five-factor data from the [Kenneth R. French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html).
4. **Estimate models.** Fit ordinary least squares regressions separately for each portfolio and event, using an estimation window from 367 to 2 calendar days before the event.
5. **Evaluate event windows.** Compare observed and model-implied returns over four trading observations: one before the matched event date, the matched date, and two after it. Non-trading event dates are matched to the nearest available date.
6. **Summarize results.** Calculate cumulative abnormal returns, standard errors, t-statistics, p-values, and pairwise portfolio comparisons; generate factor-exposure and return charts.

The notebook contains the calculations and saved outputs. The accompanying research paper, referenced in the original project description, is not included in this repository.

## Repository Contents

| File or directory | Description |
| --- | --- |
| [`stargateFinal.ipynb`](stargateFinal.ipynb) | Main analysis, including expanded portfolios, event-study calculations, statistical comparisons, and visualizations. |
| [`stargate.ipynb`](stargate.ipynb) | Earlier exploratory notebook with a smaller stock selection. |
| [`data/allPrices.csv`](data/allPrices.csv) | Exported daily adjusted closing prices. |
| [`data/allReturns.csv`](data/allReturns.csv) | Gross daily return ratios, before subtracting one. |
| [`data/allLogReturns.csv`](data/allLogReturns.csv) | Logarithms of the daily return ratios. |
| [`data/eReturns.csv`](data/eReturns.csv) | Equipment-portfolio constituent returns, weights, and aggregate returns. |
| [`data/pReturns.csv`](data/pReturns.csv) | Power-portfolio constituent returns, weights, and aggregate returns. |
| [`data/sReturns.csv`](data/sReturns.csv) | SMR-portfolio constituent returns, weights, and aggregate returns. |
| [`SMR portfolio.png`](SMR%20portfolio.png) | Saved SMR portfolio figure. |

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/sheathorpe/sicss2026.git
cd sicss2026
```

### 2. Set up Python

Use a Python 3 environment with pip. The final notebook records Python 3.13.9 in its metadata.

Create a virtual environment:

```sh
python -m venv .venv
```

Activate it with `source .venv/bin/activate` on macOS/Linux, or `.\.venv\Scripts\Activate.ps1` in Windows PowerShell. Then install the dependencies:

```sh
python -m pip install jupyterlab yfinance requests numpy "pandas<3" matplotlib seaborn scipy statsmodels
```

The pandas constraint preserves compatibility with the notebook's use of `DataFrame.applymap`, which was [removed in pandas 3.0](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html#removal-of-prior-version-deprecations-changes). Modules such as `os`, `io`, `zipfile`, and `datetime` are part of Python's standard library and do not need separate installation.

### 3. Run the analysis

```sh
jupyter lab stargateFinal.ipynb
```

Select the Python environment containing the dependencies, then run the cells in order from top to bottom. Launch Jupyter from the repository root so the relative `data/` paths resolve correctly.

An internet connection is required for price and factor downloads. Running the notebook **overwrites the generated CSV files in `data/`**.

## Outputs

The main notebook produces:

- Cumulative abnormal return tables for the three- and five-factor specifications.
- Standard errors, t-statistics, p-values, and significance summaries.
- Pairwise comparisons between sector portfolios.
- Factor-coefficient plots with confidence intervals.
- SMR portfolio return charts, event-window plots, and comparisons with SPY.

## Reproducibility Notes

- **Live downloads:** The price-download end date is the execution date. Provider revisions and changes in data availability can alter results between runs.
- **Saved data:** The committed CSV files reflect the earlier stock selection and omit PWR, VRT, NRG, and TLN. Running the final notebook regenerates them using its expanded portfolios.
- **Missing observations:** The implementation replaces missing or infinite values with zero and excludes zero-return observations when assigning portfolio weights. This treatment affects portfolio composition and should be considered when interpreting results.
- **Environment:** The repository does not include a fully pinned environment or automated test suite. The installation instructions describe the notebook's dependencies, not a validated reproduction of the paper.
- **Interpretation:** Event-window estimates describe associations around selected announcements; they do not, on their own, establish causation.

## Authors

- Shea Thorpe
- Nathan Carpenter-Holmes
- Mateo Santalucia
