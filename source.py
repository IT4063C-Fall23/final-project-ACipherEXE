#!/usr/bin/env python
# coding: utf-8

# # {Project Title}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->
# 
# That there are cars that are recalled being sold. This could be a danger for others on the road and future owners. This could lead on to unessary deaths or owners being hurt. So I want the DMV to warn before the purchase of a used car or annoy the new owner to fix the car.

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->
# 
# How many cars are currently sold with defects in the US and how many reports of known problems are happening? 

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->
# 
# I belive a large amount of defect cars are being sold in the US and cars that have defects are still on the road. 

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->

# I will use the NHTSA dataset for defects for a list of what is going on.
# 
# Link:https://www.nhtsa.gov/nhtsa-datasets-and-apis
# 
# I will used a automated dataset in kaggle that takes cars being sold in Craigslist because that is normally where owners sell their cars
# 
# Link: https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data
# 
# 
# Plus figure out how many could have been hurt by these defects with the NHTSA
# 
# Link:https://www.nhtsa.gov/nhtsa-datasets-and-apis
# 

# In[ ]:





# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->
# 
# First I want to concentrate of how many one popular brand and model of a certain year from each region US, Asian and Euro manufactures. Then look at each of their popular models and look for a list of defects that has been reported by the NHTSA. Then check how many are being on sale currently per state with the kaggle dataset. Then see how many reports of a model has been made by the last 5 years.

# In[110]:


# Start your code here


# In[111]:


import requests
import pandas as pd
# According the Zebra these are the best selling in the US ever
# https://www.thezebra.com/resources/driving/most-popular-cars/

# the best selling Asian car so far is the Honda Accord in the US
request_params_asian = {
    "make": "Honda",
    "model": "Accord",
    "modelYear": "2012"
}
response_asian = requests.get("https://api.nhtsa.gov/recalls/recallsByVehicle", params=request_params_asian)
print( response_asian.json())
response_asian_data = pd.DataFrame(response_asian.json()['results'])
response_asian_data.head()


# In[112]:


# the best selling American car so far is the Ford F-Series in the US. Becuse there is multiple versions ill use the F-150 as a common truck.
request_params_us = {
    "make": "ford",
    "model": "F-150",
    "modelYear": "2012"
}
response_us = requests.get("https://api.nhtsa.gov/recalls/recallsByVehicle", params=request_params_us)
print( response_us.json())
response_us_data = pd.DataFrame(response_us.json()['results'])
response_us_data.head()


# In[113]:


# Euro cars are a lot smaller in the market but they are possible to find
# According to a article the Volkswagen Jetta is the most sold Euro in the US market
# Link: https://tempeautointeriorsrepair.com/the-top-european-cars-in-the-u-s/
request_params_euro = {
    "make": "Volkswagen",
    "model": "Jetta",
    "modelYear": "2012"
}
response_euro = requests.get("https://api.nhtsa.gov/recalls/recallsByVehicle", params=request_params_euro)
print( response_euro.json())
response_euro_data = pd.DataFrame(response_euro.json()['results'])
response_euro_data.head()


# In[114]:


# You will have to download the kaggle data set as its too big for git
# Link: https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data
# and throw it into Data folder
# I tried to make it easy with code but kaggle is not letting me
# No need to run this files with needed data is in the Data folder

import os
import webbrowser
folder_path = './Data/'
file_name = 'vehicles.csv'

if os.path.isfile(os.path.join(folder_path, file_name)):
    print(f"The file {file_name} is in the folder {folder_path}.")
    
else:
    print('I have opened a page to download the CSV needed please put it in the Data folder')
    webbrowser.open('https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data')

sales_df = pd.read_csv('Data/vehicles.csv')
sales_df.tail()


# In[115]:


# Remove unessary data like url, region_url, price, condition, cylinders, size, paint_color, image_url, description, posting_date, 'fuel, drive
sales_df_fixed = sales_df.drop(['url','region_url','price','condition','cylinders','size','paint_color','image_url','description','posting_date', 'fuel', 'drive', 'type', 'county'], axis=1)

sales_df_fixed.tail()


# In[116]:


# Get all honda accords from 2012
filtered_df_aisan = sales_df_fixed[(sales_df_fixed['manufacturer'] == 'honda') & (sales_df_fixed['model'].str.contains('accord')) & (sales_df_fixed['year'] == 2012.0)]
filtered_df_aisan.tail()


# In[117]:


# Get all ford f-150s from 2012
filtered_df_american = sales_df_fixed[(sales_df_fixed['manufacturer'] == 'ford') & (sales_df_fixed['model'].str.contains('f-150')) & (sales_df_fixed['year'] == 2012.0)]
filtered_df_american.tail()


# In[118]:


# Get all volkswagen jettas from 2012
filtered_df_euro = sales_df_fixed[(sales_df_fixed['manufacturer'] == 'volkswagen') & (sales_df_fixed['model'].str.contains('jetta')) & (sales_df_fixed['year'] == 2012.0)]
filtered_df_euro.tail()


# In[ ]:





# In[119]:


#save the data into a CSV and open it for testing
filtered_df_aisan.to_csv('Data/filtered_df_aisan.csv', index=False)
filtered_df_american.to_csv('Data/filtered_df_american.csv', index=False)
filtered_df_euro.to_csv('Data/filtered_df_euro.csv', index=False)


# In[120]:


asian_cars_on_sale = pd.read_csv('Data/filtered_df_aisan.csv')
asian_cars_on_sale.head()


# In[121]:


american_cars_on_sale = pd.read_csv('Data/filtered_df_american.csv')
american_cars_on_sale.head()


# In[122]:


euro_cars_on_sale = pd.read_csv('Data/filtered_df_euro.csv')
euro_cars_on_sale.head()


# In[123]:


# Now I need to set up the api for reports made by NHTSA currently about these three models
complaints_params_asian = {
    "make": "Honda",
    "model": "Accord",
    "modelYear": "2012"
}
complaints_response_asian = requests.get("https://api.nhtsa.gov/complaints/complaintsByVehicle", params=complaints_params_asian)
print( complaints_response_asian.json())
complaints_asian_data = pd.DataFrame(complaints_response_asian.json()['results'])
complaints_asian_data.head()


# That the Accord has a total of 354 complaints

# In[124]:


complaints_params_american = {
    "make": "ford",
    "model": "F-150",
    "modelYear": "2012"
}
complaints_response_american= requests.get("https://api.nhtsa.gov/complaints/complaintsByVehicle", params=complaints_params_american)
print( complaints_response_american.json())
complaints_american_data = pd.DataFrame(complaints_response_american.json()['results'])
complaints_american_data.head()


# The f-150 does not seem to have complaints

# In[125]:


complaints_params_euro = {
    "make": "Volkswagen",
    "model": "Jetta",
    "modelYear": "2012"
}
complaints_response_euro= requests.get("https://api.nhtsa.gov/complaints/complaintsByVehicle", params=complaints_params_euro)
print( complaints_response_euro.json())
complaints_euro_data = pd.DataFrame(complaints_response_euro.json()['results'])
complaints_euro_data.head()


# That the Jetta has a total of 510 complaints. Thats crazy

# Checkpont 2:
# What have we have so far? 
# 
# That the f-150 was built tough and the accord and Jetta both have a large amount of complaints. But defect wise the ford only has 4 recalls, the honda and the volkwagen have 8. But there is a ton of all in the us with the data we got from cregslist. 
# 
# There is missing vins and other things but I think with a .dropna we can clean it up.

# Lets first build a map of all the cars in the us useing the long and lat.

# In[126]:


import folium
# There was NaNS in the df for lat and long
american_cars_on_sale.dropna(inplace=True)
euro_cars_on_sale.dropna(inplace=True)
asian_cars_on_sale.dropna(inplace=True)

map_object = folium.Map(location=[39.8283, -98.5795], zoom_start=4)
for index, row in american_cars_on_sale.iterrows():
    folium.Marker([row['lat'], row['long']], popup=row['model']).add_to(map_object)
for index, row in euro_cars_on_sale.iterrows():
    folium.Marker([row['lat'], row['long']], popup=row['model']).add_to(map_object)
for index, row in asian_cars_on_sale.iterrows():
    folium.Marker([row['lat'], row['long']], popup=row['model']).add_to(map_object)
map_object


# We can see clearly that these cars are still sold all around the US. So there is a high chance that a new owner could have these cars. Even in Alaska and Hawwaii. This is a sample there are still a lot of cars that were excludeddo to the data being incomplite in cregslist. 

# But suddenly I started thinking how many vins from the creglist can I find hits with complaints in the NHTSA?
# Because there is no complaints in the F-150 we will skip them

# In[127]:


map_object = folium.Map(location=[39.8283, -98.5795], zoom_start=4)
complaints_asian_data
complaints_asian_data.dropna(inplace=True)
for index, row in asian_cars_on_sale.iterrows():
    if row['VIN'] in complaints_asian_data['vin'].tolist():
        folium.Marker([row['lat'], row['long']], popup=row['model']).add_to(map_object)
for index, row in euro_cars_on_sale.iterrows():
    if row['VIN'] in complaints_euro_data['vin'].tolist():
        folium.Marker([row['lat'], row['long']], popup=row['model']).add_to(map_object)
map_object


# Incredible but why is there none? According to NHTSA complaints are filed by users of the cars. So it was bad to assume this but they could be still roaming the US but could be being sold without the vin. So I belive this could cause a risk if a complaint was filed but still sold.

# But lets find out then what is the most common Consequence a recall could avoid. Just to get a idea of what is the worse thing it could happen if the car is not remedied.  

# In[128]:


#I want to see what the most common recall of the three cars are? I belive a word cloud could get a awnser to that quesion
#first set up for all three to become one
from wordcloud import WordCloud
import matplotlib.pyplot as plt
consequence_asian = ' '.join(response_asian_data['Consequence'].astype(str))
consequence_euro = ' '.join(response_euro_data['Consequence'].astype(str))
consequence_us = ' '.join(response_us_data['Consequence'].astype(str))

# Combine the text from all DataFrames
combined_recall = consequence_asian + ' ' + consequence_euro + ' ' + consequence_us

# Word cloud set up
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_recall)

# Display of word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Recall Consequences')
plt.show()


# What did we get from this?

# Well seeing crash is pretty scarry. Death under injury not so great. This word cloud almost looks like a ad for a experimental medication. A small chanse of fire. Effects to occupents. It seems these three popular cars could really hurt not only the driver but others inside the car. Plus May that word does sound odd at first but for a car thats a 50/50 roll on a recall problem. Its unkown until it happens.
# 
# Lets compare it to complaints to see if owners are affected

# In[129]:


affected_asian = ' '.join(complaints_asian_data['summary'].astype(str))
affected_euro = ' '.join(complaints_euro_data['summary'].astype(str))

# Combine the text from all DataFrames
combined_recall = consequence_asian + ' ' + consequence_euro

# Word cloud set up
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_recall)

# Display of word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Recall Consequences')
plt.show()


# Injury, crash and rish are way higher than expected. Death has risen a little bit but that means cars have gotten safer and these are from 2012 imagine this year cars? 
# But air bag has increased. Why? 

# Well airbags are really chemical grenades that try to save you from impact but at the same time they could case burns, neck pains and other injurys.

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->
# To figure out API stuff related to NHTSA
# 
# Link:https://www.nhtsa.gov/nhtsa-datasets-and-apis
# 
# The best selling cars that are american and asian
# 
# Link:https://www.thezebra.com/resources/driving/most-popular-cars/
# 
# The best selling Euro car
# 
# Link: https://tempeautointeriorsrepair.com/the-top-european-cars-in-the-u-s/
# 
# 
# 

# In[131]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

