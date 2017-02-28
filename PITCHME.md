#HSLIDE
#GEO 409:04
##Week 06

#HSLIDE?image=https://c1.staticflickr.com/4/3908/32359209443_9a016da7d6_k.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Birthday!</h2>

#HSLIDE
##Help for lab 03
###If you weren't here last week...

#HSLIDE?image=images/06/join.jpg

#HSLIDE
##OpenStreetMap and Geoprocessing

#HSLIDE
##OpenStreetMap
####Crowd-sourced map of local knowledge that users can freely harvest.

#HSLIDE?image=images/06/OSM.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="http://www.openstreetmap.org/note/704210#map=11/38.0492/-84.5000&layers=N" target="_blank">OSM</a></h2>
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Greatest mapping project of all time</h3>

#HSLIDE
##Geoprocessing
####A tool (function, algorithm) and workflow to manipulate spatial data in a GIS.

#HSLIDE
##Workflow
####input data > function parameters > output data (output becomes input for another function)



#HSLIDE
#Geoprocessing


#HSLIDE
##Bread 'n Butter GIS
###How much of X is near Y?

#HSLIDE
##How many people
###live within a half-mile of Town Branch Trail?


#HSLIDE?image=http://media.graytvinc.com/images/810*455/estill+forest+fire.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Wildfire in Kentucky</h2>


#HSLIDE?image=https://c1.staticflickr.com/1/752/32464606700_d84d79ce9b_h.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="https://www.flickr.com/photos/28640579@N02/32464606700/in/photostream/" target="_blank">how much is here?</a></h3>

#HSLIDE?image=https://c1.staticflickr.com/4/3855/32692041102_1f92661f70_h.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="https://www.flickr.com/photos/28640579@N02/32692041102/in/photostream/" target="_blank">how much is here?</a></h3>

#HSLIDE
#Spatial join
###how much of x is in y?

#HSLIDE?image=https://c1.staticflickr.com/1/496/31340122270_488c594cad_k.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">How many trees are in the watershed?</h3>

#HSLIDE?image=https://c1.staticflickr.com/1/496/31340122270_488c594cad_k.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">What is the average diameter?</h3>

#HSLIDE
##Point in polygon analysis 

* Aggregate by polygon and count number
* Perform summary statistics on numeric attributes
* "many to one" join

#HSLIDE
##Hexagonal grids

* Tessellation; create a grid of same polygon
* Area is same, so already normalized
* Count by hexagon


#HSLIDE
##Intersect test

* st_intersects() function
* Tests two geometries for overlap
* Exact fit but slow

#HSLIDE
##Spatial Index Query

```
select * from layer_a 
join layer_b    
on st_intersects(layer_a.geom, layer_b.geom)
group by layer_a.id --or geoid, county_name, etc.
```



#HSLIDE
##Spatial index

* Create hidden tables spatially index layers storing:
	* Minimum bounding rectangle for feature and its ID
* Each feature ID is related all other intersecting IDs in database
* Loose fit but fast

#HSLIDE
##Spatial index query

```
select * from layer_a, layer_b    
where layer_b.rowid in
	(select rowid from SpatialIndex         
	where f_table_name = 'layer_b'
	and search_frame = layer_a.geom)
```

#HSLIDE
##Heat Map

* Hot spot map
* Density surface raster
* Distance from each point weighted by curve

#HSLIDE?image=images/05/Curves.png

	
#HSLIDE
##Raster Data model
* Array of cell values (always a number!)
* Types of rasters
	* Continuous, e.g., elevation
	* Integer, landuse
	* Imaging, photograph



#HSLIDE?image=https://c1.staticflickr.com/3/2832/32813689775_27afa15b82_h.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Town Branch</h2>


#HSLIDE
#Lab 03
###Springs of Kentucky & Fayette County


#HSLIDE?image=images/05/L03-1.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Create new database</h3>

#HSLIDE?image=images/05/L03-2.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Create new project with EPSG: 3089</h3>

#HSLIDE?image=images/05/L03-3.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Import layers in correct SRID</h3>

#HSLIDE?image=images/05/L03-4.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Symbolize springs</h3>

#HSLIDE?image=images/05/L03-5.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Make hex grid</h3>

#HSLIDE?image=images/05/L03-6.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Add to Map Canvas</h3>


#HSLIDE?image=images/05/L03-7.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Multipart to singlepart tool</h3>

#HSLIDE?image=images/05/L03-8.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Import into database and Create spatial index</h3>

#HSLIDE?image=images/05/L03-9.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Practice spatial join</h3>

#HSLIDE
```
/* Spatial join prings to 5-mile long diagonal hexagon grid */

/* uncomment when ready to insert 

insert into  ky_springs_by_5mi_hexgrid

(average_elev,
average_flow_cfs,
count,
hex_id,
hex_name,
geom)

*/


select
	 avg(dow_groundwater_springs.elevation) as average_elev,
	 avg(dow_groundwater_springs.flowqty) as average_flow_cfs,
	 count(dow_groundwater_springs.id) as count,
	 ky_hexgrid_5mi_diagonal.id,
	 ky_hexgrid_5mi_diagonal.Kentucky_springs_5mi_hexgrid,
	 ky_hexgrid_5mi_diagonal.geom

from
	ky_hexgrid_5mi_diagonal
join
	dow_groundwater_springs
on 
	st_intersects(dow_groundwater_springs.geom, ky_hexgrid_5mi_diagonal.geom)
and
	dow_groundwater_springs.rowid in
	(select dow_groundwater_springs.rowid from SpatialIndex
	where f_table_name = 'dow_groundwater_springs'
	and search_frame = ky_hexgrid_5mi_diagonal.geom)
group by	
	ky_hexgrid_5mi_diagonal.id
	```

#HSLIDE?image=images/05/L03-10.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Create new table</h3>


#HSLIDE?image=images/05/L03-11.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Insert spatial join output</h3>

#HSLIDE?image=images/05/L03-12.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Your output</h3>

#HSLIDE?image=images/05/L03-13.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Symbolized layer</h3>

#HSLIDE?image=images/05/L03-14.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Use numeric attributes</h3>

#HSLIDE?image=images/05/L03-15.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Challenge: make hex grid for Fayette county</h3>




#HSLIDE?image=images/05/L03-18.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Challenge: spatial join springs to hex grid</h3>



#HSLIDE?image=images/05/L03-19.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Challenge: spatial join springs to census polygons</h3>


#HSLIDE?image=images/05/L03-20.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Create heatmap raster</h3>

#HSLIDE?image=images/05/L03-21.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Style properties for grayscale raster</h3>

#HSLIDE?image=images/05/L03-22.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Pseudocolor singleband raster with transparency</h3>

#HSLIDE?image=images/05/L03-23.png
<h3 style="color:#ffac68;text-shadow: 2px 2px 4px #000;">Final style properties for heatmap</h3>



#HSLIDE?image=https://c1.staticflickr.com/3/2261/32077384194_cd27ccf612_k.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="https://www.flickr.com/photos/28640579@N02/32077384194/in/dateposted-public/" target="_blank">Example map</a></h3>