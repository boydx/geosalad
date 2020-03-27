------?image=https://www.outragegis.com/weather/img/animation/yesterday/LookRock.gif&opacity=40
# GEO 409
## Module 06: 
### Cartography (and Field mapping)

---?image=https://live.staticflickr.com/4345/35932585353_86b4720238_k.jpg&opacity=40
<h2 style="text-shadow:0 0 2px #333, 0 0 5px #333;color:white">Take a walk in the woods</h2>


---
## Spring 2020
@ul[squares]
* Field Trip!
* Plan your own trip
* Make your own map
* Measure your space
@ulend


---?image=https://live.staticflickr.com/7786/27482504770_267470cc1f_o.jpg&opacity=40
## Adopt a landform

---?image=https://live.staticflickr.com/8185/29282811394_acffec2f45_o.jpg&opacity=40
## or a building, skyline, etc.

---?image=https://farm2.staticflickr.com/1922/43128933340_d6d61a6bb2_h.jpg&opacity=40
## Explore a big space

---
## Example
### Red River Gorge

---
# Step 1

---
## Make RRG base map
@ul[squares]
* Layers should include arches
* streams, waterbodies, rivers
* labeled streams and arches
* a hillshade background with semi-transparent landuse layer
* Export as GeoPDF
@ulend

---?image=https://farm1.staticflickr.com/930/42790171395_a745af0f06_h.jpg&opacity=100

---
## Use map in the field
### on phone with no cell data?
# 🤯

---?image=images/avenza-1.jpg&opacity=100

---
# Step 2

---
## Publish map
@ul[squares]
* Create new repo on Github.com
* Enable Github pages 
* Add `boydx` as a collaborator
* Clone down new repo, add map, commit, and push
* Find URL to map, e.g. https://username.github.io/rrg/basemap/rrg-arches.pdf
@ulend


---
# Step 3

---
### Load app
# Avenza Maps 
#### on your mobile device.
[avenzamaps.com](https://avenzamaps.com)

---
## Load campus map 
### with QR code
![images/get-map.png](images/get-map.png)

---?image=images/get-map.png&opacity=100&&size=auto 90%



---
## Load RRG base map
@ul[squares]
* Use your RRG repository
* Upload PDF and find URL
* https://username.github.io/rrg/basemap/rrg.pdf
@ulend

---
## Example map

---?image=images/rrg.jpg&opacity=100&&size=auto 90%

---?image=images/a17.jpg&opacity=100&&size=auto 95%

---?image=https://farm2.staticflickr.com/1959/43128931410_daceab6096_h.jpg&opacity=100

---
# Step 4

---
## Visit site
@ul[squares]
* Photograph
* Measure
* Drop pin
@ulend

---
@quote[I took a walk in the woods and came out taller than the trees](Henry David Thoreau)



---
# Addendum
## Making base map in ArcGIS Pro

---
## Add clipped layers
@ul[squares]
* Adjust Land cover layer
    * transparency and 
    * lightness
    * try to show hillshade beneath
@ulend

---?image=images/a00.jpg&opacity=100&&size=auto 95%

---
## Edit arch layer
@ul[squares]
* Change default symbol
* Label with FEATURE_NAME field
* Make symbol stand out against background
@ulend

---?image=images/a01.jpg&opacity=100&&size=auto 95%

---
## Edit arch layer
@ul[squares]
* Add halo
* Use color that is similar to background
@ulend

---?image=images/a02.jpg&opacity=100&&size=auto 95%

---
## Insert > New Layout
@ul[squares]
* Select a size roughly 20" x 20"
* Target scale for map is between 1:30k and 1:40k
@ulend

---?image=images/a03.jpg&opacity=100&&size=auto 95%

---
## Insert > Map Frame
@ul[squares]
* Add Map
* Tip: use Spatial Bookmarks for exact view
@ulend

---?image=images/a04.jpg&opacity=100&&size=auto 95%

---
## Edit map frame
@ul[squares]
* Right-click the map frame to **Activate**
* Pan and zoom your map to fit frame
* Exit map frame when finished
@ulend

---?image=images/a05.jpg&opacity=100&&size=auto 95%

---
## Check scale in Map Layout
@ul[squares]
* Use lower-left settings to check
    1. scale of map
    2. text is easily read at 400%
@ulend

---?image=images/a06.jpg&opacity=100&&size=auto 95%

---
## Label streams
@ul[squares]
* Right-click the layer for **Label Properties**
* Create Python expression to replace "Branch" with "Br"
@ulend

---
## Expression
```python
[GNIS_NAME].replace("Branch", " Br")
```

---?image=images/a07.jpg&opacity=100&&size=auto 95%

---
## Label streams
@ul[squares]
* Increase **Word Spacing** to add space between words
@ulend

---?image=images/a08.jpg&opacity=100&&size=auto 95%

---
## Navigate layout
@ul[squares]
* Use **Navigate tools** to move around page
* Use **Select tools** to select/edit map elements
@ulend

---?image=images/a09.jpg&opacity=100&&size=auto 95%

---
## Label streams
@ul[squares]
* Use Position > Offset curved
* Explore/edit other properties
@ulend

---?image=images/a10.jpg&opacity=100&&size=auto 95%

---
## Label streams
@ul[squares]
* Add halo
* Use transparency
@ulend

---?image=images/a11.jpg&opacity=100&&size=auto 95%

---
## Insert map elements
@ul[squares]
* Use **Rectangle** text tool
* Add title, author, etc.
@ulend

---?image=images/a12.jpg&opacity=100&&size=auto 95%

---
## Insert map elements
@ul[squares]
* Use **Picture** tool
* Add image of land cover legend
* Link: [Download image](https://www.mrlc.gov/sites/default/files/NLCD_Colour_Classification_Update.jpg)
@ulend

---?image=images/a13.jpg&opacity=100&&size=auto 95%

---
## Insert map elements
@ul[squares]
* Use **Scale Bar** tool
* Add other elements as desired...
@ulend

---
## Bonus technique
@ul[squares]
* Add **Legend** tool
* *Break* legend into component parts
* Use graphic design methods to balance layout
@ulend

---?image=images/a14.jpg&opacity=100&&size=auto 95%

---
## Edit custom legend
@ul[squares]
* **Covert To Graphics**
* Unlinks legend and makes it editable
* Can be fun!
@ulend

---?image=images/a15.jpg&opacity=100&&size=auto 95%

---
## Edit map elements
@ul[squares]
* Right-click element
* Use **Group**, **Ungroup**, and **Align** tools for layout/design
@ulend

---?image=images/a16.jpg&opacity=100&&size=auto 95%

---
## Example
@ul[squares]
* Finished map?
* Add photos, logos, etc.
* Tweak colors, transparency, etc.
* Maps are never done!
@ulend

---?image=images/a17.jpg&opacity=100&&size=auto 95%

---
## Need a map?
@ul[squares]
* if you can't get a map finished by field trip
* add this URL to your Avenza Map app
* https://tastyfreeze.github.io/rrg/basemap/rrg.pdf
@ulend
