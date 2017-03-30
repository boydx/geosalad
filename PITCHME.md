#HSLIDE
#GEO 409:04
##Week 06 - 08

#HSLIDE?image=https://c1.staticflickr.com/4/3908/32359209443_9a016da7d6_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Birthday!</h2>

#HSLIDE
##Help for lab 03
###If you weren't here last week...

#HSLIDE?image=images/06/join.jpg

#HSLIDE
##OpenStreetMap and Geoprocessing

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


#HSLIDE
##Geoprocessing
####A tool, function, or algorithm used to manipulate data in a GIS.


#HSLIDE
##Bread 'n Butter GIS
###How much of X is near Y?


#HSLIDE
##Workflow
###Chain of tools
####input data > tool parameters > output data (output becomes input for another tool)


#HSLIDE
##Flavors of geoprocessing
* QGIS tools vs. SpatiaLite functions
* Though they might appear wildly different, they are in fact based on the same processing library: GEOS (Geometry Engine Open Source)

#HSLIDE
##Common tools
* Most often produce new data
	* What happens to the new geometry?
	* What happens to the attributes?
* [Common QGIS tools](https://github.com/boydx/geo409_s17/blob/master/module-04/module-04.2.md#common-geoprocessing-tools-in-qgis)
* Compare clip, interest, union, and dissolve


#HSLIDE
##Common mistake: you can fry your attributes!
* Geometry measurements need to be recalculated after clip, intersect, etc.
* Any measurement fields, e.g., population, need to be carefully inspected to determine if they are still accurate, e.g., after a union



#HSLIDE
##Practice Lab 4.2: geoprocessing workflow
* How many people live within one mile of a completed Town Branch Trail?
* Explore how to solve with QGIS tools and SpatiaLite SQL
* Use QML files to style base map

#HSLIDE?image=https://c1.staticflickr.com/4/3832/32646236973_8176af1e3c_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="https://www.flickr.com/photos/28640579@N02/32646236973/in/dateposted-public/" target="_blank">Example map</a></h2>

#HSLIDE
##Final lab
###How many people live within <h2>3/4 mile</h2> of Town Branch Trail?

#HSLIDE
##Tool-based approach
* Buffer
* Clip (or Intersect)
* Recalculate


#HSLIDE
##SQL Approach
* [SQL Statements](https://gist.github.com/boydx/eee1577dabb185baa89e6dc34ebf3ff0)


#HSLIDE
##SQL Approach
```
/* Find population within one mile of a completed Town Branch Trail */
/* We'll add semicolon to indicate the end of a statement. Not needed in DB Manager, but standard in command line environments. */

/* Remove table if it already exists. */ 

drop table 
	tbt_buffer_1mile;
    
/********************************** Step 1 **********************************/

/* Add new table with an autoincrementing primary key called 'id' */

create table tbt_buffer_1mile
	(
	id integer not null primary key autoincrement
	);

/********************************** Step 2 **********************************/

/* Add empty geometry column */

select 
	AddGeometryColumn('tbt_buffer_1mile', 'geom', 3089, 'multipolygon', 'xy');
    
    
/********************************** Step 3 **********************************/

/* Create buffer, cast to a multipart feature, and insert into table */
/* The st_collect() function creates a single part, the CastToMulti() function ensures that we'll match the multipolygon geom type */

insert into tbt_buffer_1mile 
		(geom)
select 
	CastToMulti(st_buffer(st_collect(geom),5280)) as geom
from 
	planned_tbt;
    
    
/********************************** Step 4 **********************************/

/* Clip the census blocks with town branch trail buffer and calculate area of blocks */

select
	st_intersection(tbt_buffer_1mile.geom,census_blocks_pop_2010.geom) as geom,
	census_blocks_pop_2010.pop10,
	st_area(census_blocks_pop_2010.geom)
	
from
	census_blocks_pop_2010, tbt_buffer_1mile
where 
	st_intersection(tbt_buffer_1mile.geom,census_blocks_pop_2010.geom) is not null;
    


/********************************** Step 5 **********************************/

/* Create table to receive clip of census blocks with town branch trail buffer and calculate area of blocks */

create table tbt_pop
(
	id integer not null primary key autoincrement,
	pop real,
	area_feet real,
	derived_pop real
);


/********************************** Step 6 **********************************/

/* Add empty geometry column */

select AddGeometryColumn('tbt_pop', 'geom', 3089, 'multipolygon', 'xy'); 


/********************************** Step 7 **********************************/

/* Insert the clip of census blocks with town branch trail buffer and calculate area of blocks */

insert into tbt_pop

(
	geom,
	pop,
	area_feet
)

select
	CastToMulti(st_intersection(tbt_buffer_1mile.geom,census_blocks_pop_2010.geom)) as geom,
	census_blocks_pop_2010.pop10,
	st_area(census_blocks_pop_2010.geom)
	
from
	census_blocks_pop_2010, tbt_buffer_1mile
where 
	st_intersection(tbt_buffer_1mile.geom,census_blocks_pop_2010.geom) is not null;
    
    

/********************************** Step 8 **********************************/

/* Calculate column with ratio of populaiton in census block */

update 
	tbt_pop 
set
	derived_pop = pop*(st_area(geom)/area_feet);
    
    
/********************************** Step 9 **********************************/

/* Create summary table with populaiton estimates */

select 
	sum(pop) as total,
	sum(derived_pop) as derived
from 
	tbt_pop;
```



