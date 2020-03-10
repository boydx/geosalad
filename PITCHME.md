---?image=https://www.outragegis.com/weather/img/animation/yesterday/LookRock.gif&opacity=40
# GEO 409:05
## Automated geoprocessing & intro to ArcGIS Pro

---
## Online Class
@ul[squares]
* Canvas [course content and new videos](https://uk.instructure.com/courses/1966559)
* Zoom [screen sharing](https://uky.zoom.us/my/boyd.shearer)
* ArcGIS Pro [download & install](https://uk.instructure.com/courses/1966559/files/93580698/download)
* Virtual Den [remote applications](https://appstore.uky.edu/)
@ulend

---
## Lab 4
@ul[squares]
* Get familiar with the tool documentation
    * Don't have to know all settings all the time
* Get comfortable moving data, running code, examining output
@ulend

---
## Lab 5
@ul[squares]
* Clipping data to an AOI with ArcPy
    * Need to work through lesson
* Write new script from lesson example
* Fire up ArcGIS Pro to publish a base map
@ulend

---?image=images/ky-basemap.png&opacity=100

---
## Problem 🧱
Data is not perfectly isolated for your area of interest. The extra load can become an obstacle to efficient mapping.

---
## Solution
## ✂️ 🗺️

---
## Clip tool
@ul[squares]
* Isolate data to area of interest
* Input > function() > Output
* `arcpy.Clip_analysis(in, clip, out)`
* What happens if you have 100 layers?
@ulend


---
## Automate tools
```py
import arcpy
# set default workspace
arcpy.env.workspace = "z:\\myGIS\\data\\myProject.gdb"
# get list of data in the geodatabase
listOfData = arcpy.ListFeatureClasses()
# loop through list
for layer in listOfData:
    # ✂️ 🗺️
    arcpy.Clip_analysis(layer, "area_of_interest", f"{outputDB}\\layer")
```
@[1]
@[2-3]
@[4-5]
@[6-9]

---
## Geoprocessing
"A framework and set of tools for processing geographic and related data."

---
## Automate at scale
@ul[squares]
* Tools chained together
    * Programmatically run an entire workflow
* Operate on unlimited amounts of data
* Once coded, work on same data but from different area
@ulend

---?image=images/tools.png&opacity=100

---
## Example
Imagine if you needed to know the variety and acreage of land use and land cover for all counties in US?

---?image=images/lclu-ky.jpg&opacity=100

---?image=images/lclu-us.jpg&opacity=100

---
## Solution?
@ul[squares]
* for loop [Clip Raster > Export Table]
    * Don't get name of county in table
* RasterToVector > Intersect > for loop [Clip Raster > Export Table]
@ulend

---?image=images/lclu-us-total.jpg&opacity=100