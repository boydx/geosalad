---
# GEO 409:03
## Basic Python data structures and conditional execution

---
## Python Objectives
@ul[squares]
* Learn basic types
* Be able to test for value
* `if/else` statements
* Lab: modify a program to export CSV of US Arches
@ulend

---
## AcrGIS Pro Objectives
@ul[squares]
* Make map of US Arches
* Practice SQL queries
* Begin your base map of RRG
@ulend

---
## How to learn?
* Clone this lesson's repo 
* Open Jupyter Notebook and follow along!
* [Typical workflow](https://uky-gis.github.io/support/python-arcgis/)
* Read the readme.md

---
![Complexity](https://imgs.xkcd.com/comics/python_environment.png)

---
## Value
* A value is data that we use in our program. 
* All values have a distinct type.
* Many different types of value.

---
## Basic types
### String
### Integer
### Float
Can you identify their properties?

---
## Levels of Measurement
### Nominal
### Ordinal
### Ratio 
When you see an integer don't assume it's a quantity.

---
## Constants
### Literals
The syntax of type tells what it is.
```
"I am a literally a string of characters"
```

---
## Variables
### Assign value
to an arbitrary and limited set of characters.

---
## Variables
### Make meaningful variable names
not var1, 1var, or reserved keyword

---
## Type
### determine type
```
# type() function
type(v)
```

---?image=https://farm8.staticflickr.com/7330/26735803704_1b2f65bb9e_h.jpg
## Challenge

---
## Challenge 
How tall is it compared to Natural Bridge?
```
yourHeight = input("height: ")
natbridgeHeight = 65
print(type(yourHeight))

# percentDifference = 
# print(percentDifference)
```

---
## (a) Solution
### [Jupyter Notebook](https://github.com/UKy-GIS/uky-gis.github.io/blob/master/support/python-arcgis/examples/height_challenge.ipynb)

---
## Assignment operators
### Assign value to variables

---
## Assigns right to left
# =

---
## Adds right to left
# +=

---
```python
x = 1
# x must be assigned first!
x += 6
```

---
## Comparison operators
### Returns `True` or `False`

---
## Equality
# ==
True if same value

---
## Identity
# is
Same value, type, and object

---
```python
x = 1
y = 1.0
z = x
x == y # True
x is y # False
z is x # True
```

---
## Inequality
# !=
True if different value

---
## When to use?
# == !=
As long as it is *not equal to* x, continue working!

---
## Membership operators
### Returns `True` or `False`

---
## String sequence in
# in
True if substring in string

---
```python
place = "Grays Arch"
"Gray" in place # True
"gray" in place # False
"gray" not in place # True
```

---
## Logical operators
### Returns `True` or `False`
Combine other comparisons

---
```python
place = "Grays Arch"
"Gray" in place or "gray" in place # True
"Gray" in place and "arch" in place # False
"Gray" in place and "Arch" in place # True
```

---?image=http://annessky.net/blog/wp-content/uploads/2017/11/Interval_20.png
<h1 style="text-shadow: 2px 2px;">Challenge</h1>

---
### Contouring program
The new [KyTopo Map](http://kygeonet.ky.gov/) uses the new lidar data to create new statewide topographic maps. The 40-ft contour interval is indexed every fifth contour. Determine if any value is an index.

---
## Modulus operator
# % 
Divides left by right and returns remainder

---
```python
contourInterval = 40
countour = 120
print(countour % contourInterval) # returns 0. It's a contour!
```

---
## Input function
# input("str") 
Creates string from user input

---
```python
contour = input("Contour value: ")
print(contour)
```

---
## Convert to integer
# int("string") 
Create integer from string

---
```python
contour_remainder = int(contour)%40
```

---
### if statement
## if condition true:
Execute code body when true

---
```python
if contour_remainder == 0:
    print("Contour!") # Indent four spaces
```

---
### if/else statement
## else:
Execute code body when false

---
```python
if contour_remainder == 0:
    print("Contour!") # Indent four spaces
else: 
    print("Not a contour!")
```

---
### if/elif/else statement
## elif condition true:
Else if this condition is true execute code body

---
```python
if contour_remainder == 0:
    print("Contour!") # Indent four spaces
elif contour_remainder == 1:
    print("Close!")
else: 
    print("Not a contour!")
```

---
## if/elif/else statement
### Only one branch is true and executes

---
## if/if/if statement
### All branches could be true

---
## Errors
Anticipate and prevent

---
![Errors](http://phdcomics.com/comics/archive/phd120804s.gif)

---
# Syntax
# Exception
# Logic

---
### try/except statement
## Prevent exceptions
If it works continue, if it blows up let's do something else

---
```python
try:
    countInt = int(contour)
except:
    print("not a number, yo!")
```

---
### Exceptions can be
## good
because they can teach you.


---
### Prevent errors of
## logic
The program executes properly, but the result isn't valid.

---
```python
if contourInt > 4139 or contourInt < 257:
    print("You're not in Kentucky!")
```

---?image=http://annessky.net/blog/wp-content/uploads/2017/11/KyTopo_24K_N17E22_Bradfordsville.png
## Jupyter Notebooks
[Link](https://github.com/UKy-GIS/uky-gis.github.io/blob/master/support/python-arcgis/examples)

---?image=https://www.outragegis.com/pixel/_data/i/galleries/1403013_RRG/_IMG1071-me.jpg
## Lab

---
## Review
@ul
* Copy Python command
* Combine commands together
* Execute
@ulend

---
## Repetition
### Where is it?
```python
arcpy.analysis.Clip("streams_water_areas", "area_of_interest", r"C:\BoydsGIS\L2\L2.gdb\streams_water_areas", None) 
```

---
## Variables
### Abstract string to a variable
@[1]
@[2]
```python
myOutputGDB = f"C:\\BoydsGIS\\L2\\L2.gdb\\"
arcpy.analysis.Clip("streams_water_areas", "area_of_interest", f"{myOutputGDB}streams_water_areas", None) 
```

---
### ArcGIS
Setup US Arches project. Can you find the highest arch above sea level?

---
# Base map layout
Create locator maps for our project

---
## Get data from Canvas module
Source:
[Natural Earth administrative boundaries](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/) and [Geographic Names Information System](https://geonames.usgs.gov/domestic/download_data.htm)

---
# Add New Map

---?image=images/03/a005.png&size=contain&opacity=100

---
# Organize databases

---?image=images/03/add-database.gif&size=contain&opacity=100

---
# Set coordinate system

---?image=images/03/a006.png&size=contain&opacity=100

---
# Format point symbol

---?image=images/03/a007.png&size=contain&opacity=100

---
# Insert new layout

---?image=images/03/a008.png&size=contain&opacity=100

---
# Insert map frame

---?image=images/03/a009.png&size=contain&opacity=100

---
# Adjust layout properties

---?image=images/03/a010.png&size=contain&opacity=100

---
# Activate map frame
To fine tune it's placement in frame

---?image=images/03/a011.png&size=contain&opacity=100

---
# Add elements

---?image=images/03/a012.png&size=contain&opacity=100

---
# Fine tune

---?image=images/03/a013.png&size=contain&opacity=100

---
# New map
ArcGIS Pro can have multiple maps and layouts in one document! 🤯 Make one for area of interest.

---
# Definition query

---?image=images/03/a014.png&size=contain&opacity=100

---
# Add halo

---?image=images/03/a015.png&size=contain&opacity=100

---
# Add labels

---?image=images/03/a016.png&size=contain&opacity=100

---
# Adjust position

---?image=images/03/a017.png&size=contain&opacity=100

---
# Tweak endlessly

---?image=images/03/a018.png&size=contain&opacity=100

---
# Export GeoPDF

---?image=images/03/a019.png&size=contain&opacity=100
