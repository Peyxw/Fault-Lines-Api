# Fault-Lines-Api
This api is for you; Data such as Micro Plates and Major Fault Zones, Plate interfaces, Plate Movements in a single JSON file. presents it to you.



## Features
- USGS uses the parameters that the system uses.
- presents three data in the same file


## Setup
Download required modules.
# Use
This instruction for use has been created for you to install on your own computer.
```py
py index.py

```
When the system works, it will give you an internet address, you can log in from there.
###JSON Output
```json
{
  "type": "FeatureCollection",
  "name": "Micro Plates and Major Fault Zones",
  "creative": {
    "Name": "Emin",
    "Github": "https://github.com/Peyxw",
    "Gmail": "eminnesatg@gmail.com",
    "nickname": "Peyxw"
  },
  "Micro_Plates_and_Major_Fault_Zones": [
    {
      "type": "Feature",
      "properties": {
        "Name": "Tamayo Fracture Zone",
        "description": null,
        "altitudeMode": "clampToGround",
        "LABEL": "Transform Boundary",
        "Field_1": "Tamayo Fracture Zone"
      },
      "geometry": {
        "type": "MultiLineString",
        "coordinates": [
          [
            [
              -106.8899999996003,
              21.79900000034979
            ],
            [
              -107.0459999999001,
              21.75399999990015
            ],
            [
              -107.1709999996502,
              21.7520000002998
            ],
            [
              -107.3930000002498,
              21.74800000019991
            ],
            [
              -107.5859999999,
              21.74199999960035
            ],
            [
              -107.7740000000999,
              21.74
            ],
            [
              -107.9279999999001,
              21.686
            ],
            [
              -108.1139999996003,
              21.72000000039975
            ],
            [
              -108.3970000001498,
              21.83500000034979
            ],
            [
              -108.5819999996003,
              21.90499999985019
            ],
            [
              -108.5820008557549,
              21.90500050077253
            ],
            [
              -108.5867013144141,
              21.90775076878299
            ]
          ]
        ]
      }
    }
  ],
  "Plate_Interface": [
    {
      "type": "Feature",
      "properties": {
        "Name": "Eurasian:North American",
        "description": null,
        "altitudeMode": "clampToGround",
        "LABEL": "Transform Boundary",
        "Field_1": "Eurasian:North American"
      },
      "geometry": {
        "type": "MultiLineString",
        "coordinates": [
          [
            [
              66.3010025028633,
              86.60600280798326
            ],
            [
              66.54399871806646,
              86.65499877957006
            ]
          ]
        ]
      }
    }
  ],
  "Plate_Motion": [
    {
      "type": "Feature",
      "properties": {
        "Name": "PA-NA",
        "description": "<img src=\"usgs.jpg\" alt=\"USGS\" style=\"width:200px;height:150px;\"></img><br></br> <font size=\"4.5\"> <b>Plates: </b>PA-NA<br></br><b>Velocity: </b>76 mm/yr</font>"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          164.73,
          54.72
        ]
      }
    }
  ]
}
```



# Support Request

If you have any questions or stuck anywhere, you can contact me at eminnesatg@gmail.com.
# Contribution
[Contribution](https://opensource.guide/tr/how-to-contribute/) You can contribute by reviewing.


``` 
MIT License

Copyright (c) 2023 Emin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
