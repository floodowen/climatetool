# streamlit run teststreamlit.py to run

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

csv_file_all = 'Combined_data.csv'
df= pd.read_csv(csv_file_all)

st.title("Climate Variables Over Time")
st.markdown(
"""
This app is for visualizing climate variables over time 
"""
)

st.markdown("#### " +"What Trends would you like to see?")

selected_metrics = st.selectbox(
    label="Choose...", options=['Global Temperature over time','Sea Ice Extent', 'Australia CO2 Emissions', 'European Union CO2 Emissions', 'USA CO2 Emissions']
)

fig = go.Figure()
if selected_metrics == 'Global Temperature over time':
    fig.add_trace(go.Scatter(x=df.Year_temp, y=df.Temp,
                    mode='lines',
                    name='Global Temperature over time'))
if selected_metrics == 'Sea Ice Extent':
    fig.add_trace(go.Scatter(x=df.Date_ice, y=df.Extent,
                    mode='markers', 
                    name='Sea Ice Extent'))
if selected_metrics == 'Australia CO2 Emissions':
    fig.add_trace(go.Scatter(x=df.Australia_year, y=df.GHG_Aus,
                    mode='markers', 
                    name='Australia CO2 Emissions'))
if selected_metrics == 'European Union CO2 Emissions':
    fig.add_trace(go.Scatter(x=df.EU_year, y=df.GHG_EU,
                    mode='markers', 
                    name='European Union CO2 Emissions'))
if selected_metrics == 'USA CO2 Emissions':
    fig.add_trace(go.Scatter(x=df.US_year, y=df.GHG_US,
                    mode='markers', 
                    name='USA CO2 Emissions'))

st.plotly_chart(fig, use_container_width=True)