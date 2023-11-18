# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes for Hawaii Weather Data:<br/><br>"
        f"-- Daily Precipitation Totals for Last Year: <a href=\"/api/v1.0/precipitation\">/api/v1.0/precipitation<a><br/>"
        f"-- Active Weather Stations: <a href=\"/api/v1.0/stations\">/api/v1.0/stations<a><br/>"
        f"-- Daily Temperature Observations for Station USC00519281 for Last Year: <a href=\"/api/v1.0/tobs\">/api/v1.0/tobs<a><br/>"
        f"-- Min, Average & Max Temperatures for Date Range: /api/v1.0/trip/yyyy-mm-dd/yyyy-mm-dd<br>"
        f"NOTE: If no end-date is provided, the trip api calculates stats through 08/23/17<br>" 
    )

# Create a route that retrieves just the last 12 months of precipitation data
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all Precipitation Data"""
    
    # Query all Precipitation
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= "2016-08-24").\
        all()
    session.close()
    
    # Convert this data into a dictionary
    rain = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(rain)

# Create a route that returns a list of stations from the data
/api/v1.0/stations
def stations():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all Stations"""
    
    # Query all Stations
    results = session.query(Station.station).order_by(Station.station).all()
    session.close()
    
    # Populate list of stations
    # Referenced the code below from: https://github.com/sliwet/sqlalchemy-challenge/blob/master/app.py
    stations = []
    for station,name,lat,lon,el in queryresult:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Lat"] = lat
        station_dict["Lon"] = lon
        station_dict["Elevation"] = el
        stations.append(station_dict)

    return jsonify(stations)

# Create a route that returns temperature data from the past year
/api/v1.0/tobs
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all Temperature Data"""
    
    #Query all temperature data
    most_active = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station =='USC00519281').\
    filter(Measurement.date > '2022-11-5').all()
    
    session.close()
    
    # Return a list of temperature data
    most_active_list = [i for i in most_active[0]]

    session.close()

    return jsonify(most_active_list)


   if __name__ == "__main__":
    app.run(debug=True)
