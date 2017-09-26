#HSLIDE
# Lesson 4
### Week 5-6

#HSLIDE
# NRE 355
## Geospatial applications

#HSLIDE
# Raster data
### matrix of cell values

#HSLIDE
## More info in Canvas
RasterAnalysis_I_04_Presentation.pdf
RasterAnalysis_II_04_Presentation.pdf

#HSLIDE
## Simple data model
* Cell or pixel (picture element)
* Cell resolution: size on the ground
* Count of cells gives area measurement



#HSLIDE
# Cell numbers!
### Correctly interpreting numbers associated with cell values is crucial.

#HSLIDE
## Cell values
* Values are numeric and represent a magnitude or a type
	* E.g., elevation versus land cover
* Bit depth: 2<sup>n</sup> number of distinct values
* Integer vs. ratio values?




#HSLIDE
## Levels of measurement
### to assign numeric values to real-world things.


#HSLIDE
## Nominal type
* Numbers represent unranked categories, e.g., land cover type
* Avoid symbology that implies preference or order

#HSLIDE?image=images/raster-data/01.png

#HSLIDE
## Ordinal type
* Numbers represent ranked categories, e.g., suitability
* Rank is not magnitude, e.g., 2 is not twice as much as 1

#HSLIDE?image=images/raster-data/02.png

#HSLIDE
## Interval type
* Numbers represent continuous range with arbitrary scale, e.g., temperature
* 20&deg; is not twice as hot as 10&deg;

#HSLIDE?image=images/raster-data/03.png

#HSLIDE
## Ratio type
* Numbers represent continuous range of quantities, e.g., elevation
* 200 feet is twice as high as 100 feet

#HSLIDE?image=images/raster-data/04.png

#HSLIDE
# Raster types

#HSLIDE
## Thematic raster
* aka discrete or integer grids
* Maps difference of type
* 1-bit to 8-bit range of values


#HSLIDE
## Continuous raster
* aka surface or floating-point grids
* Maps difference of magnitude
* 16-bit to 32-bit range of values


#HSLIDE
## Imaging raster
* aka photographs or images
* Maps magnitude of reflected or emitted light
* 8-bit to 32-bit range of values

#HSLIDE
## Multiple band rasters
* Imaging rasters with multiple spectral bands
* Same time and scene, just different wavelengths of light
* Red, green, blue (RGB) of true-color (human-visible) light

#HSLIDE
# Data
## NASA MODIS Worldview
### Near real-time views of Earth in multiple wavelengths of light.
<a href="https://worldview.earthdata.nasa.gov" target="blank">link</a>

#HSLIDE?image=images/raster-data/044.png


#HSLIDE
## Histogram
### Graphical representation showing the frequency distribution of data.

#HSLIDE?image=images/raster-data/05.png

#HSLIDE
## Challenge
### Find the highest elevations inside New Circle

#HSLIDE
## Map Algebra expression
ArcMap > ArcToolbox > Spatial Analyst tools > Map Algebra > Raster Calculator

```
"Ky_DEM_5ft" >= 1070
```

#HSLIDE?image=images/raster-data/06.png

#HSLIDE?image=images/raster-data/07.png


#HSLIDE
## Image Analysis window
ArcMap > Windows > Image Analysis


#HSLIDE?image=images/raster-data/08.png

#HSLIDE
# Data
## USGS Earth Explorer
### Landsat 8 Archive (among other _remote sensing_ imagery)
<br><a href="https://earthexplorer.usgs.gov/" target="blank">link</a>

#HSLIDE?image=images/raster-data/09.png

#HSLIDE
## Landsat 8 imagery
* 16-day repetitive Earth coverage collecting 393 GB per day.
* First satellite in series launched in 1972.
* 30 and 100 meter spatial resolution with <a href="https://landsat.usgs.gov/what-are-band-designations-landsat-satellites" target="blank">11 spectral bands</a> that can be composited for <a href="https://landsat.gsfc.nasa.gov/landsat-8/landsat-8-bands/" target="blank">analysis</a>.

#HSLIDE
## September 10, 2017
### Southern Bluegrass country
<a href="https://www.dropbox.com/s/8nkm0zel1qp2phr/LC08_L1TP_020034_20170910_20170910_01_RT.zip?dl=0" target="blank">Download scene</a>

#HSLIDE
## Composite bands 4,3,2 (RGB)
### Create true color image
ArcMap > ArcToolbox > Data Management tools > Raster > Raster Processing > Composite Bands

#HSLIDE?image=images/raster-data/10.jpg

#HSLIDE?image=images/raster-data/11.jpg

#HSLIDE
## Panchromatic sharpening
Use higher-resolution panchromatic (broad spectrum, aka b/w image) raster (band 8) to sharpen lower-resolution true color image that we just created.

#HSLIDE?image=images/raster-data/12.jpg
## Band 8

#HSLIDE?image=images/raster-data/13.jpg




#HSLIDE
## Challenge
### Find the tree canopy cover percentage and total acreage inside New Circle.

#HSLIDE
## Solution

#HSLIDE
## Area inside New Circle
### Calculate Geometry... for polygon layer.

#HSLIDE?image=images/raster-data/14.jpg

#HSLIDE
## Tree canopy area
### Field Calculate... count of cells by ((3.281<sup>2</sup>)/43560)

#HSLIDE?image=images/raster-data/15.jpg

#HSLIDE
# 28%

#HSLIDE
## How do we get a tree canopy raster, anyhoo?



#HSLIDE
## Remote sensing
### Measuring objects without holding them.
* Airplanes and satellites use sensors to collect light that we cannot see.
* All objects have spectral signatures.
* <a href="https://earthobservatory.nasa.gov/Features/RemoteSensing/" target="blank">Nice tutorial</a>

#HSLIDE?image=http://www.gatorsports.com/wp-content/uploads/2017/09/AP17267044765752.jpg

#HSLIDE?image=http://media.hometeamsonline.com/photos/hockey/UKHOCKEY/31917695863_ae8eaaff2a_o.jpg

#HSLIDE
## Four raster resolutions in remote sensing
* Spatial (size of pixel)
* Spectral (wavelength of light)
* Radiometric (level of sensitivity, aka bit depth)
* Temporal (leaf-on v. leaf-off)


#HSLIDE
## Spectral signature
* Healthy plants highly absorb red light (we can see) and reflect near infrared light (we cannot see).
* Use precise wavelengths to identify healthy vegetation.

#HSLIDE
# NDVI
### Normalized difference vegetation index


#HSLIDE
### NDVI is calculated as a ratio between the red (R) and near infrared (NIR) bands
NDVI = (NIR – R) / (NIR + R)



#HSLIDE
## Map Algebra
* If raster bands are integer data type, we need to convert them to float data type.
```
Float(NIR – R)/Float(NIR + R)
```

#HSLIDE
## NDVI output
* Range from -1 to 1.
* < 0 is not vegetation
* > 0.5 (approx) tree canopy


#HSLIDE
# NDVI
### Higher values, more vegetation. Tree canopy is the highest value (especially jungle canopy).


#HSLIDE
## RGB Composite

#HSLIDE?image=images/raster-data/16.jpg

#HSLIDE
## NDVI

#HSLIDE?image=images/raster-data/17.jpg

#HSLIDE
## What values are canopy?

#HSLIDE?image=images/raster-data/18.jpg



#HSLIDE
.


#HSLIDE

updated: September 25
