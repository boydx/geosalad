#HSLIDE
# Lesson 4
### Week 5

#HSLIDE
# NRE 355
## Geospatial applications

#HSLIDE
# Raster data
### matrix of cell values

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
## NASA MODIS Worldview
### Near real-time views of Earth in multiple wavelengths of light.
<br><a href="https://worldview.earthdata.nasa.gov" target="_blank">link</a>

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
### ArcMap > ArcToolbox > Spatial Analyst tools > Map Algebra > Raster Calculator

```
"Ky_DEM_5ft" >= 1070
```

#HSLIDE?image=images/raster-data/06.png

#HSLIDE?image=images/raster-data/07.png


#HSLIDE
## Image Analysis window

### ArcMap > Windows > Image Analysis


#HSLIDE?image=images/raster-data/08.png




#HSLIDE
.