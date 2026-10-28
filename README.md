# Stroke Data Analysis

This project explores a healthcare dataset of 5,110 patient records to investigate how patient characteristics and health factors relate to stroke occurrence. The dataset includes age, gender, hypertension, heart disease, marital status, work and residence type, average glucose level, BMI, smoking status, and a binary stroke outcome.

The goal is to use these features to study stroke risk and, as the analysis develops, explore whether they can help identify records associated with higher stroke risk. This is an exploratory data-analysis project, not a clinical diagnostic tool.

## Dataset

The data is provided in [`healthcare-dataset-stroke-data.csv`](./healthcare-dataset-stroke-data.csv). It contains 5,110 rows and 12 columns. BMI is missing for 201 records (marked `N/A`), which should is handled during analysis. The `id` column is a record identifier rather than a patient characteristic too.
