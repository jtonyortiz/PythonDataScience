## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500[["rank", "revenues", "revenue_change"]].head(5)

## 2. Reading CSV files with pandas ##

import pandas as pd
f500 = pd.read_csv("f500.csv")
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##

fifth_row = f500.iloc[4]
company_value = f500.iloc[0,0]