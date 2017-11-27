#HSLIDE
# Lesson 7
### Weeks 15-16

#HSLIDE
# NRE 355
## Geospatial applications


#HSLIDE
# Web mapping
## with CARTO

#HSLIDE
# CARTO
* Open source technology
* Prebuilt basemaps as raster tile sets
* User-generated vector layers
* Access to attributes via user interaction

#HSLIDE
# CRS!
### Uploaded datasets are in EPSG: 4326
## WGS 84

#HSLIDE
## CARTO Builder
* A'Wizard' to build maps from datasets
* Menu driven (and pretty slick)
* Code panels allow finer control

#HSLIDE
## Spatial database
* Query data with SQL - Structured Query Language
* Data stored in PostgreSQL/PostGIS
* [SQL Reference](https://www.w3schools.com/sql/default.asp)

#HSLIDE
## Example query
```sql
select * from tree_canopy_heights where height_field > 50
```

#HSLIDE
## CartoCSS
* Cascading Style Sheets
* Markup language to customize symbology of spatial features
* [CartoCSS Reference](https://carto.com/docs/carto-engine/cartocss/)

#HSLIDE
## Example dashed outline
```css
#layer {
  polygon-fill: #ff23f0;
  polygon-opacity: 0;
}
#layer::outline {
  line-width: 3;
  line-color: #ff23ff;
  line-opacity: 0.6;
  line-dasharray: 12, 6, 2, 6;
  line-cap: round;
}
```

#HSLIDE
## HTML
* Hypertext Markup Language
* The language and structure of web page
* Browsers render content of page to you
* Can be used to customize legends, popups, etc.
* [HTML Reference](https://www.w3schools.com/html/html_intro.asp)

#HSLIDE
## Data Viz
* CARTO known for unique data visualization
* Time-series animations
* Layer blending modes more than ArcMap's single transparency
* Change layer appearance by zoom-level
* <a href="https://boydx.github.io/wildfires/" target="blank">Example maps</a>

#HSLIDE
## Widgets
* Data analysis with custom filters and histograms
* Interactive charts embedded in your map
* <a href="https://carto.com/learn/guides#widgets" target="blank">Widgets Reference</a>


#HSLIDE
## CARTO Resources
* Signup: <a href="https://carto.com/signup?" target="blank">get an account</a>
* Learn the basics at the <a href="https://carto.com/academy/" target="blank">Map Academy</a>
* Dig deeper with < <a href="http://cartodb.github.io/training/" target="blank">training workshops</a>
* Official <a href="https://carto.com/docs/" target="blank">documentation</a>

#HSLIDE
## Lab 6
* Create an interactive map in CARTO
* Interactive tree heights and photographs
* <a href="http://sweb.uky.edu/~blshea1/nre355/tree_canopy/lab-06.html" target="blank">Example map</a>


#HSLIDE
## Input datasets
* The *tree_canopy_heights* layer (as polygon)
* The *neighborhood_boundary* layer (as polygon)
* The *poi_locations* layer (as point)
* The *big_tree_locations* layer (as point)

#HSLIDE
## Tool workflow
* **Copy Raster** to convert heights to integer raster
* **Raster to Polygon** to convert heights to polygon
* **Feature Class To Shapefile** to convert all layers to Shapefiles
* Zip each Shapefile layer and upload to CARTO
