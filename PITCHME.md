#HSLIDE
#Welcome!

#HSLIDE
#GEO 409:01
##Advanced topics in GIS

#HSLIDE
##Instructor
#Boyd Shearer
Contact information in syllabus

#HSLIDE
What experiences help me teach
###GIS (& Cartography)?

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

#HSLIDE
##How about you?
* What is your name?
* Major?
* What cartography/GIS courses have you taken?

#HSLIDE
##How have I taught GEO 409 in the past?

#HSLIDE
Create a theme:
##Analyzing
#Walkability

#HSLIDE?image=images/01/map-create-zones.jpg
<h2 style="color:#111;text-shadow: 2px 2px 4px #fff;">Divide the city into zones.</h2>

#HSLIDE?image=images/01/map-digitize-paths.jpg
<h2 style="color:#111;text-shadow: 2px 2px 4px #fff;">Digitize the walking paths.</h2>

#HSLIDE
#Build a network model
###connecting the paths with streets with sidewalks. 

#HSLIDE
![Pedshed](images/01/map-pedshed.jpg)   
Create a pedshed to measure how many people can access what parts of town on foot.

#HSLIDE?image=https://geography.as.uky.edu/sites/default/files/GEO409_2014_FinalProject_Preview.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Where are the "cow paths" on campus?</h2>
<h4 style="color:#eee;text-shadow: 2px 2px 4px #000;">Are they quicker than sidewalks?</h4>

#HSLIDE
#Let's make Web Maps!

#HSLIDE?image=http://boydx.github.io/collisions/images/VineStreet_LexingtonKentucky.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Bike/Pedestrian vs. Car Collision Analysis</h3>



#HSLIDE
###Course theme
##Town Branch Trail & Commons
![Video](https://www.youtube.com/embed/OR4JaAmA9rk)
<a href="http://www.townbranch.org/" target="_blank">townbranch.org</a>







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

```sql
/* Select Kentucky from polygon layer of states. */

SELECT * FROM
    state_polygon_layer
WHERE
    state_name = 'Kentucky'
    
/* That's it! */

```

#HSLIDE
**Topics**
* Worm sleeping patterns
* tonic water harvesting methods
* windchime repair


#HSLIDE
LiDAR tools in ArcGIS help create an   
<a href="https://www.outragegis.com/trails/2016/08/27/elevation-profile-of-connected-interior-spaces" target="_blank">elevation profile of connected interior spaces(</a>
#HSLIDE?image=images/01/lidar-00.jpg
#HSLIDE?image=images/01/lidar-01.jpg
#HSLIDE?image=images/01/lidar-02.jpg
#HSLIDE?image=https://c1.staticflickr.com/9/8062/29138854162_1cd274d646_o.jpg

#HSLIDE
![Connected interior spaces](https://c1.staticflickr.com/9/8062/29138854162_1cd274d646_o.jpg)



#HSLIDE?image=https://c1.staticflickr.com/1/710/31150476630_13ead32b58_k.jpg   
#HSLIDE
Walking the urban core   
[:beer:](https://www.flickr.com/photos/28640579@N02/31150476630/in/dateposted-public/)


#HSLIDE?image=https://c1.staticflickr.com/6/5713/31179013342_da99860b71_k.jpg

#HSLIDE?image=images/01/texas-v-alaska.jpg

#HSLIDE?image=https://c1.staticflickr.com/9/8560/29239711024_0a23da2985_k.jpg

#HSLIDE
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/28640579@N02/29239711024/in/album-72157668647475382/" title="Can you see the fall sunrise in Lexington, Kentucky?"><img src="https://c1.staticflickr.com/9/8560/29239711024_0a23da2985_k.jpg" width="2048" height="1792" alt="Can you see the fall sunrise in Lexington, Kentucky?"></a>