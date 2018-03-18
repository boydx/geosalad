#HSLIDE
## Raster Analysis
## NDVI


#HSLIDE
## Raster data model
* Array of regularly spaced cells, aka grid
* Cell values are numbers; quantities or categories?
* Level of data measurement
	* Nominal
	* Ordinal
	* Interval
	* Continuous

#HSLIDE
## Important properties
* Resolution; who detailed is my data?
	* Bit depth is number of values a cell can hold
	* 2<sup>n</sup> values where n = number bits
* Single-band vs. multi-band
* File formats can create data loss

#HSLIDE
## Common rtypes
* Integer, e.g., landuse
	* 1-band, 1-bit or 8-bit format
* Continuous, e.g., elevation
	* 1-band, 32-bit floating point
* Imaging, e.g., satellite photography
	* multi-band, 8-bit or 16-bit

#HSLIDE
## Terrain Analysis
* Relief map showing elevation change
* Hillshade tool to illuminate surface
* Overlay aerial photography with transparency




#HSLIDE
## Terrain Analysis
* Relief map showing elevation change
* Digital Elevation Model provides input
* Hillshade tool calculates illumination surface
* Overlay aerial photography with transparency

#HSLIDE?image=images/07/q09.jpg



#HSLIDE
## NDVI Analysis
* Normalized Difference Vegetation Index (NDVI)
* Color infrared photography (CIR) with 4-BandNAIP imagery
* Use Raster Calculator to calculate (B4 - B1)/(B1 + B4)
* High density of vegetation is good in the city!

#HSLIDE?image=images/07/q23.jpg


#HSLIDE
## Raster tile sets
* Create slippy maps of raster layers
* `gdal2tiles` tool
* Output is folder with collection of raster tiles
* Push to your repo to share with world

#HSLIDE?image=images/07/m05.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="http://boydx.github.io/tbt/xyz/canopy/leaflet.html" target="_blank">Canopy near TBT</a></h2>
