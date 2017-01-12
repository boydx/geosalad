#HSLIDE
#Welcome!

#HSLIDE
#GEO 409:01
##Advanced topics in GIS

#HSLIDE
#Instructor
##Boyd Shearer
Contact information in syllabus


#HSLIDE


#Course theme
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



#HSLIDE?image=images/01/lidar-00.jpg
#HSLIDE?image=images/01/lidar-01.jpg
#HSLIDE?image=images/01/lidar-03.jpg
#HSLIDE?image=https://c1.staticflickr.com/9/8062/29138854162_1cd274d646_o.jpg
#HSLIDE
LiDAR tools in ArcGIS help create an   
<a href="https://www.outragegis.com/trails/2016/08/27/elevation-profile-of-connected-interior-spaces" target="_blank">elevation profile of connected interior spaces(</a>


#HSLIDE?image=https://c1.staticflickr.com/1/710/31150476630_13ead32b58_k.jpg   
#HSLIDE
Walking the urban core   
[:beer:](https://www.flickr.com/photos/28640579@N02/31150476630/in/dateposted-public/)


#HSLIDE?image=https://c1.staticflickr.com/6/5713/31179013342_da99860b71_k.jpg

#HSLIDE?image=images/01/texas-v-alaska.jpg

#HSLIDE?image=https://c1.staticflickr.com/9/8560/29239711024_0a23da2985_k.jpg

#HSLIDE
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/28640579@N02/29239711024/in/album-72157668647475382/" title="Can you see the fall sunrise in Lexington, Kentucky?"><img src="https://c1.staticflickr.com/9/8560/29239711024_0a23da2985_k.jpg" width="2048" height="1792" alt="Can you see the fall sunrise in Lexington, Kentucky?"></a>