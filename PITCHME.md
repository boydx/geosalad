---?image=images/geo_depart.png&size=50%&opacity=100

---?image=https://www.outragegis.com/weather/img/animation/yesterday/LookRock.gif&opacity=100
# GEO 409:07
### 3D and terrain analysis using lidar data

---
## Announcements
### April 21, 2020
(Check Canvas announcements)

---
## Cash Awards!
@ul
* If you are Geo major (or mapping minor)...
* Send me your (any) map by noon tomorrow to enter competition.
@ulend

---
## Update!
@ul
* Fixed problem with ArcGIS Pro 2.5...
* and Virtual Den.
* Download and use [new scripts](https://outragegis.com/d/UpdatedNotebooks_Geo409_Lidar.zip)
@ulend

---
## Prereq
@ul
* Finished the presentation about [about accessing and extracting lidar data](https://gitpitch.com/boydx/geosalad/g409-07c)
* Watch the videos on Canvas for this module
@ulend

---
## Good news!
@ul
* We're using Python again! 🎉🥳
* We can do a lot of repetitive work with Python.
* Leave more time for the fun stuff 🎥🎬
@ulend

---
## Goals
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

---?image=https://live.staticflickr.com/1913/44871763315_6228d74f85_k.jpg&size=contain&opacity=100

---
<!-- @css[title-top-right](Visiting Mammoth Cave's Historic Entrace) -->
![Gravity](https://www.youtube.com/embed/BVVCe_BSsT4)

---
![Hike up to Indian Arch](https://www.youtube.com/embed/nFV8ftGN0aM)

---
<iframe src="https://www.outrageGIS.com/pointclouds/johnson" width="100%" height="600px"></iframe>


---
## Lidar
@ul
* light detection and ranging
* Uses laser light to densely sample the surface of the earth to make highly accurate x,y,z measurements.
@ulend

---
## Lidar properties
@ul
* Active sensor records reflections of rapidly pulsing laser
* Multiple returns with attributes
* Platform: airborne vs. terrestrial
* Creates a point cloud of massively sampled locations
@ulend


---?image=http://ucanr.org/blogs/Green/blogfiles/10250.png&size=contain&opacity=100

---
## Point cloud attributes
@ul
* x, y, z position
* time
* intensity of return
* Custom algorithms classify point as ground, water, noise, above-ground features
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

---?image=images/quantum_lidar.jpg&size=contain&opacity=100

---
## Kentucky project
@ul
* Collected during leaf-off conditions
    * no snow
    * water levels at or below normal.
* Point cloud has 2.23-foot point horizontal spacing.
* Access data in 5k ft x 5k ft tiles ~100-600 MB each
@ulend


---
## Goal
@ul
* Create high-resolution elevation products for bare-earth conditions. 
* Model accurate hydrological conditions
* Create a seamless statewide Digital Elevation Model with a 5-ft resolution
@ulend

---
## Classification
@ul
* Algorithms classify point
* Need to filter for ground points
* All (non-noise) points give us height of above-ground features like trees, buildings, etc.
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
* Heads-up digitizing to enforce hydrological rules
    * Remove bridges, flatten lakes and wide rivers (lidar can record waves)
* Field measurements to verify accuracy
    * Most measurements within .2 ft
@ulend

---?image=images/cp_dz.png&size=contain&opacity=100

---?image=images/quantum_qc.jpg&size=contain&opacity=100

---?image=images/lidar-progress.png
## Future of lidar collection [KyFromAbove](http://kyfromabove.ky.gov/)

---
## Practice
Downloading, extracting, and displaying lidar data.
* [Tutorial](https://gitpitch.com/boydx/geosalad/g409-07c)
* [Video](https://uk.instructure.com/courses/1931541/pages/video-arcgis-pro-and-lidar?module_item_id=23767003)


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
## Tools used
@ul
* [LAS dataset to raster](https://pro.arcgis.com/en/pro-app/tool-reference/conversion/las-dataset-to-raster.htm)
* [LAS point statistics as raster](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/las-point-statistics-as-raster.htm)
* [Focal Statistics](https://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/focal-statistics.htm)
* NOTE: filtering a point cloud in ArcGIS Pro will control contributing points to output
@ulend

---
# Visualization

---
## Potree converter
@ul
* Point cloud renderer (fast!)
* Open source [potree.org/](http://potree.org/)
* Uses WebGL
* Upload to your repo
@ulend

---
## Videos
* https://youtu.be/zREAEdXzOcw, https://youtu.be/EYbhNSUnIdU