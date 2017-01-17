#HSLIDE
#GEO 409:01
##Advanced topics in GIS

#HSLIDE
##Topics
* Tools for the knowledge worker
* Challenge: calculate areas of Texas and Alaska

#HSLIDE
##To do
#Lesson 01


#HSLIDE
###Tools for the
##Knowledge Worker

#HSLIDE
Need to
##manage text

#HSLIDE
Particularly code
##text-based instructions

#HSLIDE
What are some code
##languages?

#HSLIDE
Structured Query Language
##SQL
pronounced "sequel" & perhaps most used language to manage data

#HSLIDE
##GIS is
#Big Data

#HSLIDE
Hypertext Markup Language
##HTML
The code that tells your browser how to display a web page

#HSLIDE
(Carto) Cascading Style Sheets 
##CSS and CartoCSS
Used with HTML to render pretty web pages

#HSLIDE
Start tinkering with examples
##[w3schools.com](http://www.w3schools.com/)

#HSLIDE
##What is in our
#Future?

#HSLIDE
We'll use a framework to start a web page
##[Get Skeleton](http://getskeleton.com/)

#HSLIDE
Command-line processing using GDAL/OGR
###OSGeo4W shell or Mac OS terminal
E.g., command -input -output -parameters

#HSLIDE
Develop scripts to automate GIS workflow
##(Python)[http://interactivepython.org/courselib/static/thinkcspy/index.html]
Most-used programming language in GIS

#HSLIDE
Tools to
##manage text

#HSLIDE
A good code editor
##Language syntax highlighting
auto-complete, find and replace, code folding

#HSLIDE
We'll use 
##Brackets
but install others like [Atom](https://atom.io/) and [Sublime](https://www.sublimetext.com)




#HSLIDE?image=images/02/markdown.md.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Many ways to create</h2>
<a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet" target="_blank">Markdown.md</a>



#HSLIDE
Manage projects to
##Prevent loss of text
and support collaboration

#HSLIDE
![Git](images/02/git.png)   
[xctd](http://xkcd.com/)


#HSLIDE  
[Git](https://git-scm.com/) was created by Linus Torvalds in 2005 for development of the Linux kernel, with other kernel developers contributing to its initial development.



#HSLIDE
We'll use the git hosting service [GitHub.com](https://github.com/) and their GitHub desktop app to manage our projects.

#HSLIDE
###Our GitHub flow
* Clone remote repository   
  (or create new local repo)
* Edit files and save
* Commit and sync

#HSLIDE
###GitHub Pages 
Use GitHub to publish web pages, including 
###Map Portfolio!

#HSLIDE
###GitHub.io
* Create repo named    
    ```<github-username>.github.io```    
    must be a public repo
* Create a ```docs``` folder inside private repo

#HSLIDE?image=images/02/github-settings.jpg





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