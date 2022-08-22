#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
from os import listdir
from os.path import isfile, join
from datetime import date

# creds
access_key="AKIA5AFAVX7VDB7AOH2F"
secret_key="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"

s3 = boto3.client("s3"
             , aws_access_key_id=ACCESS_KEY
             , aws_secret_access_key=SECRET_KEY
                 )

# get filenames in local drive  function
def getFilename(filePath):
    fileList = [f for f in listdir(filePath) if isfile(join(filePath, f))]
    return fileList

# upload to s3 function
def toS3(path,filenameExt,awsBucket,newFilename):
    s3.upload_file(
        Filename= path+"\\"+filenameExt,  
        Bucket=awsBucket,
        Key=newFilename
    )
    


# In[2]:


path = "\dataset"
filename = getFilename(path)
awsBucket="perqara-landingzone-us-east1-dev"
todays = date.today()
year = todays.year
month = todays.month
day = todays.day

#Bulk Upload to landingzone bucket as it is
for i in filename:
    k = i.replace(".csv","")
    k = k.replace("_dataset","")
    toS3(path,i,awsBucket,
        k+"/"+str(year)+str(month)+str(day)+"/"
         +k+".csv"
        )
        

