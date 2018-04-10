#HSLIDE
# GEO 409
## Mapbox


#HSLIDE
## 2014
# Vector tiles
#### geometries and metadata

#HSLIDE
## Raster v. Vector
# Compare
* [OSM](https://www.openstreetmap.org/#map=2/37.3/-79.4)
* [Mapbox](https://api.mapbox.com/styles/v1/mapbox/streets-v9.html?title=true&access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA#1.07/0/0)

#HSLIDE
### The winner
<iframe src="https://api.mapbox.com/styles/v1/mapbox/streets-v9.html?title=true&access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA#1.07/0/0" width="100%" height="500"></iframe>

#HSLIDE?image=images/06/OSM.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="https://www.openstreetmap.org/history#map=11/38.0492/-84.5000&layers=N" target="blank">OSM</a></h2>
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Greatest mapping project of all time</h3>


#HSLIDE
## OSM data
* .osm file is human-readable XML
* Builds topology with nodes, ways, relations
* Tags are built with _key:value_ pairs

#HSLIDE
## Harvesting data
* [OpenStreetMap.org](http://www.openstreetmap.org)
* MapZen's [extracts are no more](https://mapzen.com/)
* QuickOSM plugin in QGIS
* DO NOT USE QGIS's Vector tools

#HSLIDE
## Data used extensively
* [MapBox](https://www.mapbox.com/maps/)
* Look for their open source license requirement:
	* &copy; OpenStreetMap Contributors


#HSLIDE
## Styling data
* Use Rule-based symbology with SQL
* Simple statements like `"highway" = 'motorway'`
* Change symbols based on scale
* Your first [slippy map!](https://tastyfreeze.github.io/hometown-map/lex-parks/tiles.html) in QGIS

#HSLIDE
## Lab: Create base map for your recreation area
* Create nicely symbolized OSM layers in QGIS
* Add text to roads, streams, and other layers
* Export to QML file format in QGIS
* Export map as GeoTIFF (using JPEG compression)
