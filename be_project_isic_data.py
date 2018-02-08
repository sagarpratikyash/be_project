
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json


# In[2]:


import glob
#Enter the folder name in which your json files are stored followed by /*.json
#Example if my json files are in /home/pratik/Desktop/be_project/downloaded_meta/UDA-1/
#I will write /home/pratik/Desktop/be_project/downloaded_meta/UDA-1/*json
#/home/sagar/Desktop/BE/ISIC-images/UDA-1
filenames = glob.glob('/home/sagar/Desktop/BE/ISIC-images/MSK-1/*.json')
d=[]
for fname in filenames:
    with open(fname, 'r') as readfile:
        d.append(json.load(readfile))
        


# In[3]:


data=pd.DataFrame()
data['value']=d


# In[4]:


data['name']=data['value'].apply(lambda x: x['name'])
data['age']=data['value'].apply(lambda x: (x['meta']['clinical']['age_approx']))
data['benignmalignant']=data['value'].apply(lambda x: x['meta']['clinical']['benign_malignant'])
data['diagnosis']=data['value'].apply(lambda x: x['meta']['clinical']['diagnosis'])
data['sex']=data['value'].apply(lambda x: x['meta']['clinical']['sex'])


# In[5]:


data


# In[6]:


#here we are saving the data
#write the file name in which you want to save the data
#write a new file for each folder
#here since my data is from UDA-1 i have stored it in an excel file named UDA-1
#do the same for all the folders and make separate excel files for each
writer = pd.ExcelWriter('/home/sagar/Desktop/BE/metadata/MSK-1.xlsx')
data.to_excel(writer,'Sheet1')
writer.save()


