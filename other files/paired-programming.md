# Paired programming  
### Goal of the project:  
If I am right the goal of this project is to create a plot or graph to visualize the data to show climate changes by using `streamlit`, `pandas`, `numpy`, `matplotlib`, `meteostat`, `geopandas`, `folium`, and `scikit-learn` packages.

### The data:  
I believe the data will be a sebset of public-available geopraphic and climate data. I also think it is better to work with part of those data to make the whole process less time consuming.

### Code:  
I noticed that you are on the very beginning of this project so keep it up. I also found out that you are using `https://github.com/floodowen/climatetool/blob/main/seaice.csv` for the URL of your data file, and I suppose it is better to use `https://raw.githubusercontent.com/athe1sm/climatetool/main/seaice.csv` instead to avoid those headers(?).  
I think a REST API might be helpful to your project.

### Contribution:  
1. I have added a new `webapp` module to present some datasets. See the module for more details. e.g. you can use `uvicorn` to run a local server and visit `localhost:8000/climatedata?category=seaice` to see a cropped `seaice.csv`
