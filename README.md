# Week 2: Data Collection, Cleaning, and Preprocessing for Logistics Analysis

## Project Overview

This project focuses on implementing a structured data preprocessing pipeline for logistics analysis using Python. It demonstrates how raw logistics data can be transformed into a clean, consistent, and analysis-ready dataset.

The project uses a simulated e-commerce logistics dataset to identify and resolve common data quality issues, including missing values, duplicate records, inconsistent formatting, and outliers.

## Objectives

- Simulate logistics data collection and explore dataset characteristics.
- Identify and handle missing and invalid data.
- Detect duplicate records and potential outliers.
- Standardize categorical variables and normalize numerical features.
- Implement data preprocessing techniques using Python.
- Explain how improved data quality supports logistics operations and decision-making.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- CSV

## Methodology

**1. Data Collection:** Prepare a simulated logistics dataset containing order IDs, delivery locations, distances, delivery durations, shipping costs, and item quantities.

**2. Data Exploration:** Examine data types, missing values, duplicate records, and descriptive statistics.

**3. Data Cleaning:** Remove duplicate records, standardize city names, validate numerical values, and handle missing data using median imputation.

**4. Outlier Detection:** Apply the Interquartile Range (IQR) method to identify unusual delivery durations while preserving original observations for investigation.

**5. Data Normalization:** Apply Min-Max scaling to selected numerical features to prepare them for further analytical modelling.

**6. Data Validation:** Verify dataset consistency, uniqueness, completeness, and numerical validity.

## Illustrative Results

The simulated dataset demonstrates the following preprocessing improvements:

| Data Quality Metric | Before | After |
|---|---|---|
| Total records | 12 | 11 |
| Duplicate order records | 1 | 0 |
| Missing delivery durations | 1 | 0 after imputation |
| Missing shipping costs | 1 | 0 after imputation |
| City name formatting | Inconsistent | Standardized |
| Extreme delivery durations | Present | Flagged for investigation |

These figures describe a simulated educational example, not actual logistics company performance.

## Business Applications

Cleaned logistics data can support:

- Delivery time and route performance analysis.
- Transportation cost optimization.
- Identification of unusual delivery delays.
- Operational reporting and KPI monitoring.
- More reliable forecasting and data-driven decisions.

## Stakeholder Communication

Preprocessing results can be communicated through weekly operational dashboards, monthly cost reports, data-quality summaries, and management reviews.

The insights can help logistics managers identify inefficient routes, finance teams investigate abnormal costs, and management prioritize operational improvements.

## Conclusion

This project demonstrates the importance of data quality in logistics analytics. By applying systematic cleaning, validation, outlier detection, and normalization techniques, raw data can be prepared for meaningful analysis and future predictive modelling.

**Note:** The dataset is simulated for educational purposes. The preprocessing techniques can be adapted to real logistics datasets.
