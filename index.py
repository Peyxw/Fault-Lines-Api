import re
import json
import time
import threading
import schedule
from urllib.request import urlopen
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from flask import Flask, make_response, request
import random
import requests
import os
import geopandas as gpd
cur_dir = os.path.dirname(os.path.realpath(__file__))



Micro_Plates_and_Major_Fault_Zones = 'data/Micro_Plates_and_Major_Fault_Zones.geojson'

with open(Micro_Plates_and_Major_Fault_Zones, 'r', encoding='utf-8'  ) as f:
    Micro_Plates_and_Major_Fault_Zones = json.load(f)


Plate_Interface = 'data/Plate_Interface.geojson'

with open(Plate_Interface, 'r', encoding='utf-8') as f:
    Plate_Interface = json.load(f)

Plate_Motion = 'data/Plate_Motion.geojson'

with open(Plate_Motion, 'r', encoding='utf-8') as f:
    Plate_Motion = json.load(f)


app = Flask(__name__)

@app.route('/')
def index():
    json_data = json.dumps({ 
        "type" : "FeatureCollection" , 
        "name" : "Micro Plates and Major Fault Zones" ,
        "creative" : {
        "Name": "Emin",
        "Github" : "https://github.com/Peyxw",
        "Gmail" : "eminnesatg@gmail.com",
        "nickname" : "Peyxw"
        },
        "Micro_Plates_and_Major_Fault_Zones" : Micro_Plates_and_Major_Fault_Zones['features'],
        "Plate_Interface" : Plate_Interface['features'],
        "Plate_Motion" : Plate_Motion['features'],

         }, sort_keys=False)   
    res = make_response(json_data)
    res.headers['Content-Type'] = 'application/json'
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

print(Micro_Plates_and_Major_Fault_Zones,Plate_Interface,Plate_Motion)

if __name__ == '__main__':
     app.run(debug=True)


