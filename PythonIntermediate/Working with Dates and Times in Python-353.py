## 1. Introduction ##

from csv import reader
opened_file= open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]


## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt

ibm_founded = dt.datetime(1911, 6, 16)

man_on_moon = dt.datetime(1969, 7, 20, 20, 17)