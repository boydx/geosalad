---
# GEO 409:01
## Advanced topics in GIS

---
## Topics
* Tools for the knowledge worker
* Set up our work environment
* Measure area the desktop way
* Challenge: measure area by code

---
## Your task:
# Lesson 01
on Canvas


---
### Tools for the
## Knowledge worker

---
## We need to
# manage text

---
# as code
### a/k/a plain-text instructions
that use *keywords* and *syntax*

---
## For example
```html
<p style="color:blue;">Hello, world!</p>
```
renders to:
<p style="color:blue;">Hello, world!</p>

---
### Advantages of coding
* Work simply
* Work remotely
* Work when you sleep 🌝
* Share exact instructions

---
[Get a job](https://geekprank.com/hacker/)

---
First tool
# Text editor
Not Notepad, Microsoft Word, etc. but a platform to view/edit/create multiple code formats

---
A good text editor offers
### Language syntax highlighting
auto-complete as you type, find and replace, and code folding to hide blocks of text.

---
We'll use
### <a href="https://www.anaconda.com/download" target="blank">VS Code</a>
(as part of Python 3.7 package)

---
and 
### [Jupyter Notebook](https://developers.arcgis.com/python/guide/using-the-jupyter-notebook-environment/)
a browser based editor installed by ArcGIS

---
## Customize VS Code
1. Bling it up with themes!
2. Create working directory, our root
3. Pro tips: modify settings

---?image=images/a01.png
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Themes</h3>

---
#### Let's setup your local root
### GIS project directory
where all of your GIS projects, assets, files, repos, and everything else will be stored related to class.

---
## Create working directory
Open *View > Terminal*

---?image=images/02/q-002.png
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Access console, terminal, command line, shell, etc.</h3>

---
### Type in the terminal I
```bat
:: This is a comment in windows terminal
:: Change directory to top of C: drive
cd C:\
:: If you're not on C: drive execute
C:
```
---
### Type in the terminal II
```bat
:: make a directory on C:
mkdir MyFunNameGIS
:: go into the new directory
cd MyFunNameGIS
```
---
### Type in the terminal III
```bat
:: make a directory on C:\
:: Create your COOL COOL name
mkdir BoydsGIS 
:: go into the new directory
cd BoydsGIS 
```
---
## How will I
### know all of these commands?!?

---?image=images/02/q-003.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Commands</h2>
<a href="http://simplyadvanced.net/blog/cheat-sheet-for-windows-command-prompt/" target="blank">cheat sheet</a>

---
## Modify settings
### For super-customized control
Open *File > Preferences > Settings > Edit in settings.json*



---
## After installing ArcGIS Pro
### Copy and paste:
```json
{
    "python.pythonPath":"C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3",
    "terminal.integrated.shell.windows": "C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\Scripts\\proenv.bat",
    "workbench.colorTheme": "NimboBimbo",
    "editor.fontSize": 17,
    "editor.fontFamily": "'Space Mono', Menlo, Monaco, 'Courier New', monospace",
    "editor.lineHeight":25,
    "terminal.integrated.fontSize": 18,
    "terminal.integrated.lineHeight": 1.05,
}
```

---
## Add readme.md
### in new directory
A Readme.md is a Markdown formatted file that tells visitors about your project (and helps you remember, too!)

---?image=images/02/q-004.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Open Folder...</h2>

---?image=images/02/q-005.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Right-click...</h2>

---?image=images/02/q-006.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Preview</h2>

---?image=images/02/markdown.md.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Many ways to create</h2>
<a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet" target="blank">Markdown.md</a>

---
# Whew!
What if we lost our text?

---
# GIT
"Git is a version control system for tracking changes in computer files and coordinating work on those files among multiple people."

---
![Git](images/02/git.png)<br>
[xctd](http://xkcd.com/)


---  
[Git](https://git-scm.com/) was created by Linus Torvalds in 2005 for development of the Linux kernel, with other kernel developers contributing to its initial development.


---
We'll use the git hosting service
### GitHub
and their desktop app to manage our projects.

---
Get account at [GitHub.com](https://github.com/) using your
### uky.edu
email address

---
### Our GitHub flow each week
* Find invitation to lesson in Canvas
* Accept invitation and _clone remote repository_
* Work through lesson/lab and save work
* _Commit_ changes as you go and _push_ when finished.

---
### GitHub Pages
Use GitHub to publish web pages, including
### Map Portfolio!


---
### Let's clone our lesson
## Repo
(use link in Canvas)

---
### First, let's install and
## sign in

---?image=images/02/q-007.png

---?image=images/02/q-010.png

---
## Create a local repo:
## _geo409_
inside your root GIS folder

---?image=images/02/q-009.png

---
# Publish
## in GitHub

---
## Create a remote repo called
## _rrg_
(if you haven't already)

---?image=images/02/q-011.png

---
# Clone
## to local root GIS folder

---
# Tips
* Add @UKy-GIs to your profile information
* Always Fetch and pull remote changes before you start
* Commit and push often!

---
# !!
* Create a folder outside of any repo to download data.
* Create: c:/GIS/BoydsGIS/data folder
* 100 MB limit in GitHub
* Data is redundant, code is unique

---
# How to undo in Git
* Can undo almost anything
* "Revert This Commit" is just for single undo
* More complex undo need to use command line
* [Cheat sheet](https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/)


---?image=images/02/natural-earth-download.jpg
<div style="background-color: rgba(0,0,0,0.4);width:100%;height:100%;margin: 0 auto;padding:20px 0;">
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Download data</h2>
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">to "data" folder</h3>
<a href="http://www.naturalearthdata.com/downloads/10m-cultural-vectors/" target="blank">Natural Earth</a>
</div>

---?image=images/02/natural-earth-download.jpg


---
## Create folder in _geo409_
### "c01"
* Open ArcMap
* and QGIS


---
## Measure state areas in
# ArcMap

---
## Change your Data Frame's
# Projection

---?image=images/02/arcmap-projection.jpg
<h2 style="color:#111;text-shadow: 2px 2px 4px #eee;">EPSG: 5070</h2>

---
```
NAD_1983_Contiguous_USA_Albers
WKID: 5070 Authority: EPSG

Projection: Albers
False_Easting: 0.0
False_Northing: 0.0
Central_Meridian: -96.0
Standard_Parallel_1: 29.5
Standard_Parallel_2: 45.5
Latitude_Of_Origin: 23.0
Linear Unit: Meter (1.0)

Geographic Coordinate System: GCS_North_American_1983
Angular Unit: Degree (0.0174532925199433)
Prime Meridian: Greenwich (0.0)
Datum: D_North_American_1983
  Spheroid: GRS_1980
    Semimajor Axis: 6378137.0
    Semiminor Axis: 6356752.314140356
    Inverse Flattening: 298.257222101

```


---
```
North_America_Albers_Equal_Area_Conic
WKID: 102008 Authority: Esri

Projection: Albers
False_Easting: 0.0
False_Northing: 0.0
Central_Meridian: -96.0
Standard_Parallel_1: 20.0   // Only change in
Standard_Parallel_2: 60.0   // standard parallels
Latitude_Of_Origin: 40.0    // and refocus north
Linear Unit: Meter (1.0)

Geographic Coordinate System: GCS_North_American_1983
Angular Unit: Degree (0.0174532925199433)
Prime Meridian: Greenwich (0.0)
Datum: D_North_American_1983
  Spheroid: GRS_1980
    Semimajor Axis: 6378137.0
    Semiminor Axis: 6356752.314140356
    Inverse Flattening: 298.257222101

```


---
### Select only those states we need
## Definition Query
```
"name" in ('Texas','Alaska','Kentucky')
```

---?image=images/02/arcmap-definition-query.jpg
<h2 style="color:#111;text-shadow: 2px 2px 4px #eee;"></h2>


---
## Open attribute table
# Add Field
as **Type: Float**

---?image=images/02/arcmap-add-field.jpg
<h2 style="color:#111;text-shadow: 2px 2px 4px #eee;"></h2>

---
## Right+click
# Field
and **Calculate Geometry**

---?image=images/02/arcmap-area.jpg
<h2 style="color:#111;text-shadow: 2px 2px 4px #eee;"></h2>


---
## ArcMap mesaurement

```
name,       area_sq_km
Alaska,     1496210
Texas,      685531
Kentucky,   104525
```

---
## Measure state areas in
# QGIS

---
### Housekeeping
open pgAdmin and check if PostGIS is installed

---?image=images/02/postgres.png


---
### QGIS Browser Panel
## Connect PostGIS database


---?image=images/02/connect_postgres.png

---
### QGIS DB Manager
## Import Layer


---?image=images/02/qgis-import-layer.png

---
### Finally!
## Open SQL Window

---?image=images/02/qgis-connect-db.png

---?image=images/02/qgis-execute-sql.jpg
<h2 style="color:#111;text-shadow: 2px 2px 4px #eee;">Execute SQL...</h2>


---

```
/* select everything */

select * from ne_10m_admin_1_states_provinces_lakes
```

---

```
/* select just texas, kentucky, and alaska */

select
    name
from
    ne_10m_admin_1_states_provinces_lakes
where
    name in ('Texas','Alaska','Kentucky')
```

---

```
/* select states and calculate area */

select
    name,
    ST_Area(geom) As "area in what units?"
from
    ne_10m_admin_1_states_provinces_lakes
where
    name in ('Texas','Alaska','Kentucky')
```

---

```
/* select states and calculate area in new projection, EPSG: 5070 */

select
    name,
    ST_Area(ST_Transform(geom, 5070)) As "sq. meters"
from
    ne_10m_admin_1_states_provinces_lakes
where
    name in ('Texas','Alaska','Kentucky')
```


---

```
/* select states and calculate area in new projection, EPSG: 5070 */
/* and sort, too! */

select
    name,
    (ST_Area(ST_Transform(geom, 5070))/1000000) As "sq km",
    (ST_Area(geom, true))/1000000 As "sq km on spheroid"
from
    ne_10m_admin_1_states_provinces_lakes
where
    name in ('Texas','Alaska','Kentucky')
order
	by "sq km" DESC
```

---

## Measurement

```
name,       sq km       sq km on spheroid
Alaska,     1505637.34, 1505638.85
Texas,      684969.01,  684969.02
Kentucky,   104576.98,  104576.98

```

---
# Challenge
Do all of this without opening a desktop program?
## Script it!

---
### Create a file called
## measure.bat
in VS Code

---
### Access
* QGIS 3.2 > OS4GeoW Shell
* change directory to BoydsGIS\geo409\c01

---
### Experiment with
## ogr2ogr
Library that supports data manipulation in QGIS


---
```bat
:: run program
ogr2ogr --version

:: Create projected GeoJSON and select three states
ogr2ogr -f geojson projected.geojson -sql "select name from ne_10m_admin_1_states_provinces_lakes where name in ('Texas','Alaska','Kentucky')" -s_srs EPSG:4326 -t_srs EPSG:5070 d:\BoydsGIS\data\ne_10m_admin_1_states_provinces_lakes.shp

:: Use ogr2ogr internal measurement feature
ogr2ogr -f CSV output.csv -sql "select name, (OGR_GEOM_AREA/1000000) as sq_km from ne_10m_admin_1_states_provinces_lakes" projected.geojson

:: Use PostGIS database to access data if working in QGIS
:: ogr2ogr -f CSV output.csv -sql "select name, (st_area(geom,true)/1000000) as sq_km from ne_10m_admin_1_states_provinces_lakes where name in ('Texas','Alaska','Kentucky')" PG:"dbname=postgres host=localhost port=5432 user=postgres password=postgres"
```

---
### Save your
## project files
#### then commit and push!

---
## That's the
# Challenge
this semester and we'll keep at it!


