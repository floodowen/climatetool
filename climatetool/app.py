from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse
from climatetool.climatetool import Climate_plot

#creat the app as an instance
app = FastAPI()

# create an end point 
@app.get("/")
def root():
    return {"message": """Go to /plot"""} 

@app.get("/plot", response_class=HTMLResponse)
def plot(data_type: str):
	climate_class = Climate_plot()
	p = climate_class.temp_plot()
	return p._repr_html_()