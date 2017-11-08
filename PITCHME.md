#HSLIDE
# Lesson 6
### Weeks 10-12

#HSLIDE
# NRE 355
## Geospatial applications


#HSLIDE
# Elevation analysis
* Terrain modeling
* 3D visualization
* Tree canopy height (sweet!)


#HSLIDE
# DEM
### Digital Elevation Model
* Raster data model with elevation as cell value
* Surface model of bare earth (no structures or trees)
* [More info](http://desktop.arcgis.com/en/arcmap/latest/analyze/commonly-used-tools/surface-creation-and-analysis.htm)

#HSLIDE?image=https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Srtm_ramp2.world.21600x10800.jpg/1280px-Srtm_ramp2.world.21600x10800.jpg

#HSLIDE
## Ky DEM data sources
[ftp://ftp.kymartian.ky.gov/kyaped/DEMs_5FT/](ftp://ftp.kymartian.ky.gov/kyaped/DEMs_5FT/)
* Also available via ArcGIS Server @kyraster.ky.gov
* 5-foot spatial resolution
* 32-bit floating point raster (.IMG format)
* State not completely covered

#HSLIDE
## Who makes the data?
* KYAPED
* Kentucky's Aerial Photography & Elevation Data program
* Consortium of partners to contract data creation
* [Kentucky From Above](http://kygeonet.ky.gov/kyfromabove/)

#HSLIDE?image=images/terrain-analysis/010_northcampus.jpg
## North campus & Kentucky River example data

#HSLIDE
## DEM derivatives
### Analysis to derive surface properties from DEM

#HSLIDE
## Enable ArcGIS Extentions
* 3D Analyst
* Spatial Analyst

#HSLIDE
# Hillshade
* Illuminate surface to create shaded relief
* Sun source: azimuth and elevation
* Outputs 8-bit raster
* Compare cast shadows or not...

#HSLIDE?image=images/terrain-analysis/011.jpg

#HSLIDE?image=images/terrain-analysis/012.jpg

#HSLIDE?image=images/terrain-analysis/013.jpg

#HSLIDE
# Contour
* Create elevation contours, isolines of height
* Should know z units
* Outputs to vector layer
* Might need to smooth raster (Focal Statistics)

#HSLIDE?image=images/terrain-analysis/014.jpg

#HSLIDE?image=images/terrain-analysis/015.jpg

#HSLIDE
# Slope
* Steepest downhill change in height
* Outputs 32-bit floating point raster


#HSLIDE?image=images/terrain-analysis/016.jpg

#HSLIDE
# Aspect
* Direction slope faces
* Outputs 32-bit floating point raster

#HSLIDE?image=images/terrain-analysis/017.jpg

#HSLIDE
## 3D Analyst toolbar
* Interpolate elevations from surface
* Draw elevation profiles and 3D views
* Export 3D features to ArcScene

#HSLIDE?image=images/terrain-analysis/0171.jpg


#HSLIDE
# Lidar
### Light detection and ranging
* Active sensor transmits pulses of light
* Sensor records time of return
* First return top (building/tree top), last return bottom (bare earth)
* Lidar point cloud of XYZ positions
* [More info](http://desktop.arcgis.com/en/arcmap/10.4/manage-data/las-dataset/what-is-lidar-data-.htm)

#HSLIDE?image=images/01/lidar-00.jpg
#HSLIDE?image=images/01/lidar-01.jpg



#HSLIDE
## KY lidar data sources
[ftp://ftp.kymartian.ky.gov/kyaped/LAZ/](ftp://ftp.kymartian.ky.gov/kyaped/LAZ/)
* LASer (LAS) is common public GIS format
* LAZ is a zipped LAS file
* Create ArcGIS LAS dataset (LASD) by merging LAZ files

#HSLIDE
## LAS Dataset toolbar
* Filter points (ground vs. all returns)
* Draw profiles and 3D views

#HSLIDE?image=images/terrain-analysis/018.jpg


#HSLIDE
## LAS Dataset to Raster
* Creates a raster using elevation
* Filter returns for desired surface, i.e., ground vs. tops

#HSLIDE?image=images/terrain-analysis/019.jpg

#HSLIDE?image=images/terrain-analysis/020.jpg


#HSLIDE?image=images/terrain-analysis/021.jpg
<h2 style="color: white; text-shadow: 2px 2px 4px #000000;">Bare earth</h2>

#HSLIDE?image=images/terrain-analysis/022.jpg
<h2 style="color: white; text-shadow: 2px 2px 4px #000000;">Tops</h2>

#HSLIDE
## LAS Point Statistics as Raster
* Find range of elevation values between first and last returns

#HSLIDE?image=images/terrain-analysis/023.jpg


#HSLIDE?image=images/terrain-analysis/024.jpg

#HSLIDE
# Whoa Trees!

#HSLIDE
## Zone Statistics as Table
* Find height of building footprints (a.k.a. the zone)
* Filter returns for desired surface, i.e., ground vs. tops
* Each zone must have unique fields

#HSLIDE?image=images/terrain-analysis/025.jpg

#HSLIDE
## Attribute join table
* Join resulting table to building footprints
* Export to new feature class layer
* View in ArcScene

#HSLIDE?image=images/terrain-analysis/026.jpg

#HSLIDE?image=images/terrain-analysis/027.jpg

#HSLIDE?image=images/terrain-analysis/028.jpg

#HSLIDE
# Lab 4
### Campus example


#HSLIDE
## Lab 4 steps
1. Create NDVI raster for Campus using *Raster Calculator*
2. Create *LAS Point Statistics as Raster*
3. Create areas where NDVI > 0.? and elevation > ? ft using *Raster Calculator*
4. Create final raster layer with *Raster Calculator*


#HSLIDE
## Step 1
# NDVI

#HSLIDE
## *Raster Calculator* query
```
Float("Campus_north_NAIP_2016_2FT - Band_4" - "Campus_north_NAIP_2016_2FT - Band_1") / Float("Campus_north_NAIP_2016_2FT - Band_4" + "Campus_north_NAIP_2016_2FT - Band_1")
```

#HSLIDE?image=images/terrain-analysis/029.jpg

#HSLIDE?image=images/terrain-analysis/030.jpg
<h2 style="color: white; text-shadow: 2px 2px 4px #000000;">Vegetation</h2>

#HSLIDE
## Step 2
# Elevation Range

#HSLIDE?image=images/terrain-analysis/031.jpg

#HSLIDE?image=images/terrain-analysis/032.jpg
<h2 style="color: white; text-shadow: 2px 2px 4px #000000;">Z Range</h2>

#HSLIDE
## Step 3
# Elevation + Vegetation

#HSLIDE
## *Raster Calculator* query
```
("North_campus_ELEV_range">5)  & ("NDVI_2016" > 0.1)
```

#HSLIDE?image=images/terrain-analysis/033.jpg

#HSLIDE?image=images/terrain-analysis/034.jpg
<h2 style="color: white; text-shadow: 2px 2px 4px #000000;">Trees!</h2>

#HSLIDE?image=images/terrain-analysis/035.jpg

#HSLIDE
## Step 4
# Get Z of trees

#HSLIDE
## *Raster Calculator* query
```
Pick("Trees_5ft_NDVI_1",["North_campus_ELEV_range"])
```

#HSLIDE?image=images/terrain-analysis/036.jpg

#HSLIDE?image=images/terrain-analysis/037.jpg

#HSLIDE
# Errors?
* Check if tall buildings are getting captured. Should be small amount.
* Did we get all trees? Let's geocode UK's tree study and see!
* Might need to tweak parameters. Let's do it!

#HSLIDE
# The future
## Let's talk about it.

#HSLIDE
# Calendar
* 6 more classes
* Nov 15 is GIS Day and a UFI presentation
* One field day to possibly scan a tree

#HSLIDE
# Final Projects
## Who has a specific project?

#HSLIDE
## how about a
# Group project?

#HSLIDE
## Neighborhood Tree Canopy study
* Neighborhood teams produce content
* Web team publishes content and I nominate [Renato](http://sweb.uky.edu/~rvi234/nre355/)
* Spend more time in [CARTO](https://www.carto.com)
* Submit group website and maps to the bigwigs
