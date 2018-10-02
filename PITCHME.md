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
## Objectives
* Create script to quickly process data for mapping
* Learn more Python!
* Finish draft of base map

#HSLIDE?image=https://farm2.staticflickr.com/1978/44221432854_c4570602c1_h.jpg

#HSLIDE
## Lab 3
* Your commit log shows how much work you're doing
* 19 commits v 1 commit
* commit often, perfect later
* <a download src="assets/lab-03-practice.ipynb">More practice</a>

#HSLIDE
## Functions
* Block of statements that execute when called
* Might take arguments
* Might return data

#HSLIDE
```python
# function with two parameters
function(x, y)
# parameters are 'placeholders' for passing arguments
```

#HSLIDE
## Define function
* Store and reuse statements
* Need unique name followed by `():`
* Inputs?
* Indent function body four spaces


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
## Built-in functions
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
# What!?!

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
* 38.038015, 0-84.5046852!
* 1&deg; of lattitude = 69 miles
* 1.0&deg;  6.9 mi of precision
* 1.00&deg;  3600 ft
* 1.000&deg;  360 ft
* 1.0000&deg;  36 ft
* 1.000000&deg;  4 in

#HSLIDE
## Jupyter Notebook
* Open workbook for lesson
* Work through challenges


#HSLIDE
## Objects and methods
* Every object has a value, identity, and type
* Methods are functions that operate on certain objects
	* object.function()


#HSLIDE?
```python
# same value, different type and identity
1 == 1.0 # true
1 is 1.0 # false

# methods on float type
x = 1.0
x.is_integer() # true
```

#HSLIDE
## String methods more common
* Perform common tasks on strings
* Find substrings, change case, etc.
* [Built-in methods](https://www.w3schools.com/python/python_ref_string.asp)
* Always returns new values

#HSLIDE
## String indexes
* Sequence of characters have positions in string starting at zero.
* Bracket notation to show position.
```python
"Hello World!"[0] # returns H
```

#HSLIDE
## String slice
* Access substring using start:end indexes
* End index is up-to-but-including
* Address in string v. length of string

#HSLIDE
```python
len("Hello World!") # returns 12
"Hello World!"[0] # returns H
"Hello World!"[11] # !
"Hello World!"[0:12] # returns all
"Hello World!"[12] # returns error
```

#HSLIDE
## String index challenge
Print the arch variable backwards using only string indexes

#HSLIDE
## while loop
* Runs while true
* Avoid infinite loop with breaks
* loop body indented with four spaces


#HSLIDE
```python
arch = "Grays Arch"
while "Natural Bridge" not in arch:
    print("Crash this program")
# No!
```

#HSLIDE
```python
length_of_word = len(arch)
i = 0
while i < length_of_word:
    print(arch[i])
    # What's missing?
```

#HSLIDE
## while loop challenge
Create a while loop that runs until a correct state name is input

#HSLIDE
## for loop
* Iterates through a list, value by value.
* Indented four spaces
* Runs a definite number of times


#HSLIDE
```python
# We need to create a list first.
# Assume we have a much, much large string than this
place = "Welcome to the lost treasures of Silvermine Arch and Hidden Arch in Wolfe county!"

# Split a string into list on each space in string
listOfWords = place.split(" ") # returns 14 words

# print the contents of listOfWords
print(listOfWords) # use the print function to see how it works
```

#HSLIDE
## for loop challenge
Scan text and print the names of the arches in the text.

#HSLIDE?image=https://farm2.staticflickr.com/1901/44221426354_d8a711a753_h.jpg

#HSLIDE
## Lesson addendum
* `import csv` module
* iterate through `arches.csv`


#HSLIDE 
## Lab practice
* Refactor script from lab 2
* Create hillshade script

#HSLIDE
```python
# build field data type showing properties of us_arches fields.
fields = arcpy.ListFields(layer_name)
for field in fields:
    print(field.name + " is a type of " + field.type)
```