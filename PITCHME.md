---?image=https://www.outragegis.com/weather/img/animation/yesterday/LookRock.gif&opacity=40
# GEO 409:04
## Advanced data structures & intro to ArcPy

---
## Crossing the bridge
@ul[squares]
* From Python fundamentals
* to ArcPy, ESRI's Python site package.
@ulend

---
## Lab 3
@ul[squares]
* More Python calisthenics 🏃‍♀️🏋️🧐
* Impressed with your dedication!
* Recognize that scripting an application has a flow.
    * You may not know how everything works, but you know how to set local variables.
@ulend

---
### Example application

```py
# Import tools
import xyz
# Set local parameters
workspace = "myHuckleberry"
buffer = 1000 # units?
# The application body
myFunction(input, output, buffer)
```
@[1-2]
@[3-5]
@[6-7]

---
## Lab 4
@ul[squares]
* Explore new data formats 
* Finish the Python drills 
    * Recognize fundamental stuff
* Intro to ArcPy's highly abstracted tools
    * 🚂 vs 📐. Tools already built. Give ticket & itinerary.
@ulend

---
## Implications
@ul[squares]
* Functions can have many parameters
    * Reading documentation required
* ⛓️Chaining functions together 
    * What to do with intermediate data?
@ulend

---
```py
# Import tools
import arcpy
# Set local parameters
workspace = "myHuckleberry"
# The application body
myFuncOne(inData, outData1, a, b, c, {x}, {y}, {z})
myFuncTwo(outData2, outFinal, i, j, {k})
```
@[1-2]
@[3-4]
@[5-7]

---
## Model Builder?

![Model Builder](https://www.arcgis.com/sharing/rest/content/items/04d37668a2d745e8a17b3366ea8dedd2/resources/1573037919202.png)

---
## Lab 4: Application
Find areas within some distance of selected GNIS features. 1) Jupyter Notebook processing then 2) 🔥up ArcGIS Pro to view data!

---
## Outline
@ul[squares]
* Collections
    * types 
    * methods
* Application
    * `arcpy.Exists()`
    * `arcpy.CreateFileGDB()`
    * `arcpy.XYTableToPoint()`
    * `arcpy.Buffer()`
@ulend

---
## Collections
@ul[squares]
* Ordered vs. unordered
* mutable vs. immutable
* Nested collections (collection of collections)
* Looping through collections
@ulend

---
## Videos
@ul[squares]
* Collections of data
* Watch videos!
    * [lists](https://www.py4e.com/lessons/lists)
    * [tuples](https://www.py4e.com/lessons/tuples)
    * [dictionaries](https://www.py4e.com/lessons/dictionary)
@ulend

---
## List
An mutable, **sequence** of **items** or **elements** separated by a comma and enclosed in square brackets. Items can be any value.

---
```python
archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch'] 
```

---
### Index bracket notation
Address items in sequence with integer, just like strings.


---
```py
myList[item]
# where item is an integer
```

---
```python
# archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch'] 
n = 0
for i in archesList:
    print(i)
    print(archesList[n])
    n += 1
```

---
### Add items
```python
archesList[3]= "Rainbow Arch"
# ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch', "Rainbow Arch"] 
```

---
### Change items
```python
archesList[3]= "Sky Bridge"
# ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch', "Sky Bridge"] 
```

---
### Nested collections
Because lists can contain any type, you can have lists inside lists. Gang together brackets to access nested collection.


---
```py
myList[outerItem][innerItem]
# where outerItem and innerItem are integers
```

---
```py
archCoords = [[37.7873, -83.6243], [37.8123, -83.5796], [37.7686, -83.5582]]
```

---
```python
# archCoords = [[37.7873, -83.6243], [37.8123, -83.5796], [37.7686, -83.5582]]
n = 0
for i in archCoords:
    print(i)
    print(archesList[n])
    print(archesList[n][0])
    print(archesList[n][1])
    n += 1
```


---
### List methods
Changes source list
```py
.sort() # alphabetically
.append() # add one element
.extend() # add elements from one iterable
.remove() # remove first occurrence
```

---
### `.sort()`
Alphabetize elements in list
```py
# archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
archesList.sort() 
# ['Castle Arch', 'Rock Bridge Arch', 'Silvermine Arch']
archesList.sort(reverse=True)  # keyword argument
# ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
```

---
### `.append()`
One argument. Adds element to end of list
```py
# archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
archesList.append('Grays Arch') 
# ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch', 'Grays Arch']
```

---
### `.extend()`
One argument: an iterable. Adds element(s) to end of list
```py
# archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
archesList.extend(['Grays Arch', 'Natural Bridge']) 
# ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch', 'Grays Arch', 'Natural Bridge']
```

---
### Useful list functions
Returns a value
```py
len() # number of elements in the list
range() # range of index values
```

---
### `len()`
Returns number of characters in string or elements in list
```py
# archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
x = len(archesList)
print(x) 
# 3
```

---
### `range()`
Returns sequence of numbers (over which to iterate)
```py
for i in range(6):
    print(i)
for i in range(len(archesList)):
    print(i, archesList[i])
```

---
## Challenge: 
### iterate over each word and letter in the following sequence
```py
archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
```

---
## Challenge: 
### combine, sort, and report on arch names and locations
```py
archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
archCoords = [[37.7873, -83.6243], [37.8123, -83.5796], [37.7686, -83.5582]]
```

---
## Challenge: 
### Sort by west to east
```py
archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
archCoords = [[37.7873, -83.6243], [37.8123, -83.5796], [37.7686, -83.5582]]
```

---
## Solutions

---
```py
archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
for i in range(len(archesList)):
    for j in range(len(archesList[i])):
        print(j, archesList[i][j])
```

---
```py
aList = []
archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
archCoords = [[37.7873, -83.6243], [37.8123, -83.5796], [37.7686, -83.5582]]
n = 0
for i in archesList:
    aList.append([i, archCoords[n]])
    n += 1
print(aList)
```

---
```py
aList = []
archesList = ['Silvermine Arch', 'Castle Arch', 'Rock Bridge Arch']
archCoords = [[37.7873, -83.6243], [37.8123, -83.5796], [37.7686, -83.5582]]
n = 0
for i in archesList:
    aList.append([[archCoords[n][1], archCoords[n][0]], i])
    n += 1
aList.sort(reverse=True) # reverse needed?
print(aList)
```

---
## Tuple
An immutable sequence of values separated by a comma and enclosed in round brackets

---
```python
oneArchTuple = ('Silvermine Arch', [37.7873, -83.6243])
```

---
```python
oneArchTuple = ('Silvermine Arch', [37.7873, -83.6243])
oneArchTuple[0] = "Castle Arch" # Blows up!
oneArchTuple[1][0] = 37.112 # 😀
```

---
### Unique assignment
Tuple on the left side of an assignment statement
```py
aList = ['Silvermine Arch', 'Castle Arch']
(x, y) = aList # or x, y = aList
print(x, y) # Silvermine Arch Castle Arch
```

---
### Tuple unpacking
```py
archCoords = [[37.7873, -83.6243], [37.8123, -83.5796], [37.7686, -83.5582]]
for x, y in archCoords:
    print(y, x)
```

---
## Dictionary
An unordered collection of **items** stored as key:value pairs separated by a comma and enclosed in curly brackets

---
```python
archesDictionary = {
 'Castle Arch': [37.8123, -83.5796],
 'Red-byrd Arch': [37.8148, -83.5504],
 'Rock Bridge Arch': [37.7686, -83.5582],
 'Silvermine Arch': [37.7873, -83.6243]
 }
```

---
### Iterate through dictionary
```python
for i in archesDictionary:
    print(i, archesDictionary[i])
```

---
### Iterate just keys
```py
for k in archesDictionary.keys():
    print(k)
```

---
### Iterate just values
```py
for v in archesDictionary.values():
    print(v)
```
---
### Iterate each item with key:value as tuple
```py
for i in archesDictionary.items(): # returns tuple of items!
    print(i)
```

---
## Challenge
### In two lines, print the value:key in
```py
archesDictionary = {
 'Castle Arch': [37.8123, -83.5796],
 'Red-byrd Arch': [37.8148, -83.5504],
 'Rock Bridge Arch': [37.7686, -83.5582],
 'Silvermine Arch': [37.7873, -83.6243]
 }
```

---
## Challenge
Most common character in
```py
spring = """
I've banished Winter, saith the Spring,
Awake! arise, ye flowers!
Brisk breezes blow,
Bright sunshine glow,
And rouse the young Year's powers.
"""
# -Henry James Slack (1818–1896)
```

---
### Hint
```py
myDict = {}
for letter in spring:
    # create new keys and values
    myDict[letter] = 1
print(myDict)
# Missing keys!!!
```

---
### Hint `.get(key, "default value")`
If key exists, will return value
If key doesn't exist, will add default value

---
### Hint
```py
myDict = {}
for letter in spring:
    # create new keys and values
    myDict[letter] = myDict.get(letter,0) + 1
print(myDict)
# Missing keys!!!
```

---
## Solutions

---
```py
for k, v in archesDictionary.items(): # returns tuple of items!
    print(v, k)
```

---
```py
lettersInWord = {} # create empty dict
for letter in spring:
    # create new key:values based on occurrence of letter
    lettersInWord[letter] = lettersInWord.get(letter,0) + 1
print(lettersInWord)
```

---
```py
letterCount = []
for k, v in lettersInWord.items():
    letterCount.append([v, k])
letterCount.sort(reverse=True)
print(letterCount)
```

---
### Wheel of Fortune analysis!
Pick spaces??



---
## Advantages of each?
@ul[squares]
* Lists are easy to search/build
* Tuples are fast to access
* Dictionaries are so tidy!
@ulend

---?image=https://live.staticflickr.com/65535/33813132438_2c62d8c92b_k.jpg&opacity=100
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Application</h3>
@snap[south-west]
<p style="color:#FFD27F;text-shadow: 2px 2px 4px #000;"><i>Sky Bridge</i></p>
@snapend

---
@quote[Everything is related to everything else, but near things are more related than distant things.](Tobler's first law of geography)

---
### Find *areas* within *distance* of *selected* features.

---
### How do we do *that*?

---
### Assuming no barriers (like rivers) create polygon about feature.

---?image=https://pro.arcgis.com/en/pro-app/tool-reference/analysis/GUID-267CF0D1-DB92-456F-A8FE-F819981F5467-web.png&opacity=100

---
### Buffer
ArcGIS Pro [tool documentation and syntax](https://pro.arcgis.com/en/pro-app/tool-reference/analysis/buffer.htm)

---
# 🛎️
## Look up all tools
E.g., Google the following phrase "arcpy buffer"    
@ul[squares]
* Why arcpy?
@ulend

---
## ArcPy
@ul[squares]
* Python site package for geospatial applications
* Published by ESRI and ships with ArcGIS Pro
* ESRI's [What is ArcPy?](https://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-arcpy-.htm)
@ulend

---
### Using ArcPy
Add to first cell in Jupyter Notebook with all other import statements.
```py
import arcpy # lower case
# that's it!
```

---
## Geoprocessing overview
@ul[squares]
* Get data
* Project data (if necessary)
* Analyze data
* View 📍🗺️📊📈
@ulend

---
### Get data
@ul[squares]
* [GNIS database](https://www.usgs.gov/core-science-systems/ngp/board-on-geographic-names/download-gnis-data) of place names and locations
* Lab 2 script to filter and export CSV file

@ulend

---
### Store data
@ul[squares]
* Most of the data used in arcpy will be stored in a **file geodatabase**
    * a folder with a *.gdb* extension
* Create the database if doesn't exist
* Convert CSV to ArcPy **feature class**
    * a collection of geographic features that share the same geometry type and attributes
    * e.g., a layer of points, lines, or polygons
@ulend

---
### Project data
@ul[squares]
* The CSV data uses spherical coordinates (lat, long)
* We need to transform to Cartesian coordinates (plane coordinates)
* Define and use the official KY CRS, EPSG: 3089
* All data will be in this CRS before analysis
    * Luckily, most of data is already in this CRS (after this lab).
@ulend

---
### Analyze data
@ul[squares]
* Create chain of [geoprocessing](https://desktop.arcgis.com/en/arcmap/latest/analyze/main/what-is-geoprocessing.htm) tools
* This exercise uses one tool, buffer, to perform a [proximity analysis](https://desktop.arcgis.com/en/arcmap/latest/analyze/commonly-used-tools/proximity-analysis.htm)
* Classic example: Dr. John Snow's 1854 analysis of London cholera epidemic
@ulend

---?image=https://open.lib.umn.edu/app/uploads/sites/178/2017/07/Image100.jpg&opacity=100

---
## Application overview
@ul[squares]
* Jupyter Notebook cells
    1. `import` statements
    2. set local variables
        * 🛎️ Only edit this cell!
    3. remaining cells perform geoprocessing
@ulend

---
### Environment settings
@ul[squares]
* ArcPy's default settings
    * E.g., tool output can overwrite existing data?
* Exposed as properties on [ArcPy's env class](https://pro.arcgis.com/en/pro-app/arcpy/classes/env.htm).
    * arcpy.env.[propertyName] = [some value]
@ulend

---
### Environment settings
@ul[squares]
* Two are important to always set
* `arcpy.env.workspace` = [file/path/to/gdb]
* `arcpy.env.overwriteOutput = True`
@ulend

---
### Follow along
@ul[squares]
* In the lesson, find the section, "Application: Finding areas within a distance of selected features with ArcPy"
* Open the Jupyter Notebook **lab-04/Lab-04-application.ipynb**
@ulend


---?image=https://live.staticflickr.com/4023/35739307185_4c4ffc805b_k.jpg&opacity=100
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Spring break is almost here!</h3>
@snap[south-west]
<p style="color:#FFD27F;text-shadow: 2px 2px 4px #000;"><i>Jump rock</i></p>
@snapend

---
## Addendum: Pandas 
A DataFrame is a two-dimensional tabular data structure and the primary data structure for pandas.

```python
import pandas as pd

with open("KY_Features_20181001.txt", encoding='utf-8') as csvfile:
    reader = pd.read_csv(csvfile, delimiter='|')
    pdData = pd.DataFrame(reader)

print(pdData)
```


