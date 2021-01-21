import pandas as pd
import numpy as np
import matplotlib as plt

dataset_1 =pd.read_csv("..\Datasets\datafile.csv")
crops = dataset_1["Crop"] 
print(dataset_1["2004-05"].max())
print(crops)
