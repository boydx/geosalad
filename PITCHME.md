#HSLIDE
#GEO 409:02
##Week 04

#HSLIDE
##Attribute Joins
##& choropleth maps


#HSLIDE
##Topics
* Quantity mapping: choropleth maps
* Perform an attribute join in SQL
* Edit tables and add custom coordinate systems
* In class: world population density choropleth map
* Lab: Fayette County population density map


#HSLIDE
##Your task:
#Lesson 02
on Canvas and <a href="https://uk.instructure.com/courses/1884348/pages/lesson-02-on-github?module_item_id=23086873" target="_blank">GitHub</a>

#HSLIDE?image=images/04/hay.jpg<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Look right?</h2>

#HSLIDE?image=images/04/wheat.jpg<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">More area more production</h2>

#HSLIDE
##Choropleth map
* Combine tables using shared field values
* Fields contain unique identifiers
	* Postal ID, geoid, your student ID...
* Used to map tables without geometry

#HSLIDE
##Attribute Join
* Combine tables using shared field values
* Fields contain unique identifiers
	* Postal ID, geoid, your student ID...
* Used to map tables without geometry

#HSLIDE
##(inner) join
* Combine tables using shared field values
* Fields contain unique identifiers
	* Postal ID, geoid, your student ID...
* Used to map tables without geometry


#HSLIDE?image=https://c1.staticflickr.com/3/2436/3532938292_6e091a7e9f_o.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Think Summertime</h2>

#HSLIDE?image=https://c1.staticflickr.com/9/8598/28904721335_5b9734c8dc_o.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">In Lex</h2>

#HSLIDE?image=https://c1.staticflickr.com/9/8532/29426262562_02449660b1_o.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">On the trail</h2>

#HSLIDE
##Note
###I renumbered assignments
The first lab and module is now "00"

#HSLIDE
###Our goal in class this week
##is to make a map

#HSLIDE?image=https://c1.staticflickr.com/1/550/32506050195_34e2b75f64_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Kentucky waterways map</h2>
<a href="https://www.flickr.com/photos/28640579@N02/32506050195/in/dateposted-public/" target="_blank">example map</a>

#HSLIDE
###First step
#read lesson
##:)

#HSLIDE
###Today, let's
##download data
from Canvas module 01

#HSLIDE
###Build a spatial database
##in QGIS

#HSLIDE
###Then execute some 
##SQL Queries
find a list of statements on Canvas

#HSLIDE
###There is  
##video too
woohoo

#HSLIDE
###Open code editor  
##save your SQL

#HSLIDE
###Use your Geo409 repo
##sync
your work between home and class

#HSLIDE
##Lab 01
Due this Sunday by end of day.

#HSLIDE?image=http://cdn.fansided.com/wp-content/uploads/usat-images/2017/01/9845065-ncaa-basketball-kansas-at-kentucky.jpeg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Don't worry about basketball!</h2>

#HSLIDE
##Lab 01
###Requirements
Two maps and a measurement


#HSLIDE?image=https://c1.staticflickr.com/1/550/32506050195_34e2b75f64_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Map in class (70%)</h2>

#HSLIDE?image=images/03/minimum-map.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">a minimal second map (20%)</h2>

#HSLIDE?image=images/03/minimum-map.png
<h4 style="color:#eee;text-shadow: 2px 2px 4px #000;">Town Branch's length is</h4>
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">3.8 miles (10%)</h2>


#HSLIDE?image=https://c1.staticflickr.com/1/779/32407852142_a94ecb9fad_h.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Lab challenge (+20%)</h2>
<a href="https://www.flickr.com/photos/28640579@N02/32407852142/in/dateposted-public/" target="_blank">example map</a>

#HSLIDE?image=images/03/nhd-hydro.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Lab data</h2>
* <h4 style="color:#eee;text-shadow: 2px 2px 4px #000;">stream flowline</h4>
* <h4 style="color:#eee;text-shadow: 2px 2px 4px #000;">large stream areas</h4>
* <h4 style="color:#eee;text-shadow: 2px 2px 4px #000;">waterbodies</h4>


#HSLIDE
###Download more from
##The National Map
<a href="https://viewer.nationalmap.gov/basic/" target="_blank">Raster and vector data download</a>

