---?image=https://www.outragegis.com/weather/img/animation/yesterday/LookRock.gif&opacity=40
# GEO 409:02
### Basic Python data structures and conditional execution
@snap[south-west span-20 text-italic text-04]
Great Smokies, yesterday
@snapend

---
## Python Objectives
@ul[squares]
* Learn basic types
* Be able to test for value
* `if/else` statements
* Lab: make program to query/export locations of arches
@ulend


---?image=https://live.staticflickr.com/65535/48788851843_afbb1670d4_k.jpg&opacity=40
## How to learn?
@ul[squares]
* Clone this lesson's repo 
* Open Jupyter Notebook and follow along!
* [Typical workflow](https://uky-gis.github.io/support/python-arcgis/)
* Read the readme.md
@ulend


---
## Arches, like Grays Arch, are formed by [differential weathering](https://kgs.uky.edu/kgsweb/olops/pub/kgs/GeoStory.pdf)

---?image=https://live.staticflickr.com/65535/48789360117_94439e2314_k.jpg&opacity=100

---?image=https://live.staticflickr.com/65535/48789359227_79273ca1d1_k.jpg&opacity=100

---?image=https://live.staticflickr.com/65535/48788850923_9e67afd3b8_k.jpg&opacity=100

---?image=https://live.staticflickr.com/65535/48789211076_a1d9f7c7ac_k.jpg&opacity=100

---
## Value
@ul[squares]
* A value is data that we use in our program. 
* All values have a distinct type.
* Many different types of value.
@ulend

---
## Basic types
@ul[squares]
* String
* Integer
* Float
* Can you identify their properties?
@ulend


---
## Levels of Measurement
@ul[squares]
* Nominal
* Ordinal
* Ratio 
* When you see an integer don't assume it's a quantity.
@ulend


---
## Constants
Literals: the syntax tells us what type it is.

---
```python
"I am a literally a string of characters"
1.0 # I'm a float value
1 # Just an integer!
```

---
## Objects
Once a value is created, it is an object with properties and powers (more later).

---
```python
"I am a literally a string of characters".upper()
# returns 'I AM A LITERALLY A STRING OF CHARACTERS'
```

---
## Variables
Assign value to an arbitrary and limited set of characters.

---
## Variables
Make meaningful variable names, e.g., not var1, 1var, or use a reserved keyword.

---
## Type
Knowing the *type* of value tells you powers the value has.

---
```python
v = 1.0
# type() function
type(v)
# returns float
```

---?image=https://farm8.staticflickr.com/7330/26735803704_1b2f65bb9e_h.jpg
## Challenge

---
## Challenge 
How tall is it compared to Natural Bridge?

---
```python
yourHeight = input("height in feet: ")
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
# Challenge

---
### Contouring program
The new [KyTopo Map](http://kygeonet.ky.gov/) uses the new lidar data to create new statewide topographic maps. The 40-ft contour interval is indexed every fifth contour, or 200 ft. Determine if any value is an index.

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


---?image=https://www.outragegis.com/pixel/_data/i/galleries/1403013_RRG/_IMG1071-me.jpg
## Lab 2

---
## Review
@ul
* Copy Python function
* Combine functions together
* Execute
@ulend

---
## Goals
@ul
* Be able to scale up
* Do complex analysis
* Focus on finished cartography
@ulend



---
## Variablize
### Abstract string to a variable
@[1]
@[2]
@[3]
```python
myOutputGDB = f"C:\\BoydsGIS\\L2\\L2.gdb\\"
arcpy.analysis.Clip("streams_water_areas", "area_of_interest", 
f"{myOutputGDB}streams_water_areas") 
```

---
## Print
### Verify correct input/output
@[1]
@[2]
```python
print(myOutputGDB)
# outputs: C:\BoydsGIS\L2\L2.gdb\
```

---
## Organize
### Move variables to top
Easy access to change data sources, options, etc.

---
# Variablize
# Print
# Organize


