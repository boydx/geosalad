#HSLIDE
# GEO 409:06
## Week 12,13



#HSLIDE
# CARTO

#HSLIDE
## CARTO
* Spatial Database PostgreSQL/PostGIS
* SQL, HTML, CartoCSS
* CARTO's 'Wizard' is Builder


#HSLIDE
## Example of what you'll produce:
### Interactive maps

#HSLIDE
<iframe width="100%" height="520" frameborder="0" src="https://townbranchtrail.carto.com/builder/c67d9536-1952-11e7-b78b-0ee66e2c9693/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>


#HSLIDE?image=images/07/m01.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="http://boydx.github.io/tbt/xyz/hillshade/leaflet.html" target="_blank">Made this in QGIS...</a></h2>

#HSLIDE
## ..now use it in CARTO.

#HSLIDE
<iframe width="100%" height="520" frameborder="0" src="https://townbranchtrail.carto.com/builder/fbef55ce-1957-11e7-8fcd-0e233c30368f/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>



#HSLIDE
##SQL and PostGIS in CARTO
* Very similar to SpatiaLite, just a little different syntax
* 'the_geom' and 'carto_id'
* all_lower_case_no_spaces in column and table names


#HSLIDE
```
update
    tbt_2017
set
	length_feet = round((st_length(the_geom,true)*3.281)::numeric,0)
```

#HSLIDE

```
update
	one_mile_buffer
set
	pop_per_sq_mile = round((derived_pop/(st_area(the_geom, true)/2.59e+6))::numeric,0)

```

#HSLIDE
##Adding custom tile sets to CARTO
```
https://<username>.github.io/<location of tile set>/z}/{x}/{y}.png
/* Example */
http://boydx.github.io/tbt/xyz/hillshade/{z}/{x}/{y}.png
```
