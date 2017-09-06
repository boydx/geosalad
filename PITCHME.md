#HSLIDE
# Lesson 2
### Week 3

#HSLIDE
# NRE 355
## Geospatial applications

#HSLIDE
# All maps lie

#HSLIDE
# All maps are distortions


#HSLIDE?image=https://farm5.staticflickr.com/4435/36900423222_2799e7cb97_h.jpg

#HSLIDE
# CRS
## Coordinate Reference Systems

#HSLIDE
## As map makers
### It's our job to pick the right one.


#HSLIDE
## EPSG: 3089
This is the primary CRS that we will use in class.

#HSLIDE
## Anatomy of a CRS
* Framework for defining real-world locations:
* Unit of measure, e.g., feet
* A origin: (0,0)

#HSLIDE
## Geodesy
### The study of the shape of earth, which is not a perfect sphere.


#HSLIDE
## Geographic Coordinate Systems (GCS)
* Define the shape of the sphere-like earth
* angular unit of measure
* spheroid and datum

#HSLIDE
## GCS graticule
* grid on a sphere
* latitude, aka parallels
* longitude, aka meridians

#HSLIDE?image=https://www.kidsdiscover.com/wp-content/uploads/2013/09/Latitude_Longitude_2.jpg

#HSLIDE
## Common GCS
NAD83 for North America = GCS NAD83
WGS84 for world datasets = GCS WGS84


#HSLIDE
## Find
Lexington's GCS coordinates

#HSLIDE
## Projected Coordinate Systems (PCS)
* Shows earth on plane with grid
* linear unit of measure
* contains a GCS

#HSLIDE
## PCS use map projection
A systematic method of transforming points of latitude and longitude (geographic coordinates) onto a plane with grid coordinates.

#HSLIDE
### Projections can generally preserve shape and area, but not both simultaneously.

#HSLIDE
### Projections are tuned to the areas they cover to minimize distortion.

#HSLIDE
## Conformal Projections
* Preserve the shape of features
* distorts area
* used for navigation

#HSLIDE?image=https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Tissot_indicatrix_world_map_Mercator_proj.svg/2000px-Tissot_indicatrix_world_map_Mercator_proj.svg.png

#HSLIDE
## Equal Area Projections
* Preserve the area of features
* distorts shape
* used for thematic world maps 

#HSLIDE?image=https://upload.wikimedia.org/wikipedia/commons/3/30/Tissot_indicatrix_world_map_Winkel_Tripel_proj.svg

#HSLIDE
## Compromise Projections
* Preserve neither area nor shape
* A good compromise
* used for thematic world maps  

#HSLIDE?image=http://gis.osu.edu/img/projections.png

#HSLIDE
## Interrupted Projections
* Preserve the area and shape of features
* distorts direction
* used for uber cool 

#HSLIDE?image=https://hexnet.org/files/images/hexnet/dymaxion-map.png

#HSLIDE?image=http://www.lynceans.org/wp-content/uploads/2016/12/Cahill-Keyes.jpg

#HSLIDE?image=https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Tissot_indicatrix_world_map_equirectangular_proj.svg/2000px-Tissot_indicatrix_world_map_equirectangular_proj.svg.png
