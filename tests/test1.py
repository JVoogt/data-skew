import data_skew as ds
import json
import pandas as pd
import numpy as np

data = pd.DataFrame({'Gender' : ['M', 'F', None] * 12,
                   'Language' : ['P', 'F'] * 12,
                   'Quantity' : np.random.randn(24),
                   'Values' : np.random.random_integers(0,4,24)})

with open('bias.json') as bias:
    bias = json.load(bias)

df = ds.getBiasedDataset(data,bias)
print(df.groupby(by="Gender").size())