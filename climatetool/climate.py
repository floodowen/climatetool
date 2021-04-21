# streamlit run climate.py to run

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

CSV_FILE_ALL = 'Combined_data.csv'
df= pd.read_csv(CSV_FILE_ALL)


st.title("Climate Variables Over Time")
st.markdown(
"""
This app is for visualizing and comparing climate variables
"""
)

st.markdown("#### " +"What Trends would you like to see?")

selected_metrics = st.selectbox(
    label="Choose...", options=['Global Temperature Change','Sea Ice Extent',\
     'Carbon Dioxide Emissions']
)

fig = go.Figure()
if selected_metrics == 'Global Temperature Change':
    fig.add_trace(go.Scatter(x=df.Year_temp, y=df.Temp,
                    mode='lines',
                    name='Global Temperature over time'))
    fig.add_trace(go.Scatter(x=df.Year_temp, y=df.trend,
                    mode='lines',
                    name='trendline'))
    fig.update_xaxes(
        title_text = 'Year',
    )
    fig.update_yaxes(
        title_text = "Degrees Farenheit"
    )
if selected_metrics == 'Sea Ice Extent':
    north=st.checkbox("Northern Hemisphere Daily 1978-2019")
    if north:
        fig.add_trace(go.Scatter(x=df.Date_ice_N, y=df.Extent_N,
                    mode='markers',
                    name='Sea Ice Extent North'))

    south=st.checkbox("Southern Hemisphere Daily 1978-2019")
    if south:
        fig.add_trace(go.Scatter(x=df.Date_ice_S, y=df.Extent_S,
                    mode='markers',
                    name='Sea Ice Extent South'))
    low=st.checkbox("Northern Hemisphere Yearly Low 1979-2018")
    if low:
        fig.add_trace(go.Scatter(x=df.Date_ice_N_low, y=df.Extent_N_low,
                    mode='lines',
                    name='Sea Ice Extent low'))
    fig.update_xaxes(
        title_text = 'Date',
    )
    fig.update_yaxes(
        title_text = "10^6 sq km"
    )
if selected_metrics == 'Carbon Dioxide Emissions':
    usa=st.sidebar.checkbox("United States")
    if usa:
        fig.add_trace(go.Scatter(x=df.US_year, y=df.CO2_US,
                    mode='markers+lines',
                    name='USA CO2 Emissions'))
    eu=st.sidebar.checkbox("European Union")
    if eu:
        fig.add_trace(go.Scatter(x=df.EU_year, y=df.CO2_EU,
                    mode='markers+lines',
                    name='European Union CO2 Emissions'))
    australia=st.sidebar.checkbox("Australia")
    if australia:
        fig.add_trace(go.Scatter(x=df.Australia_year, y=df.CO2_Australia,
                    mode='markers+lines',
                    name='Australia CO2 Emissions'))
    austria=st.sidebar.checkbox("Austria")
    if austria:
        fig.add_trace(go.Scatter(x=df.Austria_year, y=df.CO2_Austria,
                    mode='markers+lines',
                    name='Austria CO2 Emissions'))
    belarus=st.sidebar.checkbox("Belarus")
    if belarus:
        fig.add_trace(go.Scatter(x=df.Belarus_year, y=df.CO2_Belarus,
                    mode='markers+lines',
                    name='Belarus CO2 Emissions'))
    belgium=st.sidebar.checkbox("Belgium")
    if belgium:
        fig.add_trace(go.Scatter(x=df.Belgium_year, y=df.CO2_Belgium,
                    mode='markers+lines',
                    name='Belgium CO2 Emissions'))
    bulgaria=st.sidebar.checkbox("Bulgaria")
    if bulgaria:
        fig.add_trace(go.Scatter(x=df.Bulgaria_year, y=df.CO2_Bulgaria,
                    mode='markers+lines',
                    name='Bulgaria CO2 Emissions'))
    canada=st.sidebar.checkbox("Canada")
    if canada:
        fig.add_trace(go.Scatter(x=df.Canada_year, y=df.CO2_Canada,
                    mode='markers+lines',
                    name='Canada CO2 Emissions'))
    croatia=st.sidebar.checkbox("Croatia")
    if croatia:
        fig.add_trace(go.Scatter(x=df.Croatia_year, y=df.CO2_Croatia,
                    mode='markers+lines',
                    name='Croatia CO2 Emissions'))
    cyprus=st.sidebar.checkbox("Cyprus")
    if cyprus:
        fig.add_trace(go.Scatter(x=df.Cyprus_year, y=df.CO2_Cyprus,
                    mode='markers+lines',
                    name='Cyprus CO2 Emissions'))
    czech=st.sidebar.checkbox("Czech Republic")
    if czech:
        fig.add_trace(go.Scatter(x=df.Czech_year, y=df.CO2_Czech,
                    mode='markers+lines',
                    name='Czech Republic CO2 Emissions'))
    denmark=st.sidebar.checkbox("Denmark")
    if denmark:
        fig.add_trace(go.Scatter(x=df.Denmark_year, y=df.CO2_Denmark,
                    mode='markers+lines',
                    name='Denmark CO2 Emissions'))
    estonia=st.sidebar.checkbox("Estonia")
    if estonia:
        fig.add_trace(go.Scatter(x=df.Estonia_year, y=df.CO2_Estonia,
                    mode='markers+lines',
                    name='Estonia CO2 Emissions'))
    finland=st.sidebar.checkbox("Finland")
    if finland:
        fig.add_trace(go.Scatter(x=df.Finland_year, y=df.CO2_Finland,
                    mode='markers+lines',
                    name='Finland CO2 Emissions'))
    france=st.sidebar.checkbox("France")
    if france:
        fig.add_trace(go.Scatter(x=df.France_year, y=df.CO2_France,
                    mode='markers+lines',
                    name='France CO2 Emissions'))
    germany=st.sidebar.checkbox("Germany")
    if germany:
        fig.add_trace(go.Scatter(x=df.Germany_year, y=df.CO2_Germany,
                    mode='markers+lines',
                    name='Germany CO2 Emissions'))
    greece=st.sidebar.checkbox("Greece")
    if greece:
        fig.add_trace(go.Scatter(x=df.Greece_year, y=df.CO2_Greece,
                    mode='markers+lines',
                    name='Greece CO2 Emissions'))
    hungary=st.sidebar.checkbox("Hungary")
    if hungary:
        fig.add_trace(go.Scatter(x=df.Hungary_year, y=df.CO2_Hungary,
                    mode='markers+lines',
                    name='Hungary CO2 Emissions'))
    iceland=st.sidebar.checkbox("Iceland")
    if iceland:
        fig.add_trace(go.Scatter(x=df.Iceland_year, y=df.CO2_Iceland,
                    mode='markers+lines',
                    name='Iceland CO2 Emissions'))
    ireland=st.sidebar.checkbox("Ireland")
    if ireland:
        fig.add_trace(go.Scatter(x=df.Ireland_year, y=df.CO2_Ireland,
                    mode='markers+lines',
                    name='Ireland CO2 Emissions'))
    italy=st.sidebar.checkbox("Italy")
    if italy:
        fig.add_trace(go.Scatter(x=df.Italy_year, y=df.CO2_Italy,
                    mode='markers+lines',
                    name='Italy CO2 Emissions'))
    japan=st.sidebar.checkbox("Japan")
    if japan:
        fig.add_trace(go.Scatter(x=df.Japan_year, y=df.CO2_Japan,
                    mode='markers+lines',
                    name='Japan CO2 Emissions'))
    latvia=st.sidebar.checkbox("Latvia")
    if latvia:
        fig.add_trace(go.Scatter(x=df.Latvia_year, y=df.CO2_Latvia,
                    mode='markers+lines',
                    name='Latvia CO2 Emissions'))
    liechtenstein=st.sidebar.checkbox("Liechtenstein")
    if liechtenstein:
        fig.add_trace(go.Scatter(x=df.Liechtenstein_year, y=df.CO2_Liechtenstein,
                    mode='markers+lines',
                    name='Liechtenstein CO2 Emissions'))
    lithuania=st.sidebar.checkbox("Lithuania")
    if lithuania:
        fig.add_trace(go.Scatter(x=df.Lithuania_year, y=df.CO2_Lithuania,
                    mode='markers+lines',
                    name='Lithuania CO2 Emissions'))
    luxembourg=st.sidebar.checkbox("Luxembourg")
    if luxembourg:
        fig.add_trace(go.Scatter(x=df.Luxembourg_year, y=df.CO2_Luxembourg,
                    mode='markers+lines',
                    name='Luxembourg CO2 Emissions'))
    malta=st.sidebar.checkbox("Malta")
    if malta:
        fig.add_trace(go.Scatter(x=df.Malta_year, y=df.CO2_Malta,
                    mode='markers+lines',
                    name='Malta CO2 Emissions'))
    monaco=st.sidebar.checkbox("Monaco")
    if monaco:
        fig.add_trace(go.Scatter(x=df.Monaco_year, y=df.CO2_Monaco,
                    mode='markers+lines',
                    name='Monaco CO2 Emissions'))
    netherlands=st.sidebar.checkbox("Netherlands")
    if netherlands:
        fig.add_trace(go.Scatter(x=df.Netherlands_year, y=df.CO2_Netherlands,
                    mode='markers+lines',
                    name='Netherlands CO2 Emissions'))
    zealand=st.sidebar.checkbox("New Zealand")
    if zealand:
        fig.add_trace(go.Scatter(x=df.Zealand_year, y=df.CO2_Zealand,
                    mode='markers+lines',
                    name='New Zealand CO2 Emissions'))
    norway=st.sidebar.checkbox("Norway")
    if norway:
        fig.add_trace(go.Scatter(x=df.Norway_year, y=df.CO2_Norway,
                    mode='markers+lines',
                    name='Norway CO2 Emissions'))
    poland=st.sidebar.checkbox("Poland")
    if poland:
        fig.add_trace(go.Scatter(x=df.Poland_year, y=df.CO2_Poland,
                    mode='markers+lines',
                    name='Poland CO2 Emissions'))
    portugal=st.sidebar.checkbox("Portugal")
    if portugal:
        fig.add_trace(go.Scatter(x=df.Portugal_year, y=df.CO2_Portugal,
                    mode='markers+lines',
                    name='Portugal CO2 Emissions'))
    romania=st.sidebar.checkbox("Romania")
    if romania:
        fig.add_trace(go.Scatter(x=df.Romania_year, y=df.CO2_Romania,
                    mode='markers+lines',
                    name='Romania CO2 Emissions'))
    russia=st.sidebar.checkbox("Russia")
    if russia:
        fig.add_trace(go.Scatter(x=df.Russia_year, y=df.CO2_Russia,
                    mode='markers+lines',
                    name='Russia CO2 Emissions'))
    slovakia=st.sidebar.checkbox("Slovakia")
    if slovakia:
        fig.add_trace(go.Scatter(x=df.Slovakia_year, y=df.CO2_Slovakia,
                    mode='markers+lines',
                    name='Slovakia CO2 Emissions'))
    slovenia=st.sidebar.checkbox("Slovenia")
    if slovenia:
        fig.add_trace(go.Scatter(x=df.Slovenia_year, y=df.CO2_Slovenia,
                    mode='markers+lines',
                    name='Slovenia CO2 Emissions'))
    spain=st.sidebar.checkbox("Spain")
    if spain:
        fig.add_trace(go.Scatter(x=df.Spain_year, y=df.CO2_Spain,
                    mode='markers+lines',
                    name='Spain CO2 Emissions'))
    sweden=st.sidebar.checkbox("Sweden")
    if sweden:
        fig.add_trace(go.Scatter(x=df.Sweden_year, y=df.CO2_Sweden,
                    mode='markers+lines',
                    name='Sweden CO2 Emissions'))
    switzerland=st.sidebar.checkbox("Switzerland")
    if switzerland:
        fig.add_trace(go.Scatter(x=df.Switzerland_year, y=df.CO2_Switzerland,
                    mode='markers+lines',
                    name='Switzerland CO2 Emissions'))
    turkey=st.sidebar.checkbox("Turkey")
    if turkey:
        fig.add_trace(go.Scatter(x=df.Turkey_year, y=df.CO2_Turkey,
                    mode='markers+lines',
                    name='Turkey CO2 Emissions'))
    ukraine=st.sidebar.checkbox("Ukraine")
    if ukraine:
        fig.add_trace(go.Scatter(x=df.Ukraine_year, y=df.CO2_Ukraine,
                    mode='markers+lines',
                    name='Ukraine CO2 Emissions'))
    uk=st.sidebar.checkbox("United Kingdom")
    if uk:
        fig.add_trace(go.Scatter(x=df.UK_year, y=df.CO2_UK,
                    mode='markers+lines',
                    name='United Kingdom CO2 Emissions'))

    fig.update_xaxes(
        title_text = 'Year',
    )
    fig.update_yaxes(
        title_text = "Kilotonnes"
    )

st.plotly_chart(fig, use_container_width=False)
