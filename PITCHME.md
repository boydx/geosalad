---?image=images/skybridge-4.jpg
# GEO 409:06
### Intro in lidar data and advanced data structures in Python



---
# Field Trip
### October 25

---?image=images/fieldtrip_geo409_191025-1.jpg
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Courthouse Rock, 103 ft high?</h3>

---?image=images/fieldtrip_geo409_191025-2.jpg
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Stairs to base</h3>

---?image=images/fieldtrip_geo409_191025-3.jpg
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Red River</h3>

---?image=images/skybridge-1.jpg
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">A little scary on the bridge</h3>

---?image=images/fieldtrip_geo409_191025-4.jpg
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Up to Jump Rock</h3>

---
## Midterm & Lab 4
@ul[start]
* Watch/read [Charles Severance](https://www.py4e.com/book.php)
* Code has idioms, just like foreign languages
* Focus on solving problems with code
@ulend


---
## Clip and Hillshade
@ul[start]
* Common tool in GIS
* Data managment and visualization
* Solution on Canvas in Jupyter Notebook
@ulend


---
@[1]
@[2-3]
@[4-5]
@[6-7]
@[8-9]
@[10-11]
```python
import arcpy
# Make root GIS folder a variable
myRoot = "BoydsGIS" 
# Add that variable to file path for data GDB.
arcpy.env.workspace = f"c:\\{myRoot}\\data\\rrg_build.gdb" 
# Make variable of file path for output GDB.
myOutputGDB = f"c:\\{myRoot}\\L2\\output.gdb"
# Area of interest layer
aoi = "area_of_interest"
# Overwrite property is toggled to true.
arcpy.env.overwriteOutput = True
```

---
@[1-4]
@[5-8]
```python
# Use ArcPY function to check if asset exists
if arcpy.Exists(myOutputGDB):
    # If it does, print out the location.
    print(f"{myOutputGDB} geodatabase ready for action!")
else:
    # Else if it doesn't create it and print location
    arcpy.CreateFileGDB_management (f"c:\\{myRoot}\\L2", "output.gdb")
    print(f"Created: {myOutputGDB}")
```

---
@[1-4]
@[2]
@[3-4]
@[5-8]
```python
# Use ArcPy function create a list of feature classes, aka vector layers
featureLayers = arcpy.ListFeatureClasses()
for layer in featureLayers:
    print(f"Vector: {layer}")
# Use ArcPy function create a list of raster layers
rasterLayers = arcpy.ListRasters()
for layer in rasterLayers:
    print(f"Raster: {layer}")
```


---
@[1-5]
@[5]
@[6-9]
@[9]
```python
# Loop through vector layers in GDB
for layer in featureLayers:
    print(f"Vector: {layer}")
    if layer != aoi:
        arcpy.Clip_analysis (layer, aoi, f"{myOutputGDB}\\{layer}", "#")
# Loop through raster layers in GDB
for layer in rasterLayers:
    print(f"Raster: {layer}")
    arcpy.Clip_management (layer, "#", f"{myOutputGDB}\\{layer}", aoi)
```

---
@[1-2]
@[3]
@[4-5]
@[6-7]
```python
# Hillshade script
in_raster = "DEM_2016_5ft" # Initial raster file.
lo_res = "dem_15ft"        # Lower resolution format to save processing time.
azimuth = 90               # Starting azimuth angle
altitude = 45               # The altitude angle for all the hillshades
model_shadows = "NO_SHADOWS"  # Only considers the illumination angle and no local shadows 
z_factor = 1               # x, y, and z dimensions are in the same units
```


---
@[1-2]
@[3-4]
@[5-7]
@[8-9]
```python
# Reduce resolution to increase processing time
arcpy.Resample_management (in_raster, f"{myOutputGDB}\\{lo_res}", 15, "CUBIC")
# Switch workspace to output
arcpy.env.workspace = myOutputGDB
# create describe object and print the raster's dimensions
describeLayer = arcpy.Describe(lo_res) 
print(f"Low resolution pixel height: {describeLayer.height}, width: {describeLayer.width}")
# Create hillshade
arcpy.HillShade_3d(lo_res, "hillshade_90_45", azimuth, altitude, "SHADOWS", 1)
```

---
@[1]
@[2]
@[3]
@[4]
@[5-7]
```python
# Iterate through parameters.
while azimuth <= 270: 
    out_raster = f"hillshade_{azimuth}_{altitude}"
    arcpy.HillShade_3d(lo_res, out_raster, azimuth, altitude, model_shadows, z_factor)
    print(f"Creating {out_raster} in {myOutputGDB}")
    print(azimuth)
    azimuth += 90
```

---
# Next?
@ul[start]
* Discover workflow to build point cloud
* Measure features
* Discover a way to code it in Python
@ulend

---?image=images/a033.png
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Natural Bridge</h2>
[animation](http://uky-gis.github.io/support/lidar-arcgis/view_control.gif)

---?image=images/skybridge-1-2.jpg
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Hen's Nest</h2>
[animation](https://giphy.com/gifs/lidar-hens-nest-sky-bridge-1ULAUtK63aM2cLBYMm/fullscreen)

---
# Start!
@ul[start]
* Don't worry about GitHub lesson repo in beginning
* Create folder, `c:\YourGIS\L6`
* Download data from Canvas
* Open and save L5 map to L6 directory
@ulend


---
### (light detection and ranging)
## Lidar
Uses laser light to densely sample the surface of the earth to make highly accurate x,y,z measurements.

---
### Lidar properties
@ul[start]
* Active sensor transmits pulses of light
* Sensor records time of return
* First return top (building/tree top), last return bottom (bare earth)
* Point cloud of XYZ positions
* [More info](http://pro.arcgis.com/en/pro-app/help/data/las-dataset/use-lidar-in-arcgis-pro.htm)
@ulend

---
### Kentucky lidar
At the forefront of providing access to data
#### [usgs.entwine.io](https://usgs.entwine.io/)

---
### KY lidar data sources
[ftp://ftp.kymartian.ky.gov/kyaped/LAZ](ftp://ftp.kymartian.ky.gov/kyaped/LAZ)
@ul[start]
* LASer (LAS) is common public GIS format
* LAZ is a zipped LAS file
* Create ArcGIS LAS dataset (LASD) by merging LAS files
@ulend

---
### Access interactively
@ol[start]
* Load data from Canvas  
* Add "KY_5k_PointCloud_grid"  
* Click on area for Auxier Ridge 
@olend

---?image=images/a01.png&size=contain&color=#919191

---?image=images/a015.png&size=contain&color=#919191

---
### Extract from .laz file
@code[bat zoom-10](src/convertlas.bat)
@snap[south span-100]
@[1, zoom-15](Change directory to your data space)
@[2, zoom-15](call utiltity)
@[3, zoom-15](input .laz file)
@[4, zoom-15](output .las file)
@snapend


---?image=images/a02.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Create LAS dataset</h2>

---?image=images/a03.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Explore LAS dataset</h2>

---?image=images/a04.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Filter for ground points</h2>

---?image=images/a05.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Add symbology</h2>

---?image=images/a06.png&size=contain&color=#919191

---
### LAS Dataset to Raster tool
@ul
* Input is LAS dataset filtered for ground points
* *Sampling size* parameter (pixel resolution) is 5 (5-ft pixel)
* Other parameters are default
@ulend


---?image=images/a07.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">LAS Dataset to Raster</h2>

---?image=images/a08.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Convert to local scene</h2>

---?image=images/a09.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Add elevation source</h2>

---
### Access aerial photography
* Add ArcGIS Server *https://kyraster.ky.gov/arcgis/services*
* Load 2016 NAIP imagery

---?image=images/a016.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Add aerial photography</h2>

---?image=images/a017.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">KY NAIP 2016 2ft</h2>

---
### Clip aerial photography
1. Create polygon from extent of LAS dataset
* Use the LAS DEM as input raster
* Tool: **Raster Domain**

---?image=images/a018.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Raster Domain</h2>

---?image=images/a019.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">New area of interest</h2>

---
### Clip areal photography
2. Use raster clip tool to clip to area of interest

---?image=images/a020.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Raster Clip</h2>

---
### Add new image to Scene
* Locate your landform
* Spin around and explore
* Perform preliminary measurements

---?image=images/a021.png&size=contain&color=#919191
[animation](https://uky-gis.github.io/support/lidar-arcgis/locate_arch.gif)


---
### Create new empty layer for landform
* Right-click geodatabase
* Select **New > Feature Class**
* Feature Class Type is **Point**
* Spatial Reference is NAD 1983 StatePlane Kentucky FIPS 1600 Feet

---?image=images/a022.png&size=contain&color=#919191

---?image=images/a023.png&size=contain&color=#919191

---?image=images/a024.png&size=contain&color=#919191

---
### Add new point for landform
* Add layer to **Contents**
* Access **Edit > Create Features**
* Drop on center of landform
* **Save** edits

---?image=images/a025.png&size=contain&color=#919191

---?image=images/a026.png&size=contain&color=#919191

---
### Buffer point
* Buffer point at 1,000 ft radius
* New, high resolution area of interest

---?image=images/a027.png&size=contain&color=#919191

---
### View buffer in 3D
* Edit buffer **Layer Properties**
* Set **Elevation** property to **Absolute Height**
* Use **Expression** and set feet above sea level

---?image=images/a028.png&size=contain&color=#919191

---
### Extract LAS Dataset
* Use new buffer polygon to extract LAS points
* Outputs new LAS point cloud
* Put in separate folder **outside** of any repository

---?image=images/a029.png&size=contain&color=#919191

---?image=images/a030.png&size=contain&color=#919191

---
### Colorize LAS Dataset
* Use NAIP aerial imagery to add RGB values
* Outputs yet another LAS point cloud
* Put in separate folder **outside** of any repository

---?image=images/a031.png&size=contain&color=#919191

---?image=images/a032.png&size=contain&color=#919191

---?image=images/a033.png&size=contain&color=#919191
[animation](http://uky-gis.github.io/support/lidar-arcgis/view_control.gif)

---?image=images/a034.png&size=contain&color=#919191

---?image=https://farm8.staticflickr.com/7006/13159570895_96e15d3d15_h.jpg


---
## Python III
### Advanced data structures

---
### Lists
### Tuples
### Dictionaries
### DataFrames

---
## List
A mutable sequence of values separated by a comma and enclosed in square brackets

---
### List methods
* `.sort()`
* `.append()`
* `.remove()`

---
### Useful list functions
* `len()`
* `range()`

---
### Access (and change) elements
```python
for i in range(len(archesList)):
    print(f"The index of {archesList[i]} is {i}")
```

---
## Tuple
An immutable sequence of values separated by a comma and enclosed in round brackets

---
### Exercise using lists and tuples
### Sort arches by name and elevation
Download [Kentucky GNIS (or US)](https://www.usgs.gov/core-science-systems/ngp/board-on-geographic-names/download-gnis-data)

---
```python
import csv #module to handle csv files
with open("KY_Features_20181001.txt", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter="|")
    for row in reader:
        print(row)
```

---
## Dictionary
An unordered collection of items that stored as key:value pairs separated by a comma and enclosed in curly brackets

---
## DataFrame
A two-dimensional tabular data structure and the primary data structure for pandas

```python
import pandas as pd

with open("KY_Features_20181001.txt", encoding='utf-8') as csvfile:
    reader = pd.read_csv(csvfile, delimiter='|')
    pdData = pd.DataFrame(reader)

print(pdData)
```

---
### [Help with Lab 6](https://github.com/UKy-GIS/uky-gis.github.io/tree/master/support/python-arcgis/examples)

---?image=images/skybridge-3.jpg&size=contain&color=linear-gradient(to top, #000, #333)
@snap[north-west text-italic text-18]
Cliffs along Red River
@snapend

---?image=images/skybridge-4.jpg
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Sky Bridge</h3>




