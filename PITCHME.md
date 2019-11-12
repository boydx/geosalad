---?image=images/geo_depart.png&size=50%

---
# GEO 409:07
### 3D and terrain analysis using lidar data in Kentucky

---
## Prereq
@ul
* Finished the presentation about [about accessing and extracting lidar data](https://gitpitch.com/boydx/geosalad/g409-07c)
* Watch the videos on Canvas for this module
@ulend

---
## News!
@ul
* If you've scaled the Python mountain, you will have a big payoff in this module.
* Check out the addendum and Jupyter Notebook
@ulend

---?image=https://uky-gis.github.io/gisday/assets/images/splash.png&size=contain

---?image=https://maptimelex.github.io/wildcat-eyes/assets/images/wildcat-eyes-logo.jpg&size=contain

---
## Goals
Over the final month:
@ul
* Create two maps
    * Cliffs over 30-feet
    * Interactive map of your location
* Create an animation of your location
* Publish this to your GitHub Repo, e.g., *boydsGIS.github.io/rrg*
@ulend

---
## This module
@ul
* Surface modeling
    * ground height
    * above-ground height
* Video animation
* Point cloud rendering
@ulend

---
# Examples

---?image=https://live.staticflickr.com/1913/44871763315_6228d74f85_k.jpg&size=contain

---
<!-- @css[title-top-right](Flying to Grays Arch) -->
![Gravity](https://www.youtube.com/embed/E8EJapOwvAc)

---
![Hike up to Indian Arch](https://www.youtube.com/embed/nFV8ftGN0aM)

---
<iframe src="https://www.outrageGIS.com/pointclouds/johnson" width="100%" height="600px"></iframe>


---
# [360](https://kuula.co/post/7lpQt)
Start thinking about what you want to map!

---
(light detection and ranging)
## Lidar
@ul
* active sensor
* multiple returns with attributes
* creates a point cloud (massively sampled locations)
* airborne vs. terrestrial
@ulend

---?image=http://ucanr.org/blogs/Green/blogfiles/10250.png&size=contain&opacity=100

---
## Point cloud attributes
@ul
* x, y, z position
* time
* intensity of return
* Custom algorithms classify point
@ulend

---
## Airborne lidar
@ul
* Massive sampling of earth's surface by plane
* While can penetrate canopy, cannot 'see' under solid structures.
* i.e., cannot see under our arches.
@ulend

---?image=images/quantum_airplanes.jpg&size=contain
## Quantum Spatial fleet

---?image=images/quantum_lidar.jpg&size=contain

---
## Kentucky project
@ul
* Collected during leaf-off conditions
    * no snow
    * water levels at or below normal.
* Point cloud has 2.23-foot point horizontal spacing.
* Access data in 5k ft x 5k ft tiles ~500 MB each
@ulend


---
## Goal
Create high-resolution elevation products for bare-earth conditions. A statewide 5-ft resolution DEM is now available.

---
## Classification
@ul
* Algorithms classify point
* Need to filter for ground points
* All (non-noise) points give us tree height
@ulend


---
| KY classes | Meaning|
|-------------|-----------:|
|1 |Processed, but Unassigned (above ground features) |
|2 |Bare-earth or ground|
|7 |Noise (e.g., birds. Can be low or high, manually identified, if needed)|
|9 |Water|
|10 |Ignored Ground (Breakline Proximity)|

---
## QC/QA
@ul
* Heads-up digitizing to enforce hydro rule
    * Classify bridges and noise
* Field measurements to verify accuracy
    * Most measurements within .2 ft
@ulend

---?image=images/cp_dz.png&size=contain

---?image=images/quantum_qc.jpg&size=contain

---?image=images/lidar-progress.png
## Future of lidar collection [KyFromAbove](http://kyfromabove.ky.gov/)

---
## Practice
Downloading, extracting, and displaying lidar data.
* [Tutorial](https://gitpitch.com/boydx/geosalad/g409-07c)
* [Video](https://uk.instructure.com/courses/1931541/pages/video-arcgis-pro-and-lidar?module_item_id=23767003)

---
# STOP

--- 
# Point cloud derivatives

---
Airborne point clouds can be reduced to high-resolution raster imagery.

---
## DEM
@ul
* Digital Elevation Model
* Most often bare-earth surface
@ulend

---
## DSM
@ul
* Digital Surface Model
* Includes the reflected surface
    * buildings, trees, bridges, etc.
@ulend

---
## DTM
@ul
* Digital Terrain Model
* bare-earth surface 
* with vector features to model surface features
    * lines for streams, polygons for lakes, etc.
@ulend



---
## Vidoes
* https://youtu.be/zREAEdXzOcw, https://youtu.be/EYbhNSUnIdU