#HSLIDE
## Raster Analysis
# NDVI

#HSLIDE
# Let's find trees!

#HSLIDE
## NDVI
* Normalized Difference Vegetation Index
* Index of plant “greenness” or photosynthetic activity

#HSLIDE
## Imagery source
* National Agriculture Imagery Program ([National Agriculture Imagery Program](https://www.fsa.usda.gov/programs-and-services/aerial-photography/imagery-programs/naip-imagery/))
* Color infrared photography (CIR) with 4-Band imagery

#HSLIDE?image=images/ndvi/q01.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">NAIP 2013</h3>

#HSLIDE?image=images/ndvi/q02.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">CIR</h3>

#HSLIDE
## Map Algebra
### Raster Calculator to calculate
```
(Band_4 - Band_1)/(Band_1 + Band_4)
```

#HSLIDE
## Benefits of greenness?
* Normalized Difference Vegetation Index (NDVI)

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
