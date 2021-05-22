#Create 

from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify
import  numpy as np


#Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")