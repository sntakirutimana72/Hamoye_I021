import numpy as np
import pandas as pd

dataset_url = 'http://bit.ly/HDSC-Regression-Dataset'

dataset = pd.read_csv(dataset_url, error_bad_lines=False)