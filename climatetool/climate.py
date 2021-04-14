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
        title_text = "Degrees Farenheit"
    )   
    
if selected_metrics == 'Sea Ice Extent':
    north=st.checkbox("Northern Hemisphere")
    if north:
        fig.add_trace(go.Scatter(x=df.Date_ice_N, y=df.Extent_N,
                    mode='markers', 
                    name='Sea Ice Extent'))

    south=st.checkbox("Southern Hemisphere")
    if south:
        fig.add_trace(go.Scatter(x=df.Date_ice_S, y=df.Extent_S,
                    mode='markers', 
                    name='Sea Ice Extent'))
    fig.update_xaxes(
        title_text = 'Date',
    )                    
    fig.update_yaxes(
        title_text = "10^6 sq km"
    )                
if selected_metrics == 'Carbon Dioxide Emissions':
    australia=st.checkbox("Australia")
    if australia:
        fig.add_trace(go.Scatter(x=df.Australia_year, y=df.CO2_Australia,
                    mode='markers+lines', 
                    name='Australia CO2 Emissions'))
    usa=st.checkbox("United States")
    if usa:
        fig.add_trace(go.Scatter(x=df.US_year, y=df.CO2_US,
                    mode='markers+lines', 
                    name='USA CO2 Emissions'))
    eu=st.checkbox("European Union")
    if eu:
        fig.add_trace(go.Scatter(x=df.EU_year, y=df.CO2_EU,
                        mode='markers+lines', 
                        name='European Union CO2 Emissions'))
    austria=st.checkbox("Austria")
    if austria:
        fig.add_trace(go.Scatter(x=df.Austria_year, y=df.CO2_Austria,
                        mode='markers+lines', 
                        name='Austria CO2 Emissions'))
    belarus=st.checkbox("Belarus")
    if belarus:
        fig.add_trace(go.Scatter(x=df.Belarus_year, y=df.CO2_Belarus,
                        mode='markers+lines', 
                        name='Belarus CO2 Emissions'))
    belgium=st.checkbox("Belgium")
    if belgium:
        fig.add_trace(go.Scatter(x=df.Belgium_year, y=df.CO2_Belgium,
                        mode='markers+lines', 
                        name='Belgium CO2 Emissions'))
    bulgaria=st.checkbox("Bulgaria")
    if bulgaria:
        fig.add_trace(go.Scatter(x=df.Bulgaria_year, y=df.CO2_Bulgaria,
                        mode='markers+lines', 
                        name='Bulgaria CO2 Emissions'))

    fig.update_xaxes(
        title_text = 'Year',
    )                    
    fig.update_yaxes(
        title_text = "Kilotonnes"
    )

st.plotly_chart(fig, use_container_width=False)