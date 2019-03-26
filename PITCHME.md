---
# GEO 409:06
### Intro in lidar data and advanced data structures in Python

---?image=images/a033.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Natural Bridge</h2>
[animation](http://uky-gis.github.io/support/lidar-arcgis/view_control.gif)

---?image=images/skybridge-2.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Red River</h2>

---?image=images/skybridge-1.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">A little scary on the bridge</h2>

---?image=images/skybridge-4.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Sky Bridge</h2>

---?image=images/skybridge-1-2.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Hen's Nest</h2>
[animation](https://giphy.com/gifs/lidar-hens-nest-sky-bridge-1ULAUtK63aM2cLBYMm/fullscreen)

---?image=images/skybridge-3.jpg&size=contain&color=black
@snap[north-west]
## Panorama of meander in Red River
@snapend


---
### (light detection and ranging)
# Lidar
Uses laser light to densely sample the surface of the earth to make highly accurate x,y,z measurements.

---
## Lidar properties
* Active sensor transmits pulses of light
* Sensor records time of return
* First return top (building/tree top), last return bottom (bare earth)
* Point cloud of XYZ positions
* [More info](http://pro.arcgis.com/en/pro-app/help/data/las-dataset/use-lidar-in-arcgis-pro.htm)

---
## KY lidar data sources
ftp://ftp.kymartian.ky.gov/kyaped/LAZ/
* LASer (LAS) is common public GIS format
* LAZ is a zipped LAS file
* Create ArcGIS LAS dataset (LASD) by merging LAZ files

---
## Access interactively
1. Load data from Canvas
2. Add "KY_5k_PointCloud_grid"
3. Click on "Natural Bridge"

---?image=images/a01.png

---?image=images/a015.png

---
## Extract from .laz file
```bat
cd /BoydsGIS/data
laszip64.exe
enter input file: N110E348.laz
enter output file: N110E348.las
```

---?image=images/a02.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Create LAS dataset</h2>

---?image=images/a03.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Explore LAS dataset</h2>

---?image=images/a04.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Filter for ground points</h2>

---?image=images/a05.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Add symbology</h2>

---?image=images/a06.png

---
## LAS Dataset to Raster tool
* Input is LAS dataset filtered for ground points
* *Sampling size* parameter (pixel resolution) is 5 (5-ft pixel)
* Other parameters are default


---?image=images/a07.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">LAS Dataset to Raster</h2>

---?image=images/a08.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Convert to local scene</h2>

---?image=images/a09.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Add elevation source</h2>

---
## Access aerial photography
* Add ArcGIS Server *https://kyraster.ky.gov/arcgis/services*
* Load 2016 NAIP imagery

---?image=images/a016.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Add aerial photography</h2>

---?image=images/a017.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">KY NAIP 2016 2ft</h2>

---
## Clip aerial photography
1. Create polygon from extent of LAS dataset
* Use the LAS DEM as input raster
* Tool: **Raster Domain**

---?image=images/a018.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Raster Domain</h2>

---?image=images/a019.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">New area of interest</h2>

---
## Clip areal photography
2. Use raster clip tool to clip to area of interest

---?image=images/a020.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Raster Clip</h2>

---
## Add new image to Scene
* Locate your landform
* Spin around and explore
* Perform preliminary measurements

---?image=images/a021.png
[animation](https://uky-gis.github.io/support/lidar-arcgis/locate_arch.gif)


---
## Create new empty layer for landform
* Right-click geodatabase
* Select **New > Feature Class**
* Feature Class Type is **Point**
* Spatial Reference is NAD 1983 StatePlane Kentucky FIPS 1600 Feet

---?image=images/a022.png

---?image=images/a023.png

---?image=images/a024.png

---
## Add new point for landform
* Add layer to **Contents**
* Access **Edit > Create Features**
* Drop on center of landform
* **Save** edits

---?image=images/a025.png

---?image=images/a026.png

---
## Buffer point
* Buffer point at 1,000 ft radius
* New, high resolution area of interest

---?image=images/a027.png

---
## View buffer in 3D
* Edit buffer **Layer Properties**
* Set **Elevation** property to **Absolute Height**
* Use **Expression** and set feet above sea level

---?image=images/a028.png

---
## Extract LAS Dataset
* Use new buffer polygon to extract LAS points
* Outputs new LAS point cloud
* Put in separate folder **outside** of any repository

---?image=images/a029.png

---?image=images/a030.png

---
## Colorize LAS Dataset
* Use NAIP aerial imagery to add RGB values
* Outputs yet another LAS point cloud
* Put in separate folder **outside** of any repository

---?image=images/a031.png

---?image=images/a032.png

---?image=images/a033.png
[animation](http://uky-gis.github.io/support/lidar-arcgis/view_control.gif)

---?image=images/a034.png

---?image=https://farm8.staticflickr.com/7006/13159570895_96e15d3d15_h.jpg


---
## Python III
### Advanced data structures

---
## [Help with lab 4 and lab 6](https://github.com/UKy-GIS/uky-gis.github.io/tree/master/support/python-arcgis/examples)

---
## Lists
## Tuples
## Dictionaries
## DataFrames

---
# List
A mutable sequence of values separated by a comma and enclosed in square brackets

---
## List methods
* `.sort()`
* `.append()`
* `.remove()`

---
## Useful list functions
* `len()`
* `range()`

## Access (and change) elements
```python
for i in range(len(archesList)):
    print(f"The index of {archesList[i]} is {i}")
```

---
# Tuple
An immutable sequence of values separated by a comma and enclosed in round brackets

---
## Exercise using lists and tuples
### Sort arches by name and elevation
Download [Kentucky GNIS](https://geonames.usgs.gov/domestic/download_data.htm)

---
```python
import csv #module to handle csv files
with open("KY_Features_20181001.txt", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter="|")
    for row in reader:
        print(row)
```

---
# Dictionary
An unordered collection of items that stored as key:value pairs separated by a comma and enclosed in curly brackets

# DataFrame
A two-dimensional tabular data structure and the primary data structure for pandas

```python
import pandas as pd
import numpy as np

with open("KY_Features_20181001.txt", encoding='utf-8') as csvfile:
    reader = pd.read_csv(csvfile, delimiter='|')
    pdData = pd.DataFrame(reader)

print(pdData)
```

---
## [Help with ab 6](https://github.com/UKy-GIS/uky-gis.github.io/tree/master/support/python-arcgis/examples)
