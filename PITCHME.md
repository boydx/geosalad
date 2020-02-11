---?image=https://www.outragegis.com/weather/img/animation/yesterday/LookRock.gif&opacity=40
# GEO 409:03
## Functions, methods, and loops

---
## Learning curve
@ul[squares]
* Moving steeply up curve
* Watch videos!
	* [functions](https://www.py4e.com/lessons/functions)
	* [string methods](https://www.py4e.com/lessons/strings)
	* [loops and iterations](https://www.py4e.com/lessons/loops)
@ulend

---
## Payoff coming!

---?image=https://maptimelex.github.io/wildcat-eyes/assets/images/q01.png&opacity=100

---?image=https://maptimelex.github.io/wildcat-eyes/assets/images/q02.png&opacity=100

---?image=https://maptimelex.github.io/wildcat-eyes/assets/images/q06.png&opacity=100


---
## Objectives
@ul[squares]
* Learn more fundamental Python to process data
* Work with a Python script
* Extract raster imagery
@ulend

---?image=https://live.staticflickr.com/4882/44529819000_3487acf8b7_3k.jpg&opacity=100
## Your lab work

---
## Lab 2
@ul[squares]
* Your commit log shows how much work you're doing
* 19 commits v 1 commit
* **commit often, perfect later**
@ulend


---
## Lab 2
@ul[squares]
* Grade tomorrow
* Everyone submitted, thank you!
* Chance to fix answers...
@ulend

---
```py
x == 1 # returns x undefined
# how to fix?
```

---
```py
x = True # really? That's cheeky.
# 🚫👻🤷
```

---
## Lab 3
@ul[squares]
* More Python 🏋️💪🎓
* Learn to go loopy
* Manage even larger datasets
@ulend


---
## TOC
@ul[squares]
* Functions
* Sequences
* Loops
* An application
@ulend


---
# Functions

---
## Workhorse
of any programming language

---
# 📚 ➡ 🔨 ➡ 🌟

---
## Most important function for you now?

--- 
```python
print(someVariable) # What is this variable?
# Print to find out!
```


---
## Functions
@ul[squares]
* Syntax: `functionName()`
* Block of statements that execute when called
* Might pass info into function as **arguments**
* Might **return** data
@ulend



---
```python
# function with two parameters
functionName(x, y)
# parameters are 'placeholders' for passing arguments
```

---
## Parameters
@ul[squares]
* Variables inside function
* Allows us to pass information to the function
* **SEQUENCE is CRITICAL**
@ulend

---?
## Example: clip function
@ul[squares]
* Probably most common GIS tool
* Extract spatial features by area of interest
@ulend

---?image=https://66.media.tumblr.com/31fbae995fe05a3c19f3bc88d9a78e1e/5fb2e54a0288ab22-41/s500x750/953e49b56ea5c634aadcc12801531a3774bff6a7.gifv
## What?
@ul[squares]
* Spatial features: cookie dough
* AOI: cookie cutter
@ulend

---
#### Sequence of parameters are critical
```py
arcpy.Clip_Management(x, y, z) # what are x, y, and z?
```

---
#### Sequence of parameters are critical
```py
x = "c:\\data\\KY_Rivers
y = "c:\\data\\Bluegrass
z = "c:\\project\\Bluegrass_Rivers
arcpy.Clip_Management(x, y, z)
```

---
# Challenge I
Build a function

---
```python
# What is this function doing?
function(2, 3)
# prints 8
```

---
## Define function
@ul[squares]
* Store and reuse statements
* `def` keyword defines a function
* followed by unique name and `():`
* Parameters?
* Indent function body four spaces
@ulend

---
@[2]
@[3]
@[4]
@[5]
```python
# define function
def powersXtoY(x, y): # function has arbitrary name
	z = int(x)**int(y)
	print(z) # prints to screen
	return z # when executed, function becomes value of z

powersXtoY(2,3) # Need documentation!
```
---
```python
def powersXtoY(x, y):
    """x to y power""" # Docstring provides info
    z = int(x)**int(y)
    return z

help(powersXtoY)
```

---
# Challenge II
Build a function that finds the highest elevation in a list of elevations.

---
elevations = [1232, 452, 1224, 599, 745, 355, 899]


---
## Built-in functions
@ul[squares]
* Python comes with about [60 functions](https://docs.python.org/3.8/library/functions.html)
* Don't need to `import` anything
@ulend

---
## Round function

```python
round(x, y)
# x is float type, y is integer type
print(round(7.555, 2))
```

---
# What!?!

---
## Adding functions
@ul[squares]
* Python's sprawling [standard library](https://docs.python.org/3/library/) of modules
* Adds new functions and data types
* The `decimal` module to correctly round numbers
* Use dot notation to address functions
@ulend

---
```python
import decimal # use the module's namespace to access its functions
x = decimal.Decimal('7.555')

from decimal import Decimal # access the module functions directly
x = Decimal('7.555')
```
@[1-2]
@[3-4]

---
## decimal properties
@ul[squares]
* Control precision and number of significant digits
* Rounding rules
* Useful in mapping and money applications
@ulend

---
## Lat/lon coords
@ul[squares]
* 38.038015, -84.5046852!
* 1&deg; of lattitude = 69 miles
* 1.0&deg;  6.9 mi of precision
* 1.00&deg;  3600 ft
* 1.000&deg;  360 ft
* 1.0000&deg;  36 ft
* 1.000000&deg;  4 in
@ulend

---
## Objects & methods 🔮
@ul[squares]
* Every object has a 
    * *identity*
    * *value*
    * *type* 
* **Methods** are functions that operate on certain objects
	* object.function()
    * e.g., `readerObject = csv.reader(csvFile)`
@ulend

---?
```python
# same value, different type and identity
1 == 1.0 # true
1 is 1.0 # false

# methods on float type
x = 1.0
x.is_integer() # true
```

---
# Strings

---
## String methods 
@ul[squares]
* More common
* Perform common tasks on strings
* Find substrings, change case, etc.
* [Built-in methods](https://www.w3schools.com/python/python_ref_string.asp)
* Most return new values, others return `True`/`False`
@ulend

---
## String indexes
@ul[squares]
* Sequence of characters have positions in string starting at zero.
* Bracket notation to show position.
@ulend

---?image=https:/uky-gis.github.io/support/python-arcgis/graphics/string_indexes.png&opacity=100&size=contain

---
```python
"Hello World!"[0] # returns H
"Hello World!"[-1] # returns !
"Hello World!"[4] # returns o
```

---
## String slice
@ul[squares]
* Access substring using start:end indexes
* End index is up-to-but-not-including
* Address in string v. length of string
@ulend

---
```python
len("Hello World!") # returns 12
"Hello World!"[0] # returns H
"Hello World!"[11] # !
"Hello World!"[0:12] # returns all
"Hello World!"[:12] # returns all
"Hello World!"[12] # returns error, out of index range
```

---
## String index challenge
Print the arch variable backwards using only string indexes

---?image=https://www.outragegis.com/weather/img/animation/190101/LookRock.gif&opcity=40
# Loops

---
## while loop
@ul[squares]
* Runs while true
* Avoid infinite loop with breaks
* loop body indented with four spaces
@ulend


---
```python
arch = "Grays Arch"
while "Natural Bridge" not in arch:
    print("Crash this program")
# No!
```

---
```python
length_of_word = len(arch)
i = 0
while i < length_of_word:
    print(arch[i])
    # What's missing?
```

---
# STOP

---
## while loop challenge
Create a while loop that runs until a correct state name is input

---
## for loop
* Iterates through a list, value by value.
* Indented four spaces
* Runs a definite number of times


---
```python
# We need to create a list first.
# Assume we have a much, much large string than this
place = "Welcome to the lost treasures of Silvermine Arch and Hidden Arch in Wolfe county!"

# Split a string into list on each space in string
listOfWords = place.split(" ") # returns 14 words

# print the contents of listOfWords
print(listOfWords) # use the print function to see how it works
```

---
## for loop challenge
Scan text and print the names of the arches in the text.

---?image=https://farm2.staticflickr.com/1901/44221426354_d8a711a753_h.jpg&opacity=100

---
## Lesson addendum
* `import csv` module
* iterate through `arches.csv`


--- 
## Lab practice
* Refactor script from lab 2
* Create hillshade script



---
```python
# build field data type showing properties of us_arches fields.
fields = arcpy.ListFields(layer_name)
for field in fields:
    print(f"{field.name} is a type of {field.type}")
```