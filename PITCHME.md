---?image=images/skybridge-4.jpg
# GEO 409:07
### Working with lidar in ArcGIS Pro

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
@[2, zoom-15](call utility)
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
* Load 2018 NAIP imagery

---?image=images/a016.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Add aerial photography</h2>

---?image=images/a017.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">KY NAIP 2018 2ft</h2>

---
### Clip aerial photography
@ul
1. Create polygon from extent of LAS dataset
* Use the LAS DEM as input raster
* Tool: **Raster Domain**
@end

---?image=images/a018.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Raster Domain</h2>

---?image=images/a019.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">New area of interest</h2>

---
### Clip aerial photography
2. Use raster clip tool to clip to area of interest

---?image=images/a020.png&size=contain&color=#919191
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Raster Clip</h2>

---
### Add new image to Scene
@ul
* Locate your landform
* Spin around and explore
* Perform preliminary measurements
@ulend

---?image=images/a021.png&size=contain&color=#919191
[animation](https://uky-gis.github.io/support/lidar-arcgis/locate_arch.gif)


---
### Create new empty layer for landform
@ul
* Right-click geodatabase
* Select **New > Feature Class**
* Feature Class Type is **Point**
* Spatial Reference is NAD 1983 StatePlane Kentucky FIPS 1600 Feet
@ulend

---?image=images/a022.png&size=contain&color=#919191

---?image=images/a023.png&size=contain&color=#919191

---?image=images/a024.png&size=contain&color=#919191

---
### Add new point for landform
@ul
* Add layer to **Contents**
* Access **Edit > Create Features**
* Drop on center of landform
* **Save** edits
@ulend

---?image=images/a025.png&size=contain&color=#919191

---?image=images/a026.png&size=contain&color=#919191

---
### Buffer point
* Buffer point at 1,000 ft radius
* New, high resolution area of interest

---?image=images/a027.png&size=contain&color=#919191

---
### View buffer in 3D
@ul
* Edit buffer **Layer Properties**
* Set **Elevation** property to **Absolute Height**
* Use **Expression** and set feet above sea level
@ulend

---?image=images/a028.png&size=contain&color=#919191

---
### Filter LAS Dataset
@ul
* Remove noise (class codes 7 and 18)
* Double-click LAS Dataset to **Layer Properties**
* Select **LAS Filter**
@ulend

---?image=images/filter.png&size=contain&color=#919191

---
### Extract LAS Dataset
@ul
* Use new buffer polygon to extract LAS points
* Outputs new LAS point cloud
* Put in separate folder **outside** of any repository
@ulend

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
