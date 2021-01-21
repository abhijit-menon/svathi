import pandas as pd
import numpy as np
import matplotlib as plt

dataset_1 =pd.read_csv("..\Datasets\datafile.csv")
print(dataset_1["2004-05"].max())
