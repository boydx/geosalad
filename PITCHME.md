#HSLIDE
# GEO 409:04
## Functions, methods, and loops

#HSLIDE
## Learning curve
* Moving steeply up curve
* Watch videos!
	* [functions](https://www.py4e.com/lessons/functions)
	* [string methods](https://www.py4e.com/lessons/strings)
	* [loops and iterations](https://www.py4e.com/lessons/loops)

#HSLIDE
## Payoff coming!

#HSLIDE?image=https://outragegis.com/gorge/animations/sun.gif

#HSLIDE
## Functions
* Block of statements that execute when called
* Might take arguments
* Might return data

#HSLIDE
```python
# function with two parameters
function(x, y)
# parameters are placeholders for passing arguments
```

#HSLIDE
```python
# define function
def function(x, y):
	z = int(x)**int(y)
	print(int(x) + int(y)) # prints to screen
	return z # when executed, function becomes this

function(2,4) # Need documentation!
```
#HSLIDE
```python
def function(x, y):
    """x to y power""" # Docstring provides info
    z = int(x)**int(y)
    return z

help(function)
```

#HSLIDE
## Builtin functions
* Python comes with about [60 functions](https://docs.python.org/3.6/library/functions.html)

```python
print("Hello World!")
```


#HSLIDE
## Round function

```python
round(x, y)
# x is float type, y is integer type
print(round(7.555, 2))
```

#HSLIDE
## Jupyter Notebook
* Open workbook for lesson
* Work through challenges

#HSLIDE
## Adding functions
* Python's sprawling [standard library](https://docs.python.org/3/library/)
* Adds new functions and data types
* The `decimal` module to correctly round numbers

#HSLIDE
```python
import decimal # use the module's namespace to access its functions
x = decimal.Decimal('7.555')

from decimal import * # access the module functions directly
x = Decimal('7.555')
```

#HSLIDE
## decimal properties
* Control precision and number of significant digits
* Rounding rules
* Useful in mapping and money applications

#HSLIDE
## Lat/lon coords
* 38.038015,-84.5046852!
* 1&deg; of lattitude = 69 miles
* 1.0&deg;  6.9 mi of precision
* 1.00&deg;  3600 ft
* 1.000&deg;  360 ft
* 1.0000&deg;  36 ft
* 1.000000&deg;  4 in



#HSLIDE
## UKy ArcGIS Online
* UKy has Organization account
* URL: [UKY-EDU.maps.arcgis.com](https://UKY-EDU.maps.arcgis.com)
* Login with credentials created after invite

#HSLIDE?image=images/03/a003.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Our Portal</h2>

#HSLIDE
## Setup project in root GIS folder
* [Download and unzip lesson/lab data](https://luky-my.sharepoint.com/:u:/g/personal/blshea1_uky_edu/EZ_A1MZ5tqJKm7E_RFvE3hEByn0LEJN7aIc1VJ0ByrDQ0g?e=I4a3uF)
* Put geodatabase in *data* folder

#HSLIDE
## Let's get started!
* Launch ArcGIS Pro
* [Tutorials](http://pro.arcgis.com/en/pro-app/get-started/pro-quickstart-tutorials.htm)
* Tour drive around GUI



#HSLIDE?image=images/03/a004.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Global settings</h2>

#HSLIDE?image=images/02/01.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Insert > New Local Scene</h2>

#HSLIDE?image=images/02/02.jpg
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Add Elevation Source</h2>

#HSLIDE
## Add all layers
* Explore how to symbolize layers
* Reorder them in the **Contents** pane
* Flex your GIS muscle memory!

#HSLIDE
## Start coding
* Getting scrappy with Python!
* Watch [second lesson videos](https://www.py4e.com/lessons/intro) in *Python for Everybody*


#HSLIDE
## Python 
* Modular programming
* functions >> modules >> packages
    * for: simplicity, maintainability, reusability, scoping/namespacing
* An open-source quilt of contributions

#HSLIDE?image=https://www.metmuseum.org/toah/images/hb/hb_1996.4.jpg

#HSLIDE
## Python in VS Code
* [Conda Package Management](https://conda.io/docs/user-guide/getting-started.html)
* Manage Virtual Environments
* Develop on most operating systems


#HSLIDE 
```bash
conda create --name geo409
activate geo409
```

#HSLIDE
## Python in ArcGIS Pro
* Built-in Package Management
* Make clone of default read-only environment
* Development in Windows OS only

#HSLIDE
## Development in ArcGIS Pro
* Jupyter Notebook
* Run cells of code rather than the entire script
* Download as Python (.py) file

#HSLIDE
## Setting up geoprocessing 
* ArcPy is the Python package that ships with ArcGIS Pro
* Very well documented
* Typically other properties are set to customize your workflow

#HSLIDE
# ArcPy

#HSLIDE
```python
# get the ArcGIS tools!
import arcpy # case-sensitive!
```

#HSLIDE
```python
# set environment properties
arcpy.env.workspace = r"Z:\BoydsGIS\data\rrg_build.gdb"
arcpy.env.overwriteOutput = True
# use dot notation to find correct tools, functions, properties, etc.
```

#HSLIDE
```python
# get list of feature classes in our database
# and print them to the screen
featureList = arcpy.ListFeatureClasses()
print(featureList)
```

#HSLIDE
```python
# get list of feature classes in our database
# and print them to the screen
rasterList = arcpy.ListRasters()
print(rasterList)
```

#HSLIDE
```python
# vector clip to area of interest
arcpy.analysis.Clip("cookie dough", "cookie cutter", "output cookie")
```

#HSLIDE
```python
# raster clip to area of interest
arcpy.analysis.Clip("cookie dough", "#", "output cookie", "cookie cutter")
```

#HSLIDE
# Wanna see into the future?

#HSLIDE
```python
# build field data type showing properties of us_arches fields.
fields = arcpy.ListFields(layer_name)
for field in fields:
    print(field.name + " is a type of " + field.type)
```