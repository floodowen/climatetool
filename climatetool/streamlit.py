# streamlit run streamlit.py to run

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
    label="Choose...", options=['Global Temperature Change','Sea Ice Extent', 'Carbon Dioxide Emissions']
)

fig = go.Figure()
if selected_metrics == 'Global Temperature Change':
    fig.add_trace(go.Scatter(x=df.Year_temp, y=df.Temp,
                    mode='lines',
                    name='Global Temperature over time'))
    fig.update_xaxes(
        title_text = 'Year',
    )                    
    fig.update_yaxes(
        title_text = "Degrees Celsius" #Just guessing here... 
    )   
    
if selected_metrics == 'Sea Ice Extent':
    fig.add_trace(go.Scatter(x=df.Date_ice, y=df.Extent,
                    mode='markers', 
                    name='Sea Ice Extent'))
    fig.update_xaxes(
        title_text = 'Date',
    )                    
    fig.update_yaxes(
        title_text = "Sea Ice Extent Units" #Just guessing here... 
    )                
if selected_metrics == 'Carbon Dioxide Emissions':
    australia=st.checkbox("Australia")
    if australia:
        fig.add_trace(go.Scatter(x=df.Australia_year, y=df.GHG_Aus,
                    mode='markers+lines', 
                    name='Australia CO2 Emissions'))

    usa=st.checkbox("United States")
    if usa:
        fig.add_trace(go.Scatter(x=df.US_year, y=df.GHG_US,
                    mode='markers+lines', 
                    name='USA CO2 Emissions'))

    eu=st.checkbox("European Union")
    if eu:
        fig.add_trace(go.Scatter(x=df.EU_year, y=df.GHG_EU,
                        mode='markers+lines', 
                        name='European Union CO2 Emissions'))

    fig.update_xaxes(
        title_text = 'Year',
    )                    
    fig.update_yaxes(
        title_text = "Metric Tons" #Just guessing here... 
    )

st.plotly_chart(fig, use_container_width=False)