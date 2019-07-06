## 1. Reading CSV Files with Encodings ##

import pandas as pd
laptops = pd.read_csv("laptops.csv", encoding="Latin-1")
laptops.info()

## 2. Cleaning Column Names ##

new_columns = []

for c in laptops.columns:
    clean_c = c.strip()
    new_columns.append(clean_c)

laptops.columns = new_columns
    

## 3. Cleaning Column Names Continued ##

import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')

def cleanString(strng):
    strng = strng.strip()
    strng = strng.replace("Operating System", "os")
    strng = strng.replace(" ", "_")
    strng = strng.replace("(", "")
    strng = strng.replace(")", "")
    strng = strng.lower()
    return strng

new_columns = []
for c in laptops.columns:
    clean_c = cleanString(c)
    new_columns.append(clean_c)
    
laptops.columns = new_columns
print(laptops.columns)
    
    
    