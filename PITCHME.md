---
# GEO 409:07
### 3D and terrain analysis using lidar data in Kentucky

---
## Prereq
Make sure you have finished the presentation from [Module 06](https://gitpitch.com/boydx/geosalad/g409-06a) and watch the videos on Canvas for this module.

---
## News!
If you've scaled the Python mountain, you will have a big payoff in this module.

---
## Goals
In the next month we will:
@ul
* Create two maps
    * Cliffs over 30-feet
    * Interactive map of your landform
* Create an animation of your landform
@ulend

---
# [360](https://kuula.co/post/7Y4wL)
Pick your landform today!

---
## This module
@ul
* Cliffs over 30-feet in height
* Video animation
* All in ArcGIS!
@ulend
---
@css[title-top-right](Flying to Grays Arch)
![Gravity](https://www.youtube.com/embed/E8EJapOwvAc)

---
![Fly to Grays Arch](https://www.youtube.com/embed/RB7x9B6OBkI)


---
## Lidar: review
@ul
* active sensor
* multiple returns with attributes
* creates a point cloud
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
## Practice
Downloading, extracting, and displaying lidar data.
* [Tutorial](https://gitpitch.com/boydx/geosalad/g409-06a)
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
## Vidoes
* https://youtu.be/zREAEdXzOcw, https://youtu.be/EYbhNSUnIdU