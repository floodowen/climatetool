# project
An outline of a new project idea

### Description of the project goal:
My program will be used to visualize climate change by creating graphs and maps of different climate data depending on the input of the user.
I think that this will be best used as an interactive web app, and I would like to use the `streamlit` python package to develop it.
One other function I would like to use is to be able to compare regions to highlight areas that are most impacted by climate change.

### Description of the code:
To create the web app, I will use the `streamlit` python package.
I plan to use `pandas` to import and arrange the csv files and analyze the data, and `numpy` will probably be used in this analysis as well
I will use `matplotlib` for some of the viusalizations of the data.
`meteostat` will be used for accessing and installing weather and climate data.
I plan to use `geopandas` for the mapping elements of data visualization, along with `folium`
Finally, I hope to use `scikit-learn` to cluster similar objects into sets

### Description of the data
I have found a few sets of data I plan to use.
First, through Berkeley Earth, I plan to use a dataset that includes Ocean and Land temperatures
  https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalLandTemperaturesByCountry.csv
  
Second, through The World Bank, I plan to use a dataset containing a variety of climate change variables by country from 1990-2011
  https://datacatalog.worldbank.org/dataset/climate-change-data
  
Third, the United Nations has a dataset on greenhouse gas emissions that I plan to use
  https://www.kaggle.com/unitednations/international-greenhouse-gas-emissions

Fifth, the National Snow and Ice Data Center has a dataset of sea ice extent that could be useful
  https://www.kaggle.com/nsidcorg/daily-sea-ice-extent-data

Finally, additional data may be required from the World Bank's Climate Change Knowledge Portal
  https://climateknowledgeportal.worldbank.org/download-data

### Description of user interaction
Ideally, the user could access an interactive web app and select the climate change variable and country to see a graph of the data over time
Additionally, the user could select some preselected combinations of data, such as a comparison of greenhouse emissions by countries and sea level impacts by country
Another preselected comparison could be the difference in land temperatures of European countries to those of the global south
