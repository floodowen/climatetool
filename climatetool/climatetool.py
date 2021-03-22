#!/usr/bin/env python

"""
Climate visualization tool
"""
import pandas as pd
import plotly.express as px


df = pd.read_csv('https://github.com/floodowen/climatetool/raw/main/data/Test_temp_data.csv')
fig = px.line (df, x = 'Year', y = 'Temp (Farenheit)', title = 'Avg Temp USA (1895-2020)')
fig.show()

