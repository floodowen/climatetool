#!/usr/bin/env python

"""
Climate visualization tool
"""
import pandas as pd
import plotly.express as px

class Climate_plot:
	def __init__(self):
		# maybe it is possible to generailze the codes a little bit? 
		pass 
	def temp_plot(self):
		df = pd.read_csv('https://github.com/floodowen/climatetool/raw/main/data/Test_temp_data.csv')
		fig = px.line (df, x = 'Year', y = 'Temp (Farenheit)', title = 'Avg Temp USA (1895-2020)')
		return fig.show()

