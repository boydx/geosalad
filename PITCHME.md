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
### Raster Calculator
```sh
("Band_4" - "Band_1")/("Band_1" + "Band_4")
```

#HSLIDE?image=images/ndvi/q03.jpg

#HSLIDE?image=images/ndvi/q04.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">NDVI</h3>

#HSLIDE?image=images/ndvi/q05.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Trees @ >0.3?</h3>

#HSLIDE
## Selective transparency
### to create canopy layer

#HSLIDE?image=images/ndvi/q06.jpg

#HSLIDE?image=images/ndvi/q07.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Trees @ >0.4?</h3>

#HSLIDE
## Benefits of greenness?
* What? Besides O<sup>2</sup>, keeping our cities cool, and general support of earth's ecosystem?

#HSLIDE?image=images/ndvi/q08.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Cart layer</h3>

<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;"><a href="http://boydx.github.io/tbt/xyz/canopy/leaflet.html" target="blank">Web map layer</a></h2>

#HSLIDE
## Measurement of canopy cover
```sh
#!/bin/bash

# Script uses GDAL library (2.2) and Python (2.7) to create an NDVI raster and calculate area of treee canopy.
# Assumes an NDVI value od 0.3 for canopy cover.

# echo "Clipping NDVI raster to campus boundary"
gdalwarp -cutline campus_wis.shp -crop_to_cutline -overwrite -ot Float32 naip_2013_uw-m.tif uw-m_campus.tif
gdalwarp -cutline campus_ky.shp -crop_to_cutline -overwrite -ot Float32 naip_2014_uky.tif uky_campus.tif

# Process georeferenced TIFF rasters in current folder
list=`ls -t *.tif`


# Loop through array to perform analysis
for i in $list
		do
		echo "creating NIR band from" $i
		gdal_calc.py \
			-A $i --A_band=4 \
			--outfile=nir.tif \
			--overwrite \
			--calc="A" --type='Float32'

		echo "Creating NDVI from" $i
		gdal_calc.py \
			-A $i --A_band=1 \
			-B nir.tif --B_band=1 \
			--outfile=ndvi.tif \
			--overwrite \
			--calc="((B-A)/(B+A))"


		echo "Calculating acres of tree canopy and percent of total area in" $i
		python count.py

		# remove temporary rasters
		rm -f nir.tif ndvi.tif

done
```

```Python

#!/usr/bin/env python2.7

# GDAL library 2.2 installed with QGIS 3.0 on Ubuntu 16.04.
# gdalnumeric library might not read nodata values on other platforms.

import gdalnumeric

### Define variables ###

# input NDVI from GDAL output
r_file = gdalnumeric.LoadFile("ndvi.tif")

# NDVI value for assumed tree canopy. This is a gross approximation that's just for fun.
canopy = 0.3

### Count pixels ###

# Where pixel value > canopy variable count the number of pixels
count = ((r_file >= canopy) & (r_file <= 1)).sum()

# count total pixels in area of interest
countA = ((r_file >= -1) & (r_file <= 1)).sum()

### Calculate area ###

# Each pixel is 10.76 sq ft in area. Convert to acres
acres = (count*10.76)/43560
acresA = (countA*10.76)/43560

# Percent canopy
percent = (count/float((countA)))*100

### Print results ###

# Give me the acreage and ratio
print str(round(acres,1)) + " ac " + str(round(acresA,1)) + " ac " + str(round(percent,1)) + "%  "
```
