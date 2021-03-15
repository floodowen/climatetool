from fastapi import FastAPI
import pandas as pd
import requests
import json
'''
This is a startup on the construction of webapp. At this point you can use this to access two cropped datasets, and when the devemopment 
goes on it can support the display of those plots 
'''
# create the app as an instance of the fastAPI class
app = FastAPI()

# load the database once when the server starts

SEAICEDATA = pd.read_csv("/home/athe1sm/hacks/climatetool/seaice_cropped.csv") # Feel free to change this to an URL. I can't do this since I don't have access to github on wsl2
GREENHOUSEDATA = pd.read_csv("/home/athe1sm/hacks/climatetool/greenhouse_gas_inventory_data_data_cropped.csv")
# create a root endpoint that say's hello
@app.get("/")
def root():
    "returns a hello world message"
    return {"message": "If you can see this, the server is running"}

# create another endpoint for returning iris data
@app.get("/climatedata")
def climatedata(category='seaice'):
    """
    returns climate data in JSON with option to subselect a category
    """
    # get subset or full data
    if category == "seaice":
        data = SEAICEDATA
    else:
        data = GREENHOUSEDATA

    # convert to JSON and return to endpoint
    sdata = data.to_json(orient="index")
    jdata = json.loads(sdata)
    return jdata