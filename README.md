# Air Quality Prediction — Ankara

An end-to-end machine-learning project on air-quality data from three Ankara
monitoring stations, built for a university software-engineering course.

## Overview
The project takes raw pollutant measurements, cleans and enriches them, explores
the data, and trains a neural network to classify air quality — with a full
evaluation of the results.

## Data
Measurements from three station types in Ankara:
- **Urban** — Bahçelievler
- **Traffic** — Siteler
- **Industrial** — Sıhhıye

Pollutants & conditions: PM10, PM2.5, SO₂, CO, NO₂, NOₓ, NO, O₃, and relative humidity (µg/m³).

## Pipeline
| Stage | Script | What it does |
|---|---|---|
| Imputation | `scriptler/impute.py` | Fills missing measurements |
| Feature engineering | `scriptler/mevsim_ekle.py`, `scriptler/yil_ekle.py` | Adds season & year features |
| Statistics | `scriptler/istatistik.py`, `scriptler/metrics.py` | Summary stats / dataset profiling |
| Visualization | `scriptler/gorsellestirme.py` | Generates the plots in `grafikler/` |
| Modeling | `scriptler/model.ipynb` | Keras/TensorFlow network (Dense + Dropout + LSTM) |

## Model
A neural network built with **TensorFlow/Keras**, evaluated with **accuracy,
precision, recall, and F1** (via scikit-learn). Training curves and per-class
metrics are in `grafikler/asama5/`.

## Results
See `grafikler/` for:
- Pollutant trends by day and season (`asama3/`)
- Model comparison & accuracy (`asama4/`)
- Training loss/accuracy and precision/recall/F1 (`asama5/`)

## Repository layout
- `scriptler/` — processing & modeling code
- `veri_seti/` — datasets (see `notlar.txt` for station & pollutant notes)
- `grafikler/` — generated plots and evaluation charts

## Notes
Open CSVs with a text editor (semicolon separator). Script purposes are documented
as inline comments. 

_Course project, 2020._
