#HSLIDE
# GEO 409:03
## Basic Python data structures and conditional execution

#HSLIDE
## How to learn?
* Clone this lesson's repo 
* Open Jupyter Notebook and follow along!
* [Typical workflow](https://uky-gis.github.io/support/python-arcgis/)

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
## Challenge 

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
# input("string") 
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
contour_remainder = contour%40
```

#HSLIDE
## if statement
# if condition true:
Execute code body when true

#HSLIDE
```python
if contour_remainder == 0:
    print("Contour!") # Indent four spaces
```

#HSLIDE
## if/else statement
# else:
Execute code body when false

#HSLIDE
```python
if contour_remainder == 0:
    print("Contour!") # Indent four spaces
else: 
    print("Not a contour!")
```

#HSLIDE
## if/elif/else statement
# elif condition true:
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
## Challenge 
### ArcGIS
Setup US Arches project. Find the highest arch above sea level
