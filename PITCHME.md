---
# GEO 409:06
### Intro in lidar data and advanced data structures in Python


---?image=https://farm2.staticflickr.com/1918/44749579164_54f9039f9d_h.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">NACIS</h2>

---?image=https://farm2.staticflickr.com/1941/44560608585_5273398801_h.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Wis + Ky</h2>


---?image=https://farm2.staticflickr.com/1976/43657250080_c8bb35badf_h.jpg

---
### Map winners from UW and UKy
## [Oil & Bone](https://www.kgmaps.com/oil-and-bone/)
### Kerry Gathers, UKy

---
### Student won
# $500 
(you could too)

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

---?image=images/a07.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">LAS Dataset to Raster</h2>

---?image=images/a08.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Convert to local scene</h2>

---?image=images/a09.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Add elevation source</h2>

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