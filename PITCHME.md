---?image=https://live.staticflickr.com/65535/47966553676_2ae0b1a989_o.jpg&opacity=40
# GEO 409:02
## Intro to ArcGIS Pro and Python 3


---
# NEWS
@ul[squares]
* maptimeLEX tonight at 6pm
* Free pizza!
* Info: https://maptimelex.github.com/monochromatic-maps
@ulend


---?image=https://raw.githubusercontent.com/maptimelex/monochromatic-maps/master/images/tie-dye-kentucky.jpg

---
## Goals
@ul[squares]
* Maintain data hygiene
* Test-drive ArcGIS Pro
* Begin Red River Gorge base map
* Start hacking Python (proper intro next module)
* Stay cool
@ulend

---?image=https://live.staticflickr.com/65535/47966498192_274d29b412_o.jpg&opacity=40
## Data

---?image=https://live.staticflickr.com/65535/47834322722_86a0fd6035_o.jpg&opacity=40
## Real places

---
## Organization
@ul[squares]
* Keep GIS folder organized
* Be consistent
* Don't put a file >50 MB in repo
* Don't put a .gdb folder in repo
* Don't put a repo in repo
@ulend

---
## Example folder structure

---?image=images/03/a001.png


---
## Use your student resources
@ul[squares]
* Microsoft or Google cloud storage
* Sync large files remotely
* Access via your LinkBlue account
@ulend

---?image=images/03/a002.png

---
## Download ArcGIS Pro
@ul[squares]
* For installation on personal computer
* Use this [OneDrive shared link](https://luky-my.sharepoint.com/:u:/g/personal/blshea1_uky_edu/EXZc5GPN41ZIrqjiSlO3AjEBJo3Z7ybHSc1qWDqkrySpVw?e=yHASu6) then update ArcGIS Pro OR
* In class: \\as-beijing.ad.uky.edu\geo\software\fall19\ 
* On MacOS? [Get Parallels](https://www.parallels.com/products/desktop/trial/)
@ulend

---
## UKy ArcGIS Online
@ul[squares]
* UKy has Organization account
* URL: [UKY-EDU.maps.arcgis.com](https://UKY-EDU.maps.arcgis.com)
* Login with credentials created after invite
@ulend

---?image=images/03/a003.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Our Portal</h2>

---
## Setup project in root GIS folder
* [Download and unzip lesson/lab data](https://luky-my.sharepoint.com/:u:/g/personal/blshea1_uky_edu/EZ_A1MZ5tqJKm7E_RFvE3hEByn0LEJN7aIc1VJ0ByrDQ0g?e=I4a3uF)
* Put geodatabase in *data* folder

---
## Let's get started!
@ul[squares]
* Launch ArcGIS Pro
* [Tutorials](http://pro.arcgis.com/en/pro-app/get-started/pro-quickstart-tutorials.htm)
* Tour drive around GUI
@ulend



---?image=images/03/a004.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Global settings</h2>

---?image=images/02/01.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Insert > New Local Scene</h2>

---?image=images/02/02.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Add Elevation Source</h2>

---
## Add all layers
@ul[squares]
* Explore how to symbolize layers
* Reorder them in the **Contents** pane
* Flex your GIS muscle memory!
@ulend

---
## Geoprocessing
@ul[squares]
* Tools with input, function, output
* Chain tools together for complex analysis
* Recognize sequence that can be coded
@ulend

---?image=https://live.staticflickr.com/65535/47966498192_274d29b412_o.jpg&opacity=40
## First tool
@ul[squares]
* CLIP
* Remove extraneous data outside area of interest (aoi)
* Use the [help docs!](http://desktop.arcgis.com/en/arcmap/10.3/tools/analysis-toolbox/clip.htm)
@ulend

---?image=https://live.staticflickr.com/65535/47834322722_86a0fd6035_o.jpg&opacity=40
## First task
@ul[squares]
* Clip our layers to the aoi
* Let's do it!
@ulend

---?image=https://live.staticflickr.com/65535/47966553676_2ae0b1a989_o.jpg&opacity=40
## Start coding
* Getting scrappy with Python!
* Watch [these short videos](https://www.py4e.com/lessons/intro) in *Python for Everybody*


---
# STOP



---
## Python 
@ul[squares]
* Modular programming
* functions >> modules >> packages
    * for: simplicity, maintainability, reusability
* package.module.function
@ulend

---
## An open-source quilt of contributions

---?image=https://www.metmuseum.org/toah/images/hb/hb_1996.4.jpg

---
## Managing your environment
@ul[squares]
* A development environment is a constellation of packages
* Most depend on a distinct version of other packages
* Chain of dependencies must not be broken!
@ulend

---
## Dependency Hell
* [Yep, there's a term for it](https://en.wikipedia.org/wiki/Dependency_hell)
* [Image Dependencies for Gentoo Linux](https://cgatoxford.files.wordpress.com/2017/05/gentoo-deps.jpg)
* [link](https://cgatoxford.wordpress.com/2017/05/12/the-dependency-hell-in-software-development/) 


---
## Python in ArcGIS Pro
@ul[squares]
* Built-in Package Management
* Development in Windows OS only
* Make clone of default read-only environment
@ulend


---
## Python in VS Code
@ul[squares]
* Use Anaconda or ArcGIS Pro
* Create *.py* files to execute in terminal
* Develop on most operating systems
* Create first program: "Geography, Y'all!"
@ulend

---
## Development in ArcGIS Pro
@ul[squares]
* Jupyter Notebook creates *.ipynb* files
* Run cells of code rather than the entire script
* Cells can be Python or Markdown
@ulend

---
## Setting up geoprocessing 
@ul[squares]
* ArcPy is the Python package that ships with ArcGIS Pro
* Very well documented
* Typically other properties are set to customize your workflow
@ulend

---
# ArcPy

---
```python
# get the ArcGIS tools!
import arcpy # case-sensitive!
```

---
```python
# set environment properties
arcpy.env.workspace = r"Z:\BoydsGIS\data\rrg_build.gdb"
arcpy.env.overwriteOutput = True
# use dot notation to address functions, properties, etc.
```

---
```python
# get list of feature classes in our database
# and print them to the screen
featureList = arcpy.ListFeatureClasses()
print(featureList)
```

---
```python
# get list of feature classes in our database
# and print them to the screen
rasterList = arcpy.ListRasters()
print(rasterList)
```

---
```python
# vector clip to area of interest
arcpy.analysis.Clip("cookie dough", "cookie cutter", "output cookie")
```


---
# STOP

---
```python
# build field data type showing properties of us_arches fields.
fields = arcpy.ListFields(layer_name)
for field in fields:
    fieldInLayer = f"{field.name} is a type of {field.type}."
    print(fieldInLayer)
```