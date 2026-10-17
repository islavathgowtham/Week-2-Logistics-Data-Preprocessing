from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

ROOT = Path(__file__).resolve().parents[1]
raw = pd.read_csv(ROOT / 'data' / 'logistics_raw.csv')
df = raw.copy()
df.columns = df.columns.str.strip().str.lower()
df['order_id'] = df['order_id'].astype('string').str.strip()
df['city'] = df['city'].astype('string').str.strip().str.title()
cols = ['distance_km', 'delivery_hours', 'shipping_cost_inr', 'items']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df = df.drop_duplicates(subset=['order_id'], keep='first').copy()
for col in ['distance_km', 'delivery_hours', 'shipping_cost_inr']:
    df.loc[df[col] < 0, col] = np.nan
df.loc[df['items'] < 1, 'items'] = np.nan
for col in ['delivery_hours', 'shipping_cost_inr']:
    df[col + '_was_missing'] = df[col].isna().astype(int)
for col in cols:
    if df[col].isna().any():
        df[col] = df[col].fillna(df[col].median())
q1, q3 = df['delivery_hours'].quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = max(0, q1 - 1.5 * iqr), q3 + 1.5 * iqr
df['delivery_hours_outlier'] = ((df['delivery_hours'] < lower) | (df['delivery_hours'] > upper)).astype(int)
model_df = df.copy()
model_df['delivery_hours_capped'] = model_df['delivery_hours'].clip(lower=lower, upper=upper)
scale_cols = ['distance_km', 'shipping_cost_inr', 'items']
model_df[[c + '_scaled' for c in scale_cols]] = MinMaxScaler().fit_transform(model_df[scale_cols])
df.to_csv(ROOT / 'data' / 'logistics_cleaned.csv', index=False)
model_df.to_csv(ROOT / 'data' / 'logistics_preprocessed_for_model.csv', index=False)
print(f'Raw rows: {len(raw)} | Unique cleaned orders: {len(df)}')
print('Outlier flags:', int(df['delivery_hours_outlier'].sum()))
print('Saved outputs in data/')
