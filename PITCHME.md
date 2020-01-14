---?image=https://www.outragegis.com/weather/img/animation/yesterday/LookRock.gif&opacity=40
# GEO 409
## Advanced topics in GIS
@snap[south-west span-20 text-italic text-04]
Great Smokies, yesterday
@snapend


---?image=https://www.outragegis.com/weather/img/animation/yesterday/PurchaseKnob.gif&opacity=40
## Managing complex workflows
### Module 01
@snap[south-west span-20 text-italic text-04]
Great Smokies, yesterday
@snapend



---?image=https://live.staticflickr.com/65535/49373904012_3e6813174b_h.jpg&opacity=30
## The challenge
@ul[squares]
* GIS and information-intensive projects have many assets that sprawl across directories.
* We'll download a lot of data.
* We'll write code to process it.
  * Code is unique (back it up)
  * Downloaded data is redundant (don't back it up)
* Own your assets...
* or they will haunt you...
@ulend



---?image=https://live.staticflickr.com/1821/42233874915_b274295437_o.jpg&opacity=40
## Where did it go?


---?image=https://live.staticflickr.com/65535/48789211076_36cf732bc6_h.jpg
## Topics
@ul[squares]
1. Set up our local workspace
2. Tools for the knowledge worker
  * Code editor
  * Git version and backup control
3. Create and run our first program
4. Challenge: measure area old school
@ulend

---
# I. Local
## workspace

---
## Data hygiene
@ul[squares]
* Create single top-level directory for all projects, data, etc.
  * We call this our *root* GIS directory
  * E.g., C:\BoydsGIS
* Put projects in well-named folders inside this folder
  * Use only alphanumeric characters and no spaces
* Separate *downloaded* from *created* assets
@ulend

---
## Example folder structure

---?image=images/02/a001.png&opacity=100

---
## Repo?
A *repository* ("repo") is a special project that we synchronize and backup on a remote server. More about this soon.

---
### File naming conventions
@ul[squares]
* Name should explain contents, author, metadata, etc.
* Always use a file extension, e.g., myPictureGrayscale.jpg
* No spaces; replace with hyphen, underscore, or use "camelCase"
* If need to sort by date, add date in format of YYYYMMDD
* Be descriptive and consistent!
* How the [Smithsonian does it](https://library.si.edu/sites/default/files/tutorial/pdf/filenamingorganizing20180227.pdf)
@ulend

---
# II. Tools 
## for the knowledge worker

---
### We need to
## manage text
## ✏️📓🎓


---
## as code
### plain-text instructions
that have *keywords* and *syntax*

---
## For example

---
This code is a well-formed "sentence"
```html
<p style="color:blue;">Hello, world!</p>
```
---
renders to:
<p style="color:blue;">Hello, world!</p>

---
or this...
```py
print("Hey, Geography Y'all!") #Print it to the terminal!
```

---
### Advantages of coding
@ul[squares]
* Work simply
* Work remotely
* Work when you sleep 🌝
* Share exact instructions
@ulend



---
# Text editor
🚫**Not** Notepad, Microsoft Word, etc.🚫

---
## Benefits
@ul[squares]
* Language syntax highlighting
* Autocomplete as you write
* Open source with vibrant development communities
@ulend

---
## Editors
@ul[squares]
* [VS Code](https://code.visualstudio.com/docs/editor/codebasics) is free, open source 🔥
* [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html) a browser-based editor for Python (not really a full-fledged editor but it makes running Python very easy).
* Both installed in lab
@ulend

---
## Customize VS Code
1. Bling it up with themes!
2. Create working directory, our root
3. Pro tips: modify settings

---?image=images/a01.png&opacity=100
<h3 style="color:#eee;text-shadow: 2px 2px 4px #000;">Themes</h3>

---
#### Let's setup your local
## root GIS directory
In VS Code, open *View > Terminal*


---?image=images/02/q-002.png
### Or, Terminal > New Terminal

---
### Type in the terminal I

---
```bat
rem This is a comment in windows terminal
rem Change directory to top of C: drive
cd C:\
rem If you're not on C: drive execute
C:
```
@[1]
@[3]
@[5]

---
### Type in the terminal II

---
```bat
rem make a directory on C:
mkdir MyFunNameGIS
rem go into the new directory
cd MyFunNameGIS
```
@[2]
@[4]


---
### Example

---
```bat
rem make a directory on C:\
rem Create your COOL COOL name
mkdir BoydsGIS 
rem go into the new directory
cd BoydsGIS 
```
@[3]
@[5]

---
## How will I
### know all of these commands?!?

---?image=images/02/q-003.png&opacity=40
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Commands</h2>
<a href="http://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf" target="blank">cheat sheet</a>

---
# Add info
## about this space

---
# Markdown
"write using an easy-to-read and easy-to-write plain text format" and convert it to pretty web pages. <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet" target="blank">Cheat sheet</a>

---
## Add a README.md
A README.md is a Markdown formatted file that tells visitors about your project.

---?image=images/02/q-004.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Open Folder...</h2>

---?image=images/02/q-005.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Right-click...</h2>

---?image=images/02/q-006.png
<h2 style="color:#eee;text-shadow: 2px 2px 4px #000;">Preview</h2>

---
## Backup
What if we lost our text?

---
# Git
"Git is a version control system for tracking changes in computer files and coordinating work on those files among multiple people."

---  
[Git](https://git-scm.com/) was created by Linus Torvalds in 2005 for development of the Linux kernel, with other kernel developers contributing to its initial development.

---
Git is a
## DVCS
@ul[squares]
* Distributed
  * Local repo synched to remote repo ("the backup")
* Version control
  * Make "snapshots" of project
  * Create multiple versions by *branching* project
* System
  * Can scale to allow many collaborators
@ulend

---
![Git](images/02/git.png)    

In practice, [xkcd](http://xkcd.com/)


---
We'll use the Git hosting service
### GitHub
to store our remote repos and their desktop app to manage our projects.

---
Get account at [GitHub.com](https://github.com/) using your
### uky.edu
email address

---
### Our GitHub flow each lesson
@ul[squares]
* Find invitation to lesson in Canvas
* Accept invitation and _clone remote repository_
* _Commit_ changes as you work 
* _Push_ to remote when finished
* _Pull_ in changes that I request
@ulend




---
### Let's clone our lesson
## Repo
(use link in Canvas)

---?image=images/02/slides-00.png&opacity=100
---?image=images/02/slides-001.png&opacity=100
---?image=images/02/slides-002.png&opacity=100
---?image=images/02/slides-003.png&opacity=100
---?image=images/02/slides-03.png&opacity=100
---?image=images/02/slides-04.png&opacity=100
---?image=images/02/slides-05.png&opacity=100

---
## Sign in
### to GitHub 

---?image=images/02/q-007.png&opacity=100
---?image=images/02/q-010.png&opacity=100

---
## Workflow
### in Git repo


---?image=images/02/slides-02-01.png&opacity=100
---?image=images/02/slides-02-02.png&opacity=100
---?image=images/02/slides-02-03.png&opacity=100
---?image=images/02/slides-02-04.png&opacity=100
---?image=images/02/slides-02-05.png&opacity=100
---?image=images/02/slides-02-06.png&opacity=100
---?image=images/02/slides-02-07.png&opacity=100

---
## How to undo in Git
@ul[squares]
* Can undo almost anything
* GitHub Desktop
  * Before commit: **Discard Changes**
  * After commit: **Revert this Commit**
  * **Add file to .gitignore**
* More complex undos need to use command line ([Cheat sheet](https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/))
@ulend

---
# Tips
@ul[squares]
* Add @UKy-GIS to your GitHub.com profile information
* Always Fetch and pull remote changes before you start
* Commit and push often!
@ulend

---
# MEGA!!
@ul[squares]
* Create a folder outside of any repo to download data.
  * Create: c:/BoydsGIS/**data** folder
* Never store a repo inside another repo
* 100 MB limit in GitHub
* Data is redundant, code is unique
@ulend

---
# III. First Program

---
## Python
@ul[squares]
* Created by Guido van Rossum; released in 1991
* One of the most popular programming languages
* Designed to be easy to read and write
* Named after Monty Python; not a constrictor
@ulend

---
### Objective
@ul[squares]
* We'll cover enough to work in ArcGIS Pro
* Not a formal class in programming
* Watch these [short videos](https://www.py4e.com/lessons/intro) in *Python for Everybody*
@ulend

---
### Step 1
@ul[squares]
1. Create a file in VS Code called, "hello.py"
2. Open the file and add...
@ulend

---
### Step 2
```py
# Add the following line to the file.
print("Hey, Geography Y'all!")
# When finished, save it!
```

---
### Step 3
@ul[squares]
1. To use ArcGIS's Python we need to run a batch script
2. Open a terminal in VS Code
3. Copy and paste the following line and hit **Enter**
@ulend

---
### Step 4
```txt
C:\"Program Files"\ArcGIS\Pro\bin\Python\Scripts\proenv.bat
```

---
### Step 5
@ul[squares]
1. You should see `(arcgis)
2. Open a terminal in VS Code
3. Copy and paste the following line and hit **Enter**
@ulend


---
# IV. Challenge
If we have time, measure state area using [technology](https://gdal.org/) that's 20 years old.


---
### Create folder called
## _measure-states_
inside your lesson repo

---
## VS Code
@ul[squares]
* Open root GIS folder
* Open terminal
@ulend

---
## Create readme.md:
```md
# measure-states

Let's practice measuring state areas.

* [Downloads data on Canvas](https://uk.instructure.com/courses/1950078/modules)
* [Source on Natural Earth](https://www.naturalearthdata.com/downloads/)

```

---?image=images/02/natural-earth-download.jpg&opacity=40
## Download layer from Canvas
into your data folder

---
## In terminal type:
```sh
C:\\"Program Files"\\"QGIS 3.10"\OSGeo4W.bat
o-help
```

---
### Experiment with
## [ogrinfo](https://gdal.org/programs/ogrinfo.html) & [ogr2ogr](https://gdal.org/programs/ogr2ogr.html)
Libraries that support vector data manipulation.


---
### Create files called
## area.bat & info.bat
in VS Code

---
### Edit info.bat
@ul[squares]
* Display fields and summary info
* for Kentucky, Texas, Alaska.
* Command format:
  * `ogrinfo <options> <dataset>`
@ulend

---
```bat
rem Describe dataset
ogrinfo -so -al ^
 -where "name in ('Kentucky','Texas','Alaska')" ^
 c:\BoydsGIS\data\ne_10m_admin_1_states_provinces_lakes.shp
```
@[1]
@[2]
@[3]
@[4]

---
## Execute
@ul[squares]
* Save file
* In terminal, type: `info.bat`
* Errors?
  * Look for typos!
@ulend

---
## Variables
@ul[squares]
* Substitute data with variable names
* Put variables at top of script
* Variable substitution
@ulend

---
What can be converted to a variable and moved to top?
```bat
rem Describe dataset
ogrinfo -so -al ^
 -where "name in ('Kentucky','Texas','Alaska')" ^
 c:\BoydsGIS\data\ne_10m_admin_1_states_provinces_lakes.shp
```

---
```bat
rem set variables
set states='Kentucky', 'Texas', 'Alaska'
set data=c:\BoydsGIS\data\ne_10m_admin_1_states_provinces_lakes.shp

rem print them to the CLI
echo looking for %states% in %data%

rem Describe data
ogrinfo -so -al ^
 -where "name in (%states%)" ^
 %data%
```
@[1-3]
@[5-6]
@[8-11]

---
### Edit area.bat
@ul[squares]
* Calculate sq mi for our states
* Two steps
  1. Project layer
  2. Calculate fields
* Command format:
  * `ogr2ogr <output> <options> <input>`
@ulend


---
```bat
rem Create projected Shapefile
ogr2ogr projected.shp -sql ^
 "select name from ne_10m_admin_1_states_provinces_lakes where name in ('Texas','Alaska','Kentucky')" ^
 -s_srs EPSG:4326 -t_srs EPSG:5070 ^
 c:\BoydsGIS\data\ne_10m_admin_1_states_provinces_lakes.shp

```
@[1-2]
@[3]
@[4]
@[5]

---
```bat
rem Use ogr2ogr internal measurement feature
ogr2ogr output.csv -sql ^
 "select name, (ogr_geom_area/2.59e+6) as sq_mi from projected" ^
 projected.shp

```
@[1-2]
@[3]
@[4]


---
```bat
rem Delete intermediate files
del projected.*
```

---
### Save your
## project files
#### then commit and push!

---
## Add Variables
@ul[squares]
1. Create new branch in GitHub (Menu > Repository > New Branch).
2. Make sure VS Code is using new branch
3. Find solution (get [help](https://github.com/tastyfreeze/measure-states))
4. Save, commit, and publish branch
5. Create Pull Request and Merge
@ulend

---
## That's the
# Challenge
this semester and we'll keep at it!

---
## Compare
### to ArcGIS Desktop

---
## Measure state areas in
# ArcMap

---
## Change your Data Frame's
# Projection

---?image=images/02/arcmap-projection.jpg&opacity=40
<h2 style="color:#111;text-shadow: 2px 2px 4px #eee;">EPSG: 5070</h2>


---
## Select three states
@ul[squares]
* We want only Alaska, Texas, and Kentucky
* How do we do it?
@ulend


---
```sql
"name" in ('Texas','Alaska','Kentucky')
```

---?image=images/02/arcmap-definition-query.jpg&opacity=100
<h2 style="color:#111;text-shadow: 2px 2px 4px #eee;"></h2>


---
## Open attribute table
# Add Field
as **Type: Float**

---?image=images/02/arcmap-add-field.jpg&opacity=100
<h2 style="color:#111;text-shadow: 2px 2px 4px #eee;"></h2>

---
## Right+click
# Field
and **Calculate Geometry**

---?image=images/02/arcmap-area.jpg&opacity=100
<h2 style="color:#111;text-shadow: 2px 2px 4px #eee;"></h2>


---
## ArcMap mesaurement

```
name,       area_sq_km
Alaska,     1496210
Texas,      685531
Kentucky,   104525
```

---
## Addendum

---
### History
* Command Line Interface (CLI)
* Many applications have command line interface
* CLI is hot again

---
[Do anything with the CLI](https://geekprank.com/hacker/)


---
## Modify settings
### In VS Code
Open *File > Preferences > Settings > Edit in settings.json*


---
### After installing ArcGIS Pro
### Copy and paste:
```json
{
    // After you install ArcGIS Pro, add the next three lines
    // "terminal.integrated.shell.windows": "C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\Scripts\\proenv.bat",
    // OSGeo tools from QGIS - Add after installing QGIS
    // "terminal.integrated.shell.windows": "C:\\Program Files\\QGIS 3.8\\OSGeo4W.bat", 
    "editor.fontSize": 17,
    "editor.lineHeight":25,
    "terminal.integrated.fontSize": 18,
    "terminal.integrated.lineHeight": 1.05,
}
```



---?image=images/02/heat-trees.png
@snap[south-west span-20 text-italic text-04]
[Link](https://www.npr.org/2019/09/03/754044732/as-rising-heat-bakes-u-s-cities-the-poor-often-feel-it-most)
@snapend