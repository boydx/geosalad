---
# GEO 409:04
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

---?image=https://outragegis.com/gorge/animations/sun.gif&opacity=100

---
## Objectives
@ul[squares]
* Create script to quickly process data for mapping
* Learn more Python!
* Finish draft of base map
@ulend

---?image=https://farm2.staticflickr.com/1978/44221432854_c4570602c1_h.jpg&opacity=100

---
## Lab 3
@ul[squares]
* Your commit log shows how much work you're doing
* 19 commits v 1 commit
* commit often, perfect later
@ulend


---
## Functions
@ul[squares]
* Block of statements that execute when called
* Might take arguments
* Might return data
@ulend

--- 

```python
print("Hello World!")
w = "Hello Universe!"
print(w)
```

---
```python
# function with two parameters
function(x, y)
# parameters are 'placeholders' for passing arguments
```

---
## Define function
@ul[squares]
* Store and reuse statements
* `def` keyword defines a function
* followed by unique name and `():`
* Function inputs?
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
	print(int(x) + int(y)) # prints to screen
	return z # when executed, function becomes this

powersXtoY(2,4) # Need documentation!
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
## Built-in functions
@ul[squares]
* Python comes with about [60 functions](https://docs.python.org/3.6/library/functions.html)
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
* Python's sprawling [standard library](https://docs.python.org/3/library/)
* Adds new functions and data types
* The `decimal` module to correctly round numbers

---
```python
import decimal # use the module's namespace to access its functions
x = decimal.Decimal('7.555')

from decimal import * # access the module functions directly
x = Decimal('7.555')
```

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
## Jupyter Notebook
* Open workbook for lesson
* Work through challenges


---
## Objects and methods
* Every object has a value, identity, and type
* Methods are functions that operate on certain objects
	* object.function()


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
## String methods more common
@ul[squares]
* Perform common tasks on strings
* Find substrings, change case, etc.
* [Built-in methods](https://www.w3schools.com/python/python_ref_string.asp)
* Always returns new values
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
"Hello World!"[12] # returns error
```

---
## String index challenge
Print the arch variable backwards using only string indexes

---
## while loop
* Runs while true
* Avoid infinite loop with breaks
* loop body indented with four spaces


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
    print(field.name + " is a type of " + field.type)
```