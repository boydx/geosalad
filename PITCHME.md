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
### add, sort, and report on arch names and locations


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
## Dictionary
An unordered collection of items stored as key:value pairs separated by a comma and enclosed in curly brackets

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
```python
for i in archesDictionary:
    print(i, archesDictionary[i])
```

---
## Advantages of each?
@ul[squares]
* Lists are easy to search/build
* Tuples are fast to access
* Dictionaries are so tidy!
@ulend

---
## DataFrame
A two-dimensional tabular data structure and the primary data structure for pandas. NOT a built-in data type.

```python
import pandas as pd

with open("KY_Features_20181001.txt", encoding='utf-8') as csvfile:
    reader = pd.read_csv(csvfile, delimiter='|')
    pdData = pd.DataFrame(reader)

print(pdData)
```

---
### Exercise using lists and tuples
### Sort arches by name and elevation
Download [US GNIS (or US)](https://uk.instructure.com/courses/1950078/modules) from Canvas

---
```python
import csv #module to handle csv files
with open("KY_Features_20181001.txt", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter="|")
    for row in reader:
        print(row)
```

---
### [Help with Lab 6](https://github.com/UKy-GIS/uky-gis.github.io/tree/master/support/python-arcgis/examples)

---?image=images/skybridge-3.jpg&size=contain&color=linear-gradient(to top, #000, #333)
@snap[north-west text-italic text-18]
Cliffs along Red River
@snapend

---?image=images/skybridge-4.jpg
<h3 style="color:#FFD27F;text-shadow: 2px 2px 4px #000;">Sky Bridge</h3>
