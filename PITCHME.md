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
## Who makes the data?
* KYAPED
* Kentucky's Aerial Photography & Elevation Data program
* Consortium of partners to contract data creation
* [Kentucky From Above](http://kygeonet.ky.gov/kyfromabove/)

#HSLIDE?image=images/terrain-analysis/010_northcampus.jpg

#HSLIDE
## DEM derivatives
### Analysis to derive surface properties from DEM
