# Ankara Air Quality — ML

A machine-learning project on long-term air-quality data from Ankara, built for a
university software-engineering course (YMH418).

## Motivation
The study started from a question: **how do human activity patterns affect air
pollution?** — e.g. working days vs. holidays, day vs. night, and the reduced
movement during the pandemic period. To explore this, time-based features were
engineered on top of the raw pollutant data. The modeling effort then narrowed to
a concrete, measurable task: **predicting the monitoring-station type** (urban /
traffic / industrial) from a given set of readings.

## Data
Air-quality measurements from Ankara stations, **2008–2020** (~21,500 records,
12-hour intervals), across three station types:
- **Urban** (Kentsel) — Bahçelievler
- **Traffic** (Trafik) — Siteler
- **Industrial** (Sanayi) — Sıhhıye

Measured variables: PM10, PM2.5, SO₂, CO, NO₂, NOₓ, NO, air temperature, and
relative humidity.

Engineered features: time of day (day/night), weekday/weekend, month, and season —
chosen to capture human-activity patterns.

## Pipeline
| Stage | Script | What it does |
|---|---|---|
| Cleaning | `scriptler/impute.py` | Drops empty rows, handles outliers, **K-NN imputation** of missing values |
| Feature engineering | `scriptler/mevsim_ekle.py`, `scriptler/yil_ekle.py` | Adds season / year features |
| Statistics | `scriptler/istatistik.py`, `scriptler/metrics.py` | Dataset profiling (min/max/mean/std) |
| Visualization | `scriptler/gorsellestirme.py` | Pollutant trends by year & station type (`grafikler/`) |
| Modeling | `scriptler/model.ipynb` | Trains & evaluates the classifier |

## Model
A **Keras / TensorFlow** network (LSTM + dense layers, dropout, batch norm),
trained with an 60/20/20 train/validation/test split and evaluated with accuracy,
precision, recall, and F1 (scikit-learn).

**Results:** ~75% validation accuracy, **~85% test accuracy**. Training curves and
per-metric charts are in `grafikler/asama5/`.

## Repository layout
- `scriptler/` — processing & modeling code
- `veri_seti/` — datasets (see `notlar.txt` for station & pollutant notes)
- `grafikler/` — generated plots and evaluation charts

## Notes
Open the CSVs with a text editor (semicolon separator). Script purposes are
documented as inline comments. _University course project, 2021._
