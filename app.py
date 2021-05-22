#Create 

from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify
import  numpy as np


#Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect a database into a new model 

Base = automap_base()

# Reflect the tables 

Base.prepare(engine,reflect=True)

#Save references to each table 

measurement = Base.classes.measurement
Station = Base.classes.station 

#Setup Flask 
app = Flask(__name__)

#Routes 
@app.route("/")
def welcome():
    """List all api routes."""
    return(
        f"Available Routes:<br/> "
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]<br/>"
    )
