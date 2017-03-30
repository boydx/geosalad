#HSLIDE
#GEO 409:05
##Week 10

#HSLIDE?image=http://townbranchtiger.com/wp-content/uploads/2016/04/160429_-TBCTiger_Map.jpg
<h2 style="color:#f00;text-shadow: 2px 2px 4px #fff;">New Town Branch Trail plans</h2>

#HSLIDE?image=http://www.kentucky.com/news/local/counties/fayette-county/itl4rl/picture141169983/ALTERNATES/FREE_960/0_Town%20Branch%20Aerial

#HSLIDE?image=http://www.kentucky.com/news/local/counties/fayette-county/q4nnsq/picture141170018/ALTERNATES/FREE_960/B_Midland%20Avenue%20typical%20bl

#HSLIDE?image=http://www.kentucky.com/news/local/news-columns-blogs/tom-eblen/7erdw3/picture141170308/ALTERNATES/FREE_960/2_Vine%20Street%20near%20Rose

#HSLIDE
<iframe width="100%" height="520" frameborder="0" src="https://nmp.carto.com/u/boyd/builder/52ef1fe6-14a6-11e7-a3f5-0e05a8b3e3d7/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

#HSLIDE
##Final project ideas
If you're struggling to finish labs and want to complete a final project, Town Branch Trail provides new opportunity.

#HSLIDE
##Pivot in direction
###Move towards publishing online maps and content

#HSLIDE
#Raster Processing


#HSLIDE
##Example of what you'll produce
###Terrain relief map of the Town Branch Corridor

#HSLIDE
<iframe width="100%" height="520" frameborder="0" src="http://boydx.github.io/tbt/xyz/hillshade/leaflet.html" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

#HSLIDE
##Challenge
* How we can we do simple spatial analysis and make it look good?
* For example, how many people live within 20 miles of a national park?
* Then, how can we do it anywhere?
* First, we must find a logically ordered global spatial dataset...

#HSLIDE
##OpenStreetMap
####Crowd-sourced map of local knowledge that users can freely harvest.

#HSLIDE?image=images/06/OSM.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="http://www.openstreetmap.org/note/704210#map=11/38.0492/-84.5000&layers=N" target="_blank">OSM</a></h2>
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Greatest mapping project of all time</h3>



#HSLIDE
##OSM

#HSLIDE
##OSM data
* .osm file is human-readable XML
* Builds topology with nodes, ways, relations
* Tags are built with key:value pairs

#HSLIDE
##Harvesting data
* [OpenStreetMap.org](http://www.openstreetmap.org)
* MapZen's [extracts](https://mapzen.com/data/metro-extracts/)
* QuickOSM plugin in QGIS
* DO NOT USE QGIS's Vector tools


#HSLIDE
##Styling data
* Use Rule-based symbology with SQL
* Simple statements like ```"highway" = 'motorway'```
* Change symbols based on scale
* Your first "slippy map!" in QGIS

#HSLIDE
##Lab 4.1: Creating and saving styles
* Create nicely symbolized OSM layers in QGIS
* Add text to roads, streams, and other layers
* Export to QML file format in QGIS


#HSLIDE?image=https://c1.staticflickr.com/4/3671/32680153523_18c7d76906_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Spring Break!</h2>

#HSLIDE?image=https://c1.staticflickr.com/4/3830/32680157893_dcf220c00d_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="https://www.flickr.com/photos/28640579@N02/32680157893/in/dateposted-public/" target="_blank">map in the wild!</a></h2>




