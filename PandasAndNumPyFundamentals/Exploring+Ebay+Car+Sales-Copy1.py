#!/usr/bin/env python
# coding: utf-8

# # Exploring Ebay Car Sales Data
# 
# ## Description:
# In this guided project, I will work with a dataset of used cars from <i>ebay Kleinanzeigen</i> a section of the German eBay website.
# 
# The dataset was originally scraped and uploaded to Kaggle, you can visit it here:
# 
# A few modifications have been made to the dataset, as follows:
# -50,000 data points were sameples from the full dataset
# 
# -The dataset has been given dirty values to help understand what to expect in a scraped dataset.
# 
# The data dictionary is as follows:
# 
# - dateCrawled: When this ad was first crawled. 
# All field-values were taken from this date.
# - name: Name of the car.
# - seller: Whether the seller is private or a dealer.
# - offerType: The type of listing
# - price: The price on the ad to sell the car.
# - abtest:Whether the listing is included in an A/B test.
# - vehicleType: The vehicle Type.
# - yearOfRegistration: The year in which the car was first registered.
# - gearbox: The transmission type.
# - powerPS: The power of the car in PS.
# - model: The car model name.
# - kilometer: How many kilometers the car has driven.
# - monthOfRegistration: The month in which the car was first registered.
# - fuelType: What type of fuel the car uses.
# - brand: The brand of the car.
# - notRepairedDamage: If the car has a damage which is not yet repaired.
# - dateCreated: The date on which the eBay listing was created.
# - nrOfPictures: The number of pictures in the ad.
# - postalCode: The postal code for the location of the vehicle.
# - lastSeenOnline: When the crawler saw this ad last online.
# 
# ## Purpose:
# The aim of the project is to be able to clean the data and analyze the included car listing. We will also look in better detail some of the benefits that jupyter notebook has for those who work with pandas.
# 
# So lets begin, by importing the libraries we need, and reading the dataset into pandas.
# 
# 

# In[2]:


import pandas as pd
import numpy as np

autos = pd.read_csv("autos.csv", encoding='Latin-1')




# In[3]:


#Lets run "autos" as a cell, we should see some output of our dataset below:
autos


# Next we will use `DataFrame.info()` and `DataFrame.head()` to print information about the `autos` dataframe, and the first few rows:

# In[4]:


autos.info()


# In[5]:


autos.head(5)


# In the information extracted we can see that:
# - The number of entries is arranged from `0-49999` (`50,000` total).
# - Some of the attributes of the dataframe are objects, and some are actually int values.
# - There are 20 data columns in total within this dataset.
# - The `.head()` function takes in an int value and displays the first "n" values of the dataset.
# - The `.info()` function gives us insight of the datatypes used in the dataset, and how the data is arranged.

# ## Cleaning Column Names
# Now that we know what is in the data set, lets begin by cleaning some of the column names for readability.
# 
# To begin, lets revisit the columns that we have in our present dataset though the `.columns` attribute:

# In[6]:


autos.columns #Useing the .columns attribute to print all column names:


# Note that all of the columns use camelcase.. (example: offerType)
# 
# Lets change that! Instead of the useing a capital letter after every new word in the column's name, lets instead use an underscore to divide the two words (that is, instead use `offer_type` instead of `offerType`).  

# In[7]:



#An explicit assignment for snake_case:
autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price',
                'ab_test', 'vehicle_type', 'registration_year', 'gearbox', 
                'power_PS', 'model', 'odometer', 'registration_month', 
                'fuel_type', 'brand', 'unrepaired_damage', 'ad_created',
                'num_photos', 'postal_code', 'last_seen']

#Now, lets see the results:
autos.head()


# ## Exploration and Cleaning
# 
# Now let's do some basic data exploration to determine what other cleaning tasks need to be done. In this section, we will look for: 
# 
# - Text columns where all or almost all values are the same. These can often be dropped as they don't have useful information for analysis. 
# 
# - Examples of numeric data stored as text which can be cleaned and converted.
# 
# Lets begin by looking at some descriptive statustics with the use of the function `DataFrame.describe()` with the option `include='all'`to obtain both categorical and numeric columns.
# 

# In[8]:


#Lets try useing .describe() with include='all' option
autos.describe(include='all')


# 
# 
# Our initial observations:
# 
# There are a number of text columns where all (or nearly all) of the values are the same:
# - seller
# - offer_type
# 
# The `num_photos` column looks odd, and we will look into investigating this further.
# 
# 

# In[9]:


autos["num_photos"].value_counts()


# Since `num_photos` has just zeros for the column, lets drop it from the data table.

# In[10]:


autos = autos.drop(["num_photos", "seller", "offer_type"], axis=1)


# Note also that there are two columns (price and odometer) that have numeric values stored as text, as well as abbreviations. 
# We can fix these useing a set of commands:

# In[11]:


autos["price"] = (autos["price"].str.replace("$", "")
                  .str.replace(",", "")
                   .astype(int))

autos["price"].head()


# In[12]:


autos.rename({"odometer":"odometer_km"}, axis=1, inplace=True)


# In[13]:


autos["odometer_km"].head()


# ## Exploring Odometer and Price Columns
# 
# Let's continue exploring the data, specifically looking for data that doesn't look right. We'll start by analyzing the `odometer_km` and `price` columns. Here's the steps we'll take:
# 
# - Analyze the columns using minimum and maximum values and look for any values that look unrealistically high or low (outliers) that we might want to remove.
#     
# __We'll use:__
# - `Series.unique().shape` to see how many unique values
# - `Series.describe()` to view min/max/median/mean etc
# - `Series.value_counts()`, with some variations:
# 
# - chained to `.head()` if there are lots of values.
#            
# - Because `Series.value_counts()` returns a series, we can use
#            
# - `Series.sort_index()` with ascending= True or False to view the 
#     highest and lowest values with their counts (can also chain to 
#     head() here).
# 
# - When removing outliers, we can do: `df[(df["col"] > x ) & (df["col"] < y )]`, but it's more readable to use: `df[df["col"].between(x,y)]`
# 
# 
# 

# Lets first try to use some of these on the `odometer` column:

# In[14]:


autos["odometer_km"].value_counts()


# Here we can clearly see that in this dataset there is a subtatial amount of cars for sale that exceed 100,000 km in their mileage.

# In[15]:


print(autos["price"].unique().shape)
print(autos["price"].describe())
autos["price"].value_counts().head(20)


# Notice that we have 1421 cases of "zero" for the prices of the car sales, we can drop all of the rows that lead to this result.
# 
# The highest price for a car exceeds 950,000 dollars. Lets examine the highest limit for a car price in our dataset for a moment.

# In[16]:


autos["price"].value_counts().sort_index(ascending=False).head(20)


# In[17]:


autos["price"].value_counts().sort_index(ascending=True).head(20)


# From what we can see here, there are more than 1,400 listings that have an opening price value of zero, but also a high number of expensive listings including one that exceeds $1 million.
# 
# From most auctions that can be found on Ebay, its particularly normal for an auction to begin at $1.

# In[18]:


autos = autos[autos["price"].between(1, 351000)] #Selecting an interval
autos["price"].describe() #In this interval, describe data statistically:


# However if we shorten the scope of our findings to an interval between 1 and 351,000 we can see that 50% of the listings are equal to or greater than 3,000 dollars. The `.describe()` function comes in handy here, giving the mean and certain percentile information.

# ## Exploring Date Columns
# 
# In this dataset there are a total of 5 columns that represent date values. Some of the columns were created by the crawler, some came from the website itself. 
# 
# The `date_crawled`, `last_seen`, and `ad_created` columns are all identified as string values by pandas. Because they are of a string datatype, we will need to convert the data into a numerical representation so we can understand it quantitatively.

# In[19]:


autos[['date_crawled','ad_created','last_seen']][0:5]


# In[20]:


(autos["date_crawled"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )


# In[21]:


(autos["date_crawled"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_values()
        )


# Looks like the site was crawled daily over roughly a one month period in March and April 2016. The distribution of listings crawled on each day is roughly uniform.

# In[22]:


(autos["last_seen"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )


# The crawler recorded the date it last saw any listing, which allows us to determine on what day a listing was removed, presumably because the car was sold.
# 
# The last three days contain a disproportionate amount of 'last seen' values. Given that these are 6-10x the values from the previous days, it's unlikely that there was a massive spike in sales, and more likely that these values are to do with the crawling period ending and don't indicate car sales.

# In[23]:


print(autos["ad_created"].str[:10].unique().shape)
(autos["ad_created"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )


# Note here that there is a large variety of ad created dates. Most fall within 1-2 months of the listing date, but a few are quite old, with the oldest at around 9 months.

# In[24]:


autos["registration_year"].describe()


# The year that the car was first registered will likely indicate the age of the car. Looking at this column, we note some odd values. The minimum value is 1000, long before cars were invented and the maximum is 9999, many years into the future.

# ## Dealing With Incorrect Information About Data
# 

# Because a car can't be first registered before the listing was seen, any vehicle with a registration year above 2016 is definitely inaccurate. Determining the earliest valid year is more difficult. Realistically, it could be somewhere in the first few decades of the 1900s.
# 
# One option is to remove the listings with these values. Let's determine what percentage of our data has invalid values in this column:
# 

# In[25]:


(~autos["registration_year"].between(1900,2016)).sum() / autos.shape[0]


# Since this represents less than 4% of the data we will remove these rows.

# In[26]:


# Many ways to select rows in a dataframe that fall within a value range for a column.
# Using `Series.between()` is one way.
autos = autos[autos["registration_year"].between(1900,2016)]
autos["registration_year"].value_counts(normalize=True).head(10)


# It appears that most of the vehicles were first registered in the past 20 years.

# ## Exploring Price By Brand

# In[27]:


autos["brand"].value_counts(normalize=True)


# German manufacturers represent four out of the top five brands, almost 50% of the overall listings. Volkswagen is by far the most popular brand, with approximately double the cars for sale of the next two brands combined.
# 
# There are lots of brands that don't have a significant percentage of listings, so we will limit our analysis to brands representing more than 5% of total listings.

# In[28]:


brand_counts = autos["brand"].value_counts(normalize=True)
common_brands = brand_counts[brand_counts > .05].index
print(common_brands)


# In[29]:


brand_mean_prices = {}

for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_price = brand_only["price"].mean()
    brand_mean_prices[brand] = int(mean_price)

brand_mean_prices


# Of the top 5 brands, there is a distinct price gap:
# 
# - Audi, BMW and Mercedes Benz are more expensive
# - Ford and Opel are less expensive
# - Volkswagen is in between - this may explain its popularity, it may be a 'best of 'both worlds' option.

# ## Exploring Prices With A Table

# In[30]:


bmp_series = pd.Series(brand_mean_prices)
pd.DataFrame(bmp_series, columns=["mean_price"])


# In[ ]:




