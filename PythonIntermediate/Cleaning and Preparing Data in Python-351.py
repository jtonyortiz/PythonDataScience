## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)


## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here

opened_file = open('artworks.csv')

read_file = reader(opened_file)

moma = list(read_file)

moma = moma[1:]

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace("thirty-one", "thirty-two")

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(", "")
    nationality = nationality.replace(")", "")
    row[2] = nationality
    
    
    
    gender = row[5]
    gender = gender.replace("(", "")
    gender = gender.replace(")", "")
    row[5] = gender
    
 

## 5. String Capitalization ##

for row in moma:
    gender = row[5]
    gender = gender.title()
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender
    
    nationality = row[2]              #Assign to row index 2
    nationality = nationality.title() #Place an uppercase value on the natioality
    if not nationality:               #If "", then replace the string with "Natioality Unknown"
        nationality = "Nationality Unknown"
    row[2] = nationality              #Assign the new string value back to the column
    
    

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

#Iterate through the rows in moma:
for row in moma:
    #Assign row 3 and row 4 to begDate, and endDate 
    begDate = row[3]
    endDate = row[4]
    #Clean and convert the two values:
    begDate = clean_and_convert(begDate)
    endDate = clean_and_convert(endDate)
    
    #Assign the converted values back to indexes 3, and 4:
    row[3] = begDate 
    row[4] = endDate


## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string_):
    for char in bad_chars:
        string_ = string_.replace(char, "")
    
    return string_


stripped_test_data = []             #Create an empty list
for s in test_data:                 #Iterate through test_data list 
    s = strip_characters(s)         #Call function to strip chars from the strings in the list:
    stripped_test_data.append(s)    #Append these cleaned strings to the empty list:
    
print(stripped_test_data) #print this new list:

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(date):
    if "-" in date:
        split_date = date.split("-")
        date_one = int(split_date[0])
        date_two = int(split_date[1])
        date = (date_one + date_two) / 2
        
        date = round(date)
        
    else:
        date = int(date)

    return date
        
    
processed_test_data = []

for n in stripped_test_data:
    date = process_date(n)
    processed_test_data.append(date)
    
    
for row in moma:
    dte = row[6]
    dte = strip_characters(dte)
    dte = process_date(dte)
    row[6] = dte