import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

plt.figure(figsize=(12, 5))
plt.xticks(rotation=90)

# Fetching dataset
data_url = 'https://bit.ly/HDSC-StageOneDataset'
fuel_data = pd.read_csv(data_url, error_bad_lines=False)

# QUESTION 1
A = [1, 2, 3, 4, 5, 6]
B = [13, 21, 34]
A.extend(B)


# QUESTION 2
identity_array_1 = np.identity(3)
identity_array_2 = np.eye(3)


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
print(skewness, kurtosisness)


# QUESTION 6
fuel_data.isnull().sum()  # To describe total
fuel_data.isnull().sum() * 100 / len(fuel_data)  # To describe percentage


# QUESTION 9
(fuel_data.groupby(['fuel_type_code_pudl', 'report_year'])['fuel_cost_per_unit_burned']).sum()
percentage_var = (11902.597 * 100 / 14984.572) - 100
print(percentage_var)


# QUESTION 10
sns.barplot(data=fuel_data, x='report_year', y='fuel_cost_per_unit_delivered')
