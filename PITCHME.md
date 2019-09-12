---?image=https://maptimelex.github.io/monochromatic-maps/images/example-0.png&opacity=40
## Monochromatic maps
# maptimeLEX

---?image=https://maptimelex.github.io/monochromatic-maps/images/hillshade-01.jpg&opacity=40
## Monochrome?
@ul[squares]
* Grayscale
* 1-bit color is one color
* Convert grayscale to single-hue gradient?
@ulend

---?image=https://maptimelex.github.io/monochromatic-maps/images/convert-to-monochrome.gif&opacity=40
## Easy

---?image=https://somethingaboutmaps.files.wordpress.com/2019/08/ah.jpg&opacity=40
## Inspiration
### Daniel Huffman's [Monocarto 2019](https://somethingaboutmaps.wordpress.com/monocarto-2019-winners)

---?image=https://maptimelex.github.io/monochromatic-maps/images/example-0.png&opacity=40
## Challenge
@ul[squares]
* Make hillshade effect with one color
* Use only QGIS
* Make it cool
@ulend


---?image=https://maptimelex.github.io/monochromatic-maps/images/example-0.png&opacity=40
## Why?
@ul[squares]
* One-color is reproducible on the greatest variety of media (think swag!)
* They are lighter weight in file size compared to their multi-hue siblings
* Images can take on a historic/hand-drawn patina, which ups the [spatial oomph index](https://maptimelex.github.io/monochromatic-maps/spatialoomph.mp3)
* "business in the front, party in the back, baby"
@ulend

---?image=https://maptimelex.github.io/monochromatic-maps/images/crosshatch-map.jpg&opacity=40
## Technique
@ul[squares]
* Crosshatch shading
* Old technique used by Erwin Raisz, Albrecht Dürer, et al.
@ulend

---?image=https://maptimelex.github.io/monochromatic-maps/images/example-0.png&opacity=40
## Tool flow
@ul[squares]
* Create hillshade
* Select shades
* Convert to polygons
* Apply rotating crosshatch symbols to polygons
* [Download data](https://maptimelex.github.io/monochromatic-maps/QGIS-project-and-data.zip) and [follow instructions](https://maptimelex.github.io/monochromatic-maps)
@ulend

---?image=https://maptimelex.github.io/monochromatic-maps/images/example-0.png&opacity=40
## Find macOS and Windows script in download

---
```bash
# Input DEM
input='../DEM_40m.tif'
# Resample DEM
resolution='1000'
# Z factor to increase relief in hillshade
z='14'
# Digital number from hillshade
DN='5 30 100'
# Ouput directory for polygonized hillshade
output=relief$resolution$z
# Goodbye!
rm e*.tif
gdalwarp -tr $resolution $resolution -r near -of GTiff $input eDEM.tif
gdaldem hillshade eDEM.tif eHillshade-$z.tif -of GTiff -b 1 -z $z -s 1.0 -az 315.0 -alt 45.0
mkdir $output
for value in $DN; do
    gdal_calc.py -A eHillshade-$z.tif --outfile=eRelief-$value.tif --calc="A <= $value"
    gdal_polygonize.py eRelief-$value.tif relief-$value.gpkg -b 1 -f "GPKG" relief-$value DN
    ogr2ogr -f GPKG $output/relief-$value.gpkg -where "DN = 1" relief-$value.gpkg
    rm relief-$value.gpkg
done
```
@[1-12]
@[13]
@[14]
@[15]
@[16-21]


---?image=https://maptimelex.github.io/monochromatic-maps/images/example-0.png&opacity=40
<iframe src="https://maptimelex.github.io/monochromatic-maps/map/" height="500" width="100%"></frame>
[enlarge](https://maptimelex.github.io/monochromatic-maps/map/)

---?image=https://maptimelex.github.io/monochromatic-maps/images/example-0.png&opacity=40
# Thank you!

