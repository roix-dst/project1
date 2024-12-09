import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
data = pd.read_csv('data/dst-3.0_16_1_hh_database.csv', sep=';')
print(data.describe())
#print(data.head())
#print(data.shape())