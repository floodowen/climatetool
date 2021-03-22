# Climatetool
My program will be used to visualize climate change by creating graphs and maps of different climate data depending on the input of the user.

This program will put multiple data sets into one easy to use format. Currently climate visualization does exist, but it is either too complex for the user or without much customization. This tool hopefully fills that gap.

One climate impact map is seen here:
http://www.impactlab.org/map/#usmeas=absolute&usyear=1981-2010&gmeas=absolute&gyear=1986-2005
This only allows for user interaction, but not many variables.

Other visualizations give snapshots of different variables, but have limited user interaction, as seen here:
https://www.climate.gov/maps-data

### In Development

To download and run the program, users should follow these directions:

For now:

git clone https://github.com/floodowen/climatetool.git
cd ./climatetool
pip install -e .
type in climatetool


Later:

conda install pandas as pd numpy as np matplotlib meteostat geopandas folium scikit-learn -c conda-forge ...

```
git clone https://github.com/floodowen/climatetool.git
cd ./climatetool
pip install -e .
```
