# Coding Interview
Use the file transformation.py 

# Python
## Class questions
Have a look at `class_questions.py`

## Coding Task
### First part
1. read in all 10:00 (*_1000\*) files from data/input/, which do not end on "_summe"
2. concatenate data for "Enerparc" and "sunnic_extern" column-wise
3. rename columns
   * timestamp column -> "dt_start"
   * park columns "Leistung <park name>" -> "<park name>" (remove "Leistung ")
4. save file in "data/output" as "combined_YYYYmmdd_HHMM.csv" (example: combined_20220208_1000.csv")



### Second part
<details>
  <summary>Click to expand!</summary>
  
This task shall be repeated every 30 minutes for new files.

Change your code so that you can generalize the operation and the following steps can be done by the same code. 
1. read in files from data/input/ for 10:30
2. prepare them in the same way as you did for 10:00-files
3. add new rows to existing combined file 
4. overwrite existing combined file with updated timestamp in the filename
</details>

# UML
Draw a class diagram representing a car, wheels, seats, driver & passengers.

You can use the white board or the provided car.puml 
