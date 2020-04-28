---?image=images/geo_depart.png&size=50%&opacity=100

---?image=https://www.outragegis.com/weather/img/animation/yesterday/LookRock.gif&opacity=100
# GEO 409:08
### Mapbox and final project

---
## Announcements
### April 28, 2020

---
## Lesson & Lab 
@ul[squares]
* Are combined
* We'll create a contour layer and make a slippy web map
* Add link to map on your custom repository page
@ulend

---
## Final Project
@ul[squares]
* Showcase three maps or visualizations
* On your custom repository portfolio page
* Add a few other items for content
* Past [example projects](https://uky-gis.github.io/#examples-of-student-work)
@ulend

---
## Alt lab and final project
@ul[squares]
* Create Mapbox map of Natural Bridge 
* With elevation contours and labels
* Use this zipped [Shapefile of contours](https://outragegis.com/d/L8_Geo409_contour_10ft_aoi.zip)
* Submit link to map on Canvas
@ulend

---
## Slippy map
### Pan map and change symbology on zoom
Add interactive layers and you have a map application

---
## Mapbox
@ul[squares]
- primo 🍭 slippy map builder/host
- recognize our connected devices make us sensors
- real-time data-driven location services
- [mapbox.com](https://www.mapbox.com/)
@ulend

---
### Rise of mapping services
<iframe width="560" height="315" src="https://www.youtube.com/embed/1lrJug1kgM0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe><br>
It's a good time to be a cartographer!

---
# Video
## for Mapbox portion of this module
Check Canvas for link

---?image=images/s01.jpg&opacity=100

---
## Map tiles
# Base maps

---
## mid 2000s
# Raster tiles
#### 256x256 pixel image


---
## 2014
# Vector tiles
#### geometries and metadata

---
## Raster v. Vector
# Compare
* [OSM](https://www.openstreetmap.org/#map=2/37.3/-79.4)
* [Mapbox](https://api.mapbox.com/styles/v1/mapbox/streets-v9.html?title=true&access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA#1.07/0/0)

---
### The winner
<iframe src="https://api.mapbox.com/styles/v1/mapbox/streets-v9.html?title=true&access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA#1.07/0/0" width="100%" height="500"></iframe>

---
## Mapbox uses
# OSM Data
Consider their license requirement:

`© Mapbox © OpenStreetMap Improve this map.`

---
### [mapbox.com/signup](https://www.mapbox.com/signup/)

---
## Terminology
@ul[squres]
* **Dataset** is editable
* **Tileset** is symbolized
    * Tilesets can contain many layers
* **Style** is a map
@ulend

---
### Formats we can use (open source)
* **Vector**: Shapefile, GeoJSON (edited) at EPSG: 4326
* **Raster**: GeoTIFF, EPSG: 3857

---
## Studio
@ul[squres]
* The Photoshop of online mapping
* Rule-based classification and symbology
* Change appearance as we zoom
@ulend

---
## Styles
@ul[squares]
* Aka "the map"
* Symbolized tilesets that we can share
* Free, curated "Designer" sets!
@ulend

---
## Their imagery is amazing
<iframe width="560" height="315" src="https://www.youtube.com/embed/1C2PbWr9tpY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

---
### Google Maps
<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d1767.8700418407502!2d-84.50757895563086!3d38.0442129886452!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e1!3m2!1sen!2sus!4v1523388053130" width="100%" height="500" frameborder="0" style="border:0" allowfullscreen></iframe>

---
### Mapbox
<iframe src="https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9.html?title=true&access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA#17.23/38.044077/-84.507715" width="100%" height="500"></iframe>


---
### Other services
* [ArcGIS Online](https://developers.arcgis.com/)
* [Here XYZ Beta](https://explore.xyz.here.com/)
* Require payment (at volume) and familiarity with coding


---
# Contouring

Contours are in meter units on Mapbox. Create contours on ArcGIS Pro

---
## Step 1
Do **Focal Statistics** on our bare-earth DEM to help smooth contours with the mean (average) statistic.

---
## Step 2
**Contour** to make elevation contours with a 20-foot interval (or 10-ft interval).

---
## Step 3
**Field Calculator** to make index contours for every 100 feet. An index contour has an attribute that allows us to symbolize it differently on the map.

---
## Step 4 
Use the **Clip** tool to reduce the size of area to the buffered area of interest and export Shapefile of contours that will load into Mapbox.

---
## Or use Jupyter Notebook
in the module repository


---
# Mapbox

---
## Step 1
Load datasets into Mapbox
@ul[squares]
* Load arches.geojson as a Dataset
* Load zipped contours as a Tileset
@ulend

---
## Step 2
Create new style
@ul[squares]
* Add arches and contours to new map
* Symbolize features
* Adjust layers to fade on zoom
@ulend

---
## Step 3
Publish style
@ul[squares]
* Share URL
@ulend


---
# Web Publishing

---
## URL
Uniform resource locator makes the internet work because it provides a unique address for **all** resources on the internet.

---
## Characteristics
@ul
* `https://tastyfreeze.github.io/rrg`
    * domains: sub.main.top-level
* forward slashes `/` separate directories
* Most servers *surface* index.html (don't have to type it)
* No spaces in file names for us
* Look for file extension
* Case sensitive
@ulend

---
## Linking
@ul
* Use relative paths if asset is in your repo
    * `../index.html` 
        * up one directory
    * `rrg/basemap/image.jpg` 
        * down two directories
@ulend

---
## Examples
* Maddie [code](https://github.com/maddyblandford/rrg) | [rendered](https://maddyblandford.github.io/rrg/)
* Alex [code](https://github.com/alexgis-projects/rrg) | [rendered](https://alexgis-projects.github.io/rrg/elevation/)
* Conner [code](https://github.com/CRLedington/rrg) | [rendered](https://CRLedington.github.io/rrg/)
* Jerry [code](https://github.com/jmo335/rrg) | [rendered](https://jmo335.github.io/rrg)
* Beth Ann [code](https://github.com/Winebarger/RRG2) | [rendered](https://Winebarger.github.io/RRG2)