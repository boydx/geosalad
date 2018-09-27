#HSLIDE
# GEO 409:03
## Basic Python data structures and conditional execution

#HSLIDE
## How to learn?
* Clone this lesson's repo 
* Open Jupyter Notebook and follow along!
* [Typical workflow](https://uky-gis.github.io/support/python-arcgis/)

#HSLIDE
![Complexity](https://imgs.xkcd.com/comics/python_environment.png)

#HSLIDE
## Value
* A value is data that we use in our program. 
* All values have a distinct type.
* Many different types of value.

#HSLIDE
## Basic types
### String
### Integer
### Float
Can you identify their attributes?

#HSLIDE
## Levels of Measurement
### Nominal
### Ordinal
### Ratio 
When you see an integer don't assume it's quantity

#HSLIDE
## Constants
### Literals
The syntax of type tells what it is.
```
"I am a literally a string of characters"
```

#HSLIDE
## Variables
### Assign value
to an arbitrary and limited set of characters.

#HSLIDE
## Variables
### Make meaningful variable names
not var1, 1var, or reserved keyword

#HSLIDE
## Type
### determine type
```
# type() function
type(v)
```

#HSLIDE?image=https://farm8.staticflickr.com/7330/26735803704_1b2f65bb9e_h.jpg
## Challenge

#HSLIDE
## Challenge 
How tall is it compared to Natural Bridge?
```
yourHeight = input("height: ")
natbridgeHeight = 65
print(type(yourHeight))

# percentDifference = 
# print(percentDifference)
```

#HSLIDE
## (a) Solution
### [Jupyter Notebook](https://github.com/UKy-GIS/uky-gis.github.io/blob/master/support/python-arcgis/examples/height_challenge.ipynb)

#HSLIDE
## Assignement operators
### Assign value to variables

#HSLIDE
## Assigns right to left
# =

#HSLIDE
## Adds right to left
# +=

#HSLIDE
```python
x = 1
# x must be assigned first!
x += 6
```

#HSLIDE
## Comparison operators
### Returns `True` or `False`

#HSLIDE
## Equality
# ==
True if same value

#HSLIDE
## Identity
# is
Same value, type, and object

#HSLIDE
```python
x = 1
y = 1.0
z = x
x == y # True
x is y # False
z is x # True
```

#HSLIDE
## Inequality
# !=
True if different value

#HSLIDE
## When to use?
# == !=
As long as it is *not equal to* x, continue working!

#HSLIDE
## Membership operators
### Returns `True` or `False`

#HSLIDE
## String sequence in
# in
True if substring in string

#HSLIDE
```python
place = "Grays Arch"
"Gray" in place # True
"gray" in place # False
"gray" not in place # True
```

#HSLIDE
## Logical operators
### Returns `True` or `False`
Combine other comparisons

#HSLIDE
```python
place = "Grays Arch"
"Gray" in place or "gray" in place # True
"Gray" in place and "gray" in place # False
"Gray" in place and "Arch" in place # True
```

#HSLIDE?image=http://annessky.net/blog/wp-content/uploads/2017/11/Interval_20.png
<h1 style="text-shadow: 2px 2px;">Challenge</h1>

#HSLIDE
### Contouring program
The new [KyTopo Map](http://kygeonet.ky.gov/) uses the new lidar data to create new statewide topographic maps. The 40-ft contour interval is indexed every fifth contour. Determine if any value is an index.

#HSLIDE
## Modulus operator
# % 
Divides left by right and returns remainder

#HSLIDE
```python
x = 40
print(x%20) # returns 0
```

#HSLIDE
## Input function
# input("str") 
Creates string from user input

#HSLIDE
```python
contour = input("Contour value: ")
print(contour)
```

#HSLIDE
## Convert to integer
# int("string") 
Create integer from string

#HSLIDE
```python
contour_remainder = int(contour)%40
```

#HSLIDE
### if statement
## if condition true:
Execute code body when true

#HSLIDE
```python
if contour_remainder == 0:
    print("Contour!") # Indent four spaces
```

#HSLIDE
### if/else statement
## else:
Execute code body when false

#HSLIDE
```python
if contour_remainder == 0:
    print("Contour!") # Indent four spaces
else: 
    print("Not a contour!")
```

#HSLIDE
### if/elif/else statement
## elif condition true:
Else if this condition is true execute code body

#HSLIDE
```python
if contour_remainder == 0:
    print("Contour!") # Indent four spaces
elif contour_remainder == 1:
    print("Close!")
else: 
    print("Not a contour!")
```

#HSLIDE
## if/elif/else statement
### Only one branch is true and executes

#HSLIDE
## if/if/if statement
### All branches could be true

#HSLIDE
## Errors
Anticipate and prevent

#HSLIDE
![Errors](http://phdcomics.com/comics/archive/phd120804s.gif)

#HSLIDE
# Syntax
# Exception
# Logic

#HSLIDE
### try/except statement
## Prevent exceptions
If it works conitnue, if it blows up let's do something else

#HSLIDE
```python
try:
    countInt = int(contour)
except:
    print("not a number, yo!")
```

#HSLIDE
### Exceptions can be
## good
because they can teach you.


#HSLIDE
### Prevent errors of
## logic
The program executes properly, but the result isn't valid.

#HSLIDE
```python
if contourInt > 4139 or contourInt < 257:
    print("You're not in Kentucky!")
```

#HSLIDE?image=http://annessky.net/blog/wp-content/uploads/2017/11/KyTopo_24K_N17E22_Bradfordsville.png
[Jupyter Notebook](https://github.com/UKy-GIS/uky-gis.github.io/blob/master/support/python-arcgis/examples)

#HSLIDE?image=https://www.outragegis.com/pixel/_data/i/galleries/1403013_RRG/_IMG1071-me.jpg
## Lab challenge 

#HSLIDE
### ArcGIS
Setup US Arches project. Can you find the highest arch above sea level?

#HSLIDE
# Base map layout
Create locator maps for our project

#HSLIDE
## Get data from Canavas module
Source:
[Natural Earth administrative boundaries](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/)

#HSLIDE
# Add New Map

#HSLIDE?image=images/03/a005.png

#HSLIDE
# Organize databases

#HSLIDE?image=images/03/add-database.gif

#HSLIDE
# Set coordinate system

#HSLIDE?image=images/03/a006.png

#HSLIDE
# Format point symbol

#HSLIDE?image=images/03/a007.png

#HSLIDE
# Insert new layout

#HSLIDE?image=images/03/a008.png

#HSLIDE
# Insert map frame

#HSLIDE?image=images/03/a009.png

#HSLIDE
# Adjust layout properties

#HSLIDE?image=images/03/a010.png

#HSLIDE
# Activate map frame
To fine tune it's placement in frame

#HSLIDE?image=images/03/a011.png

#HSLIDE
# Add elements

#HSLIDE?image=images/03/a012.png

#HSLIDE
# Fine tune

#HSLIDE?image=images/03/a013.png

#HSLIDE
# New map
ArcGIS Pro can have multiple maps and layouts in one document! 🤯 Make one for area of interest.

#HSLIDE
# Definition query

#HSLIDE?image=images/03/a014.png

#HSLIDE
# Add halo

#HSLIDE?image=images/03/a015.png

#HSLIDE
# Add labels

#HSLIDE?image=images/03/a016.png

#HSLIDE
# Adjust position

#HSLIDE?image=images/03/a017.png

#HSLIDE
# Tweak endlessly

#HSLIDE?image=images/03/a018.png

#HSLIDE
# Export GeoPDf

#HSLIDE?image=images/03/a019.png
