# Coding Interview
Use the file transformation.py 


## First part
1. read in all 10:00 files, which do not end on "_summe"
2. concatenate columns for "Enerparc" and "sunnic_extern"
3. rename columns
   * timestamp column -> "dt_start"
   * rename park columns "Leistung XXX" -> "XXX" (remove "Leistung ")
4. save file in "data/output" as "combined_YYYYmmdd_HHMM.csv" (example: combined_20220208_1000.csv")



<details>
  <summary>Click to expand!</summary>
  
## Second part

1. read in files for 10:30
2. prepare them in the same way as for 10:00
3. add new rows to existing combined file
</details>