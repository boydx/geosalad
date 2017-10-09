#HSLIDE
# Lesson 5
### Week 8

#HSLIDE
# NRE 355
## Geospatial applications


#HSLIDE
## Practice midterm!
* How many acres are in neighborhood x?
* How many acres of tree canopy?
* Can you put a map in a layout with the answers to the questions?


#HSLIDE
# GNSS
### global navigation satellite system

#HSLIDE
## More info in Canvas
GPSandDataInputs_05_Presentation.pdf

#HSLIDE
# GPS
## global positioning system
### One constellation among many


#HSLIDE
## Many satellites
<iframe src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Comparison_satellite_navigation_orbits.svg" height="400px" width="90%"></iframe><br>
<a href="https://upload.wikimedia.org/wikipedia/commons/b/b4/Comparison_satellite_navigation_orbits.svg" target="b">link</a>




#HSLIDE
# Time
## is the key to location.


#HSLIDE?image=http://collections.rmg.co.uk/mediaLib/450/media-450724/large.jpg

#HSLIDE
## Finding longitude
* Precise clocks and astronomical charts
* Set clock time to home port and watch the sunrise
* Offset in time is distance from home port
* 15&deg; is one hour. *<a href="https://en.wikipedia.org/wiki/History_of_longitude" target="b">history of longitude</a>*

#HSLIDE?image=http://www.rmg.co.uk/sites/default/files/styles/slider/public/rog/wp-content/uploads/sites/2/2015/03/shep-clock.jpg

#HSLIDE
# GMT
## Greenwich Mean Time
* For Lexington, KY our time is
* -4 hours during Daylight Saving Time (March – Nov), EDST
* -5 hours Eastern Standard Time, EST

#HSLIDE?image=images/raster-data/02.png

#HSLIDE
# GPS
## atomic clocks
* Among the best clocks ever made
* Three-billionths of a second precision
* They continuously synchronize time for cell networks, computers, you.
* *<a href="https://timeandnavigation.si.edu">Si.edu</a>*

#HSLIDE?image=https://timeandnavigation.si.edu/sites/default/files/styles/original/public/multimedia-assets/nasm2013-00223.jpg?itok=X20jTe-H

#HSLIDE?image=https://timeandnavigation.si.edu/sites/default/files/multimedia-assets/500-si_hiw_atomic_clock_fa_flat_revised_7-17_copy.jpg

#HSLIDE
# GPS
## Three segments
1. Space segment with ~32 satellites broadcasts time of day and their position.
2. Ground control updates and maintains integrity of satellites.
3. User segment is your receiver, aka $$$! phone.

#HSLIDE?image=http://www.techinsights.com/design-teardown/content/apple-iphone-7/gps.jpg

#HSLIDE
# Ranging
## Use speed of light to determine distance
```
Distance (range) =  Velocity (speed of light (186,282 mi/s) *  Time (offset in time between sat and receiver)
```

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
