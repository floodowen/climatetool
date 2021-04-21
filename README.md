# Climatetool
My program will be used to visualize climate change by creating graphs of different climate data depending on the input of the user.

This program will put multiple data sets into one easy to use format. Currently climate visualization does exist, but it is either too complex for the user or without much customization. This tool hopefully fills that gap.


### Installation and running the program

To download and run the program, users should follow these directions:

```
install pandas and streamlit
git clone https://github.com/floodowen/climatetool.git
cd ./climatetool
pip install -e .
cd ./climatetool
streamlit run climate.py
```

Once the user runs the program using streamlit from the command line, they will be able to use the local webpage to view variables.
The can choose Global Temperature over Time, Sea Ice Extent, or Carbon Dioxide Emissions.

Global Temperature over Time will show the average global temperature in Farenheit from 1895 to 2020.

Within Sea Ice Extent, the user can select the daily extent from 1978-2019 for the Northern or Southern Hemisphere, \
or they can view the yearly low in the Northern hemisphere from 1978-2018.

Within the Carbon Dioxide Emissions, there are 42 countries and the European Union to choose from
Selecting from these allows for a comparison of Carbon Dioxide emissions in kilotonnes from 1990 to 2014.

#### Dependencies

```
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
```

#### Climate visualizations of interest

One climate impact map is seen here:
http://www.impactlab.org/map/#usmeas=absolute&usyear=1981-2010&gmeas=absolute&gyear=1986-2005
This only allows for user interaction, but not many variables.

Other visualizations give snapshots of different variables, but have limited user interaction, as seen here:
https://www.climate.gov/maps-data
