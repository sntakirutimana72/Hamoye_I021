import io
import requests
import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

plt.figure(figsize=(12, 5))
plt.xticks(rotation=90)

# FUEL DATA RETRIEVAL
res = requests.get('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv')
data_stream = io.BytesIO(res.content)
fuel_data = pd.read_csv(data_stream)

# QUESTION 1
#* Give data A and B
A = []
B = []
AB_union = A.extend(B)
#* testing
assert AB_union == (A + B)


# QUESTION 2
indentity_array = np.indentity(3)


# QUESTION 3
fuel_cost_visual = sns.barplot(data=fuel_data, x='fuel_type_code_pudl', y='fuel_cost_per_unit_burned')
fuel_cost_visual.set_yscale("log")
fuel_cost_visual.set_ylim(1, 12000)
plt.xlabel('Fuel Unit')


# QUESTION 4
fuel_data[['fuel_mmbtu_per_unit']].describe()


# QUESTION 5
fuel_burned = fuel_data[['fuel_qty_burned']]
skewness = skew(fuel_burned)
kurtosisness = kurtosis(fuel_burned)


# QUESTION 6
fuel_data.isnull().sum()
fuel_data.isnull().sum() * 100 / len(fuel_data)


# QUESTION 7


# QUESTION 8


# QUESTION 9
sns.barplot(data=fuel_data, x='report_year', y='fuel_cost_per_unit_burned')


# QUESTION 10
sns.barplot(data=fuel_data, x='report_year', y='fuel_cost_per_unit_delivered')
