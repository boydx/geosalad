---
# GEO 409:01
## Advanced topics in GIS

---?image=https://www.outragegis.com/weather/img/animation/yesterday/LookRock.gif&opacity=40
### Managing complex workflows
Office hours W 1:30-2:30 & Tr 5:30-6:30   
[maptimeLEX](https://github.com/maptimelex/schedule): next Tr, 6-7 @ Miller Hall
@ul[squares]
* GIS and information intensive projects have many assets that sprawl across directories.
@ulend
@snap[south-west span-20 text-italic text-04]
Great Smokies, yesterday
@snapend

---?image=images/02/heat-trees.png
@snap[south-west span-20 text-italic text-04]
[Link](https://www.npr.org/2019/09/03/754044732/as-rising-heat-bakes-u-s-cities-the-poor-often-feel-it-most)
@snapend

---?image=https://live.staticflickr.com/1821/42233874915_b274295437_o.jpg&opacity=40
## Where did it go?


---?image=https://live.staticflickr.com/1824/42163152085_8a07212910_o.jpg&opacity=40
## Topics
@ul[squares]
* Set up our work environment
* Tools for the knowledge worker
* Review: measure US states's area the desktop way
* Challenge: measure area by code
@ulend



---
## Data hygiene
@ul[squares]
* Create single top-level directory for all projects, data, etc.
* We'll call this our *root* GIS directory
* Separate *redundant* from *created* assets
@ulend

---
## Example folder structure

---?image=images/02/a001.png


---
### Tools for the
## Knowledge worker

---
### We need to
## manage text
## ✏️📓🎓


---
## as code
### a/k/a plain-text instructions
that use *keywords* and *syntax*

---
## For example

---
This code
```html
<p style="color:blue;">Hello, world!</p>
```
---
renders to:
<p style="color:blue;">Hello, world!</p>

---
### Advantages of coding
@ul[squares]
* Work simply
* Work remotely
* Work when you sleep 🌝
* Share exact instructions
@ulend



---
First tool
# Text editor
Not Notepad, Microsoft Word, etc.

---
A good text editor offers
### Language syntax highlighting

---
We'll use
## VS Code
a popular open source and free editor

---
and 
### [Jupyter Notebook](https://developers.arcgis.com/python/guide/using-the-jupyter-notebook-environment/)
a browser-based editor for Python

---
## Customize VS Code
1. Bling it up with themes!
2. Create working directory, our root
3. Pro tips: modify settings

---?image=images/a01.png
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Themes</h3>

---
#### Let's setup your local
## root GIS directory
In VS Code, open *View > Terminal*


---?image=images/02/q-002.png
### Or, Terminal > New Terminal

---
### Type in the terminal I

---
```bat
rem This is a comment in windows terminal
rem Change directory to top of C: drive
cd C:\
rem If you're not on C: drive execute
C:
```
@[1]
@[3]
@[5]

---
### Type in the terminal II

---
```bat
rem make a directory on C:
mkdir MyFunNameGIS
rem go into the new directory
cd MyFunNameGIS
```
@[2]
@[4]


---
### Example

---
```bat
rem make a directory on C:\
rem Create your COOL COOL name
mkdir BoydsGIS 
rem go into the new directory
cd BoydsGIS 
```
@[3]
@[5]

---
## How will I
### know all of these commands?!?

---?image=images/02/q-003.png&opacity=40
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Commands</h2>
<a href="http://simplyadvanced.net/blog/cheat-sheet-for-windows-command-prompt/" target="blank">cheat sheet</a>

---
# Add info
## about this space

---
# Markdown
"write using an easy-to-read and easy-to-write plain text format" and convert it to pretty web pages

---
## Add readme.md
A Readme.md is a Markdown formatted file that tells visitors about your project 

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
# Git
"Git is a version control system for tracking changes in computer files and coordinating work on those files among multiple people."

---
![Git](images/02/git.png)    

[xctd](http://xkcd.com/)


---  
[Git](https://git-scm.com/) was created by Linus Torvalds in 2005 for development of the Linux kernel, with other kernel developers contributing to its initial development.


---
We'll use the Git hosting service
### GitHub
and their desktop app to manage our projects.

---
Get account at [GitHub.com](https://github.com/) using your
### uky.edu
email address

---
### Our GitHub flow each lesson
@ul[squares]
* Find invitation to lesson in Canvas
* Accept invitation and _clone remote repository_
* _Commit_ changes as you work 
* _Push to remote_ when finished
* _Pull_ in changes that I request
@ulend

---
### GitHub Pages
Use GitHub to publish web pages, including
### Map Portfolio!

---
Git is a
## DVCS
@ul[squares]
* Distributed 
* Version control system
@ulend


---
### Let's clone our lesson
## Repo
(use link in Canvas)

---?image=images/02/slides-00.png
---?image=images/02/slides-001.png
---?image=images/02/slides-002.png
---?image=images/02/slides-003.png
---?image=images/02/slides-03.png
---?image=images/02/slides-04.png
---?image=images/02/slides-05.png

---
## Sign in
### to GitHub 

---?image=images/02/q-007.png
---?image=images/02/q-010.png

---
## Workflow
### in Git repo


---?image=images/02/slides-02-01.png
---?image=images/02/slides-02-02.png
---?image=images/02/slides-02-03.png
---?image=images/02/slides-02-04.png
---?image=images/02/slides-02-05.png
---?image=images/02/slides-02-06.png
---?image=images/02/slides-02-07.png

---
## How to undo in Git
@ul[squares]
* Can undo almost anything
* GitHub Desktop
  * Before commit: **Discard Changes**
  * After commit: **Revert this Commit**
  * **Add file to .gitignore**
* More complex undos need to use command line ([Cheat sheet](https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/))
@ulend

---
# Tips
@ul[squares]
* Add @UKy-GIS to your GitHub.com profile information
* Always Fetch and pull remote changes before you start
* Commit and push often!
@ulend

---
# MEGA!!
@ul[squares]
* Create a folder outside of any repo to download data.
* Create: c:/BoydsGIS/**data** folder
* 100 MB limit in GitHub
* Data is redundant, code is unique
@ulend




---
# Practice


---
## Create a local repo:
## _measure-states_
inside your root GIS folder

---?image=images/a02.png

---
## Open in VS Code
from GitHub Desktop

---?image=images/a03.png

---
## Edit readme.md:
```md
# measure-states

Let's practice measuring state areas.

* [Downloads data on Canvas](https://uk.instructure.com/courses/1950078/modules)
* [Source on Natural Earth](https://www.naturalearthdata.com/downloads/)
```

---?image=images/02/natural-earth-download.jpg&opacity=40
## Layer on Canvas

---
# Publish
## in GitHub

---
## Measure state areas in
# ArcMap

---
## Change your Data Frame's
# Projection

---?image=images/02/arcmap-projection.jpg
<h2 style="color:#111;text-shadow: 2px 2px 4px #eee;">EPSG: 5070</h2>

---
## Investigate 
Coordinate reference system (CRS) parameters

---
```yaml
Name: NAD_1983_Contiguous_USA_Albers
WKID: 5070 Authority: EPSG
Projection: Albers
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
```yaml
Name: North_America_Albers_Equal_Area_Conic
WKID: 102008 Authority: Esri
Projection: Albers
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
## Compare 
Many CRS definitions are very similar

---
## Select three states
@ul[squares]
* We want only Alaska, Texas, and Kentucky
* How do we do it?
@ulend


---
```sql
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
## Challenge
Do all of this without opening a desktop program?
## Script it!

---
### Create files called
## ares.bat & info.bat
in VS Code

---
### Access terminal
@ul[squares]
* change directory to rootGIS\measure-states
* Open terminal in VS Code
* Type: C:\"Program Files"\"QGIS 3.8"\OSGeo4W.bat
* Type: o-help
@ulend

---
### Experiment with
## ogrinfo & ogr2ogr
Libraries that supports vector data manipulation in QGIS


---
```bat
:: run program
ogr2ogr --version

:: Create projected GeoJSON and select three states
ogr2ogr -f geojson projected.geojson -sql "select name from ne_10m_admin_1_states_provinces_lakes where name in ('Texas','Alaska','Kentucky')" -s_srs EPSG:4326 -t_srs EPSG:5070 ne_10m_admin_1_states_provinces_lakes.shp

:: Use ogr2ogr internal measurement feature
ogr2ogr -f CSV output.csv -sql "select name, (OGR_GEOM_AREA/1000000) as sq_km from ne_10m_admin_1_states_provinces_lakes" projected.geojson

```

---
### Save your
## project files
#### then commit and push!

---
## That's the
# Challenge
this semester and we'll keep at it!

---
## Addendum

---
### History
* Command Line Interface (CLI)
* Many applications have command line interface
* CLI is hot again

---
[Do anything with the CLI](https://geekprank.com/hacker/)


---
## Modify settings
### In VS Code
Open *File > Preferences > Settings > Edit in settings.json*



---
### After installing ArcGIS Pro
### Copy and paste:
```json
{
    // After you install ArcGIS Pro, add the next three lines
    "terminal.integrated.shell.windows": "C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\Scripts\\proenv.bat",
    // OSGeo tools from QGIS - Add after installing QGIS
    // "terminal.integrated.shell.windows": "C:\\Program Files\\QGIS 3.8\\OSGeo4W.bat", 
    "editor.fontSize": 17,
    "editor.lineHeight":25,
    "terminal.integrated.fontSize": 18,
    "terminal.integrated.lineHeight": 1.05,
}
```
