#HSLIDE
# Lesson 1

#HSLIDE
# NRE 355
## Geospatial applications

#HSLIDE
# GIS
## Geographic Information Systems

#HSLIDE
## Classic definition
A multidisciplinary system of hardware, software, data, people, organizations, and institutional arrangements for collecting, storing, analyzing, and disseminating information about areas of the earth.

#HSLIDE
## We'll add
GIS: The activity of spatial measurement and visualization of hazards and assets in our environment.

#HSLIDE
## Maps
### The story of place?

#HSLIDE
## Place
### The space where we live
We'll parse place into a series of themed, overlapping layers.


#HSLIDE

<img src="https://www.jmu.edu/_images/facmgt/gis-layers-graphic.jpg" height="600px">

#HSLIDE
## Model
an abstraction of real-world phenomena and processes.


#HSLIDE?image=https://farm5.staticflickr.com/4429/36033302333_267b460188_h.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Duncan Park Centennial</h2>

#HSLIDE
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3141.78852090571!2d-84.48936984567271!3d38.0520137106569!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x884244fb16bc0c15%3A0x543114380232ce17!2sDuncan+Park%2C+Lexington%2C+KY+40508!5e0!3m2!1sen!2sus!4v1503845223217" width="800" height="600" frameborder="0" style="border:0" allowfullscreen></iframe>

#HSLIDE?image=https://farm5.staticflickr.com/4387/36033305973_97c9d43dc8_h.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">New tree</h2>


#HSLIDE?image=https://i2.wp.com/www.outragegis.com/trails/wp-content/uploads/2014/12/NeighborhoodGreenIndex_MLKNA.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Green index</h2>
<a href="https://www.outragegis.com/trails/2014/11/04/neighborhood-green-index/" target="_blank">map</a>

#HSLIDE
## GIS
### digitize
### organize
### analyze
### visualize


#HSLIDE
## Spatial data model
the rules/constructs for how we represent features on earth in our GIS.



#HSLIDE?image=http://www.esri.com/~/media/Images/Content/about-esri/about/graphics/timeline/1986.jpg 
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">1986</h3>

#HSLIDE

## ARC/INFO

Early version of ArcGIS in which the name hints at the nature of spatial data model.

* **ARC** is an array of coordinates giving locations.
* **INFO** is a table of rows and columns (a database) of attributes.


#HSLIDE
## Tabular data model  

* A table of rows (feature) and columns (attribute)
* Formats include text-based files like a _.csv_ file (comma separated values), spreadsheets, or tables in a geodatabase
* Attributes will have data types, e.g., numeric vs. alphanumeric

#HSLIDE?image=http://desktop.arcgis.com/en/arcmap/10.4/manage-data/tables/GUID-E9C5D05E-5D42-4078-8E86-57BAD0FD5FC8-web.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">table</h2>
<a href="http://desktop.arcgis.com/en/arcmap/10.4/manage-data/tables/what-are-tables-and-attribute-information.htm" target="_blank">link</a>


#HSLIDE
## Vector data model  

* Array of x,y coordinates (usually hidden from user)
* Contains tabular data where each geographic feature (a row in the table) has columns of attributes
* Formats include the _Shapefile_ and geodatabase _Feature Class_

#HSLIDE
### Vector geometric primitives 

* **Point** - single x,y coordinate value
* **Line** - series of connected coordinate values (vertices) with two end points (nodes)
* **Polygon** - a closed line 
* Great for discrete features (with distinct boundaries), e.g., lakes, trails, and campsites.


#HSLIDE
### Vector topology 

Connectivity and geometric relationships between features that model real-world conditions.

* Trails are connected by intersections
* Lakes are adjacent to land
* Islands are contained within lakes 

#HSLIDE
### Vector layers  

* One layer holds only one geometry type (point, line, or polygon)
* Every feature in a layer is an object with a unique identifier (*OBJECTID* or *FID*)
* Multifeatures (multipoint, multiline, multipolygon) have multiple features but only one record, e.g., how many polygons are Georgia?

#HSLIDE?image=http://desktop.arcgis.com/en/arcmap/10.4/manage-data/geodatabases/GUID-49497935-EDB0-4BCA-8861-8BE08F89AAA9-web.gif
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">vector</h2>
<a href="http://desktop.arcgis.com/en/arcmap/10.4/manage-data/geodatabases/feature-class-basics.htm" target="_blank">link</a>


#HSLIDE
## Raster data model  

* Matric of cells or pixels (picture element)
* **Cell size** determines raster resolution
* * 10 m x 10 m cell size (100 sq m) has 10-meter resolution
* Great for continuous phenomena, like land elevation and reflected sunlight.

#HSLIDE
### Raster cell values  

* A numeric value represent same conditions for the entire cell area
* * Aerial photography (average intensity of reflected sunlight)
* * Land elevation (average height)
* * Land cover (majority landcover type)


#HSLIDE
### Raster formats  

* The _.tif_ TIFF and _.jpg_ JPEG formats are common
* * Need an associated _worldfile_ to spatially reference in our GIS (_.tfw_ and _.jpw_ respectively)
* We will use geodatabase rasters

#HSLIDE?image=http://desktop.arcgis.com/en/arcmap/10.4/manage-data/raster-and-images/GUID-6754AF39-CDE9-4F9D-8C3A-D59D93059BDD-web.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">raster</h2>
<a href="http://desktop.arcgis.com/en/arcmap/10.4/manage-data/raster-and-images/what-is-raster-data.htm" target="_blank">link</a>



#HSLIDE
## A world of numbers  

* Be aware of your units of measure (meters vs. feet)
* Is a number a quantity or a category (height of tree vs. zip code of tree)

#HSLIDE
## Metadata 

* A description or explanation of a dataset
* Often attached as an *.xml* file (extensible markup language), a text-based method of encoding information
* Open file in browser and look for ```<tag>value</tag>```, e.g., ```<author>Kentucky GeoNET</author>```

#HSLIDE
## Summary 

When you get data to use in your GIS ask a few questions first: 

* What data model is it? What geometry type? 
* Does it have attributes? Does it have metadata? 
* What place does the data show? Does it "look right" on screen? 

#HSLIDE
## Our first lab and the geodatabase 

Regardless of the source, format, or data model of your data, you will load this data into a **File Geodatabase**. This is goal of Lab 0.


#HSLIDE
## More 

Find more PDFs about scale, resolution, ArcMap, data sources etc. on Canvas module this week.




