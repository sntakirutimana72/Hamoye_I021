import numpy as np
import pandas as pd

data_url = 'http://bit.ly/HDSC-Regression-Dataset'
df = pd.read_csv(dataset_url, error_bad_lines=False)

column_names = {'T1': 'Temperature in kitchen area',
                'RH_1': 'Humidity in kitchen area',
                'T2': 'Temperature in living room area',
                'RH_2': 'Humidity in living room area',
                'T3': 'Temperature in laundry room area',
                'RH_3': 'Humidity in laundry room area',
                'T4': 'Temperature in office room',
                'RH_4': 'Humidity in office room',
                'T5': 'Temperature in bathroom',
                'RH_5': 'Humidity in bathroom',
                'T6': 'Temperature outside the building (north side)',
                'RH_6': 'Humidity outside the building (north side)',
                'T7': 'Temperature in ironing room',
                'RH_7': 'Humidity in ironing room',
                'T8': 'Temperature in teenager room 2',
                'RH_8': 'Humidity in teenager room 2',
                'T9': 'Temperature in parents room',
                'RH_9': 'Humidity in parents room',
                'To': 'Temperature outside (from Chievres weather station)',
                'RH_out': 'Humidity outside (from Chievres weather station)',
                'rv1': 'Random variable 1',
                'rv2': 'Random variable 2'}
df = df.rename(columns=column_names)

# Normalise dataset to instructed scale
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
transformed_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
normalized_df = transformed_df.drop(columns=['date', 'lights'])
