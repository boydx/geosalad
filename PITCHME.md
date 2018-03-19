#HSLIDE
## Raster Analysis
# NDVI
### QGIS 3

#HSLIDE?image=https://farm8.staticflickr.com/7355/13891770272_6cd7624525_o.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Let's leave the icy chill</h3>

#HSLIDE?image="https://farm5.staticflickr.com/4240/35679659782_93a8f94195_o.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">and welcome spring.</h3>

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

#HSLIDE
#### The process of photosynthesis has a distinct
## spectral signature

#HSLIDE?image=images/ndvi/q02.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">CIR</h3>

#HSLIDE
## Map Algebra
### with the Raster Calculator
```sh
("Band_4" - "Band_1")/("Band_1" + "Band_4")
```

#HSLIDE?image=images/ndvi/q03.jpg

#HSLIDE?image=images/ndvi/q04.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">NDVI</h3>

#HSLIDE
## Let's find
# Trees!

#HSLIDE?image=images/ndvi/q05.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Trees @ >0.3?</h3>

#HSLIDE
## Selective transparency
### to create tree canopy layer

#HSLIDE?image=images/ndvi/q06.jpg

#HSLIDE?image=images/ndvi/q07.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Trees @ >0.4?</h3>

#HSLIDE
## Benefits of greenness?
* What? Besides keeping our cities cool and providing the foundation for the ecosystem we call Earth?

#HSLIDE?image=images/ndvi/q08.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Canopy layer</h3>

#HSLIDE
<iframe src="https://boydx.github.io/tbt/xyz/canopy/leaflet.html" height="600px" width="100%"></iframe>

#HSLIDE?image=https://farm5.staticflickr.com/4283/35706563651_ed72b792ce_k.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Where to hang a tree swing!</h3>

#HSLIDE
# Lab
## Measure tree canopy
### UW-Madison's campus

#HSLIDE?image=images/ndvi/q09.jpg
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">GeoData@Wisconsin</h3>
`OWNERNAME like 'UNIV OF WIS%'`

#HSLIDE
## Script it!
```sh
#!/bin/bash

# Script uses GDAL library (2.2) and Python (2.7) to create an NDVI raster and calculate area of tree canopy.
# Assumes an NDVI value of 0.4 for canopy cover.

# echo "Clipping NDVI raster to campus boundary"
gdalwarp -cutline campus_wis.shp -crop_to_cutline -overwrite -ot Float32 naip_2013_uw-m.tif uw-m_campus.tif
#gdalwarp -cutline campus_ky.shp -crop_to_cutline -overwrite -ot Float32 naip_2014_uky.tif uky_campus.tif

# Process georeferenced TIFF rasters in current folder
list=`ls -t *uw*.tif`


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

#HSLIDE
## Measure canopy

```python
#!/usr/bin/env python2.7

# GDAL library 2.2 installed with QGIS 3.0 on Ubuntu 16.04.
# gdalnumeric library might not read nodata values on other platforms.

import gdalnumeric

### Define variables ###

# input NDVI from GDAL output
r_file = gdalnumeric.LoadFile("ndvi.tif")

# NDVI value for assumed tree canopy. This is an approximation.
canopy = 0.4

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

#HSLIDE
## Estimates ☘️
| Campus   | Acres   | Canopy  | NDVI Value | NAIP Year |
| -------------: |-------------:| -----:| -----:| -----:|
| UW-M       | 1,187 | 27.5% | 0.40 | 2013 |
| UKY      | 931 ac    |   14.3% | 0.24 | 2014 |

#HSLIDE
<iframe src="https://player.vimeo.com/video/260685194" width="100%" height="480" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
