import requests
import json
import time
from random import uniform

def locationGen():
  latitude = uniform(-23.643578, -23.549229)
  longitude = uniform(-46.618219, -46.554714)
  location = [latitude, longitude]
  return location 

id = 1
while(1):
  
  time.sleep(5)
  location = locationGen()
  print(location[0], location[1])
  print(id)
  payload = {"actionType":"APPEND",
    "entities":[
      {
        "id":"location" +  str(id), "type":"Shelf",
        "location":{
          "type":"geo:json", "value":{ "type":"Point","coordinates":[location[0], location[1]]}
        },
      }
    ]
  }
  id += 1
  r = requests.post('http://localhost:1026/v2/op/update', json=payload)

  print(r.status_code)
  print(r.text)