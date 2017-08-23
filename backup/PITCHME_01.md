#HSLIDE
#Welcome!

#HSLIDE
#GEO 409:01
##Advanced topics in GIS

#HSLIDE
###Instructor
##Boyd Shearer
Contact information in syllabus

#HSLIDE
What experiences help me teach
###GIS & Cartography?


#HSLIDE?image=images/01/map-cuga.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">I make maps</h2>
<a href="https://outrageGIS.com" target="_blank">outrageGIS.com</a>

#HSLIDE?image=https://c1.staticflickr.com/1/390/31713088315_f0326f577c_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">I photograph</h2>

#HSLIDE?image=https://c1.staticflickr.com/6/5324/30627102241_3cde14d218_o.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">I walk a lot</h2>

#HSLIDE?image=https://c1.staticflickr.com/6/5555/25390145339_41f3abb792_h.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">I'm a recent new dad</h2>

#HSLIDE?image=https://c1.staticflickr.com/1/585/31458905453_5db120e84d_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">I like to experiment</h2>
<a href="https://kuula.co/post/7ft7S" target="_blank">(with 3D maps)</a>

#HSLIDE?image=https://c1.staticflickr.com/6/5697/31017969892_6a6f41ec25_o.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">I like field trips to see sunsets</h2>

#HSLIDE
##How about you?
* What is your name?
* Major?
* What cartography/GIS courses have you taken?

#HSLIDE
###How have I taught GEO 409 in the past?

#HSLIDE
Create a theme:
##Analyzing
#Walkability

#HSLIDE?image=images/01/map-create-zones.jpg
<h2 style="color:#111;text-shadow: 2px 2px 4px #fff;">Divide city into zones.</h2>

#HSLIDE?image=images/01/map-digitize-paths.jpg
<h2 style="color:#111;text-shadow: 2px 2px 4px #fff;">Digitize walking paths.</h2>

#HSLIDE
###Build a network model
connecting paths to streets with sidewalks. 

#HSLIDE
![Pedshed](images/01/map-pedshed.jpg)   
Create a pedshed to measure how many people can access what parts of town on foot.

#HSLIDE?image=https://geography.as.uky.edu/sites/default/files/GEO409_2014_FinalProject_Preview.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Where are the "cow paths" on campus?</h3>
<h4 style="color:#eee;text-shadow: 2px 2px 4px #000;">Are they quicker than sidewalks?</h4>

#HSLIDE
##Let's make web maps!

#HSLIDE?image=http://boydx.github.io/collisions/images/VineStreet_LexingtonKentucky.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Bike/Pedestrian vs. Car Collision Analysis</h3>
<a href="http://boydx.github.io/collisions/" target="_blank">Bring in CARTO!</a>

#HSLIDE
**Publishing maps online needs a web page (and host)**
* Student web server @ sweb.uky.edu (slow but free)
* GitHub Pages (comes with version control and syncing!)

#HSLIDE
##We will publish maps using GitHub Pages

#HSLIDE
##What tools will we use?

#HSLIDE
###More open source!
* Students have requested it
* QGIS is robust, free, and runs on a mac OS
* We'll still use ArcGIS (You'll get a year license)

#HSLIDE
###More code!
* Text-based instructions are cool, dude
* ESC the desktop, free your workflow
* SQL, shell scripts, Python


#HSLIDE
#EXAMPLES?


#HSLIDE
```sql
/* Select Kentucky from polygon layer of states. */

SELECT * FROM
    state_polygon_layer
WHERE
    state_name = 'Kentucky'
    
/* That's it! */

```
#HSLIDE

###Chunk of code, recipe, gist, etc.
* Avoid the click click desktop
* Execute on remote servers (with terrabites of memory)
* Write it once, use it forever


#HSLIDE?image=https://c1.staticflickr.com/6/5713/31179013342_da99860b71_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">How acres have burned per county?</h2>

#HSLIDE
###Spatial Join
intersect and summarize    
<a href="http://boydx.github.io/wildfires/" target="_blank">1992-2013 analysis</a>

#HSLIDE

```sql
/* Sum wildfire acres by county polygon */

SELECT 
    sum(pts.fire_size) as fire_acres,
    round((sum(pts.fire_size) / (poly.aland * 0.000247105)*100)::numeric,2) as percent_burned, 
    poly.name, 
    poly.geoid, 
    poly.aland, 
    poly.geom 
from 
    poly 
join 
    pts on ST_Intersects(pts.geom, poly.geom) 
group by 
    poly.name,
    poly.geoid,
    poly.aland,
    poly.geom

/* That's it! */
```

#HSLIDE
###We'll do overaly analysis
Using SQL on spatial databases (SpatiaLite and PostGIS)


#HSLIDE
###We want more 3D!
LiDAR data now available for Lexington

#HSLIDE?image=images/01/lidar-00.jpg
#HSLIDE?image=images/01/lidar-01.jpg
#HSLIDE?image=images/01/lidar-02.jpg

#HSLIDE?image=https://c1.staticflickr.com/1/710/31150476630_13ead32b58_k.jpg  
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">I like to get high</h3>
<p style="color:#eee;text-shadow: 2px 2px 4px #000;">and photograph</p>

#HSLIDE
###Walking the urban core   
<a href="https://www.flickr.com/photos/28640579@N02/31150476630/in/dateposted-public/" target="_blank">in spherical photos.</a>


#HSLIDE
![Connected interior spaces](https://c1.staticflickr.com/9/8062/29138854162_1cd274d646_o.jpg)

#HSLIDE
LiDAR tools in ArcGIS help create an   
<a href="https://www.outragegis.com/trails/2016/08/27/elevation-profile-of-connected-interior-spaces" target="_blank">elevation profile of connected interior spaces</a>



#HSLIDE?image=https://c1.staticflickr.com/9/8560/29239711024_0a23da2985_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Sunrise in Lexington</h2>

#HSLIDE?image=images/01/map-sunrise.jpg

#HSLIDE
###LiDAR can help accurately model scenic areas
Which areas of town can see a sunrise with respect to buildings, trees, etc.    
<a href="https://www.flickr.com/photos/28640579@N02/29239711024/in/album-72157668647475382/" title="Can you see the fall sunrise in Lexington, Kentucky?">Full map</a>

#HSLIDE
###We now arrive at a
##Theme


#HSLIDE
Spring 2017 course theme:
##Town Branch Trail & Commons
![Video](https://www.youtube.com/embed/OR4JaAmA9rk)
<a href="http://www.townbranch.org/" target="_blank">townbranch.org</a>

#HSLIDE?image=http://www.townbranch.org/info/wp-content/uploads/2013/05/TBT_news2.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">One mile already exists</h2>

#HSLIDE?image=http://www.townbranch.org/info/wp-content/uploads/2016/11/TownBranchTiger.png

#HSLIDE?image=http://www.townbranch.org/info/wp-content/uploads/2016/11/WaterFeature-1024x771.jpg

#HSLIDE?image=http://www.kentucky.com/latest-news/38c860/picture43889769/ALTERNATES/FREE_960/ADAd5.So.79.jpeg

#HSLIDE?image=http://www.townbranch.org/doc/TBT_at_NCR_2014.jpg

#HSLIDE
##Mapping Town Branch
* What is the current condition of the corridor?
* Canopy, water, built environment, walking paths, etc.
* How might the corridor look after trail is built?


#HSLIDE
##What couyld go wrong?
#HSLIDE?image=images/01/texas-v-alaska.jpg


#HSLIDE
##Challenge for you
What are the areas of Texas and Alaska?