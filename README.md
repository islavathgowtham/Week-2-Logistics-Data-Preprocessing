# Week 2: Logistics Data Collection, Cleaning, and Preprocessing

A reproducible educational project demonstrating Python preprocessing of simulated e-commerce logistics orders.

## Objectives
- Validate data types and detect invalid values
- Remove duplicate order IDs
- Standardize city names
- Flag and impute missing numeric data
- Detect delivery-time outliers using IQR
- Normalize modelling features using Min-Max scaling
- Connect data quality to logistics decision-making

## Dataset
The 12-row **synthetic** CSV contains order ID, city, distance (km), delivery duration (hours), shipping cost (INR), and item count. It intentionally includes one duplicate order, two missing values, inconsistent city formatting, and a 120-hour delivery-time anomaly. It is not a real company's data.

## Run
```bash
pip install -r requirements.txt
python src/preprocess_logistics.py
```

The script writes `data/logistics_cleaned.csv` and `data/logistics_preprocessed_for_model.csv`.

## Example results
| Metric | Raw | Cleaned |
|---|---:|---:|
| Records | 12 | 11 |
| Duplicate order IDs | 1 | 0 |
| Missing delivery durations | 1 | 0 after median imputation |
| Missing shipping costs | 1 | 0 after median imputation |

The original 120-hour delay remains in the cleaned file and is flagged for review; a separate capped field is created only in the modelling copy.

## Stakeholder use
Operations can review delivery-delay exceptions, finance can investigate abnormal shipping costs, and analysts can report missingness and transformation logs. Use verified data for official KPIs; imputed values should not be presented as observed facts.

## Contents
- `report/`: detailed Word report
- `data/`: synthetic raw and generated cleaned datasets
- `src/`: preprocessing pipeline
- `requirements.txt`: Python dependencies

## Limitations
This small simulated dataset illustrates methodology, not real operational findings. Min-Max scaling is fitted on the full sample for demonstration; production predictive models should fit scalers only on training data.
