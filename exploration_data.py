import pandas as pd
import scipy
import matplotlib.pyplot as plt
import numpy as np

filename = "household_power_consumption/0_smart_plugs_devices.csv"

data = pd.read_csv(filename)

print(data.head(10))

shape = data.shape
print(shape)

data = pd.read_csv(filename)
types = data.dtypes
print(types)

pd.set_option('display.precision', 2)
description = data.describe()
print(description)

pd.set_option('display.precision', 3)
correlations = data.corr(method='pearson')
print(correlations)
