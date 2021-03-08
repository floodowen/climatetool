#!/usr/bin/env python

"""
Climate visualization tool
"""
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('https://github.com/floodowen/climatetool/blob/main/seaice.csv')

fig = go.Figure(go.Scatter(x = df['Year'], y = df['Extent'],
                  name='Sea Ice over time'))

fig.update_layout(title='Sea Ice over Time',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.show()