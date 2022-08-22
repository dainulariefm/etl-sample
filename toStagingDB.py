#!/usr/bin/env python
# coding: utf-8

# In[78]:


import boto3
import pandas as pd
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO # Python 2.x
else:
    from io import StringIO # Python 3.x
import creds
from sqlalchemy import create_engine
import datetime as dt
import re


todays = dt.date.today()
year = todays.year
month = todays.month
day = todays.day

ACCESS_KEY=creds.access_key
SECRET_KEY=creds.secret_key

s3_rsc = boto3.resource('s3'     
            , aws_access_key_id=ACCESS_KEY
             , aws_secret_access_key=SECRET_KEY)

s3_clnt = boto3.client("s3"
             , aws_access_key_id=ACCESS_KEY
             , aws_secret_access_key=SECRET_KEY
                 )

def removeDup(dirtyData):
    stepDups = dirtyData.drop_duplicates(subset=None,keep='first',inplace=False)
    return stepDups

def newColDate(tbl):
    rn = []
    for col in tbl.columns:
        newcol = col.replace("_at","_date")
        newcol = newcol.replace("_timestamp","_date")
        rn.append(newcol)
        
    return rn

def dataCleansing(df):
    newcol = newColDate(df)
    z = 0
    df = df.convert_dtypes()
    for col in df.columns:    
        newcolumns = newcol[z]
        df = df.rename(columns={col:newcolumns})
        if "_date" in newcolumns :
            df[newcolumns] = pd.to_datetime(df[newcolumns], format="%Y-%m-%d %H:%M:%S")

        z= z+ 1

    df = removeDup(df)
    
    return df


# In[80]:


awsBucketSourceName = "perqara-landingzone-us-east1-dev"
awsBucketSourceResource = s3_rsc.Bucket(awsBucketSourceName)


# In[82]:


engine = create_engine("postgresql://mart:martyuk123@db-datamart.cpawye9eytzs.us-east-1.rds.amazonaws.com:5432/staging")


# In[69]:



for object_summary in awsBucketSourceResource.objects.filter():
    object_key = str(object_summary.key)  
    if str(year)+str(month)+str(day) in object_key :
        csv_obj = s3_clnt.get_object(Bucket=awsBucketSourceName, Key=object_key)
        body = csv_obj['Body']
        csv_string = body.read().decode('utf-8')
        df = pd.read_csv(StringIO(csv_string))
        df = dataCleansing(df)
        df['etl_loadtime'] = dt.datetime.now()
        tblname = re.search(r'^[a-z_]*',str(object_key)).group()
        df.to_sql(tblname, con=engine, if_exists='append')
    
    else:
        continue


# In[61]:


print(dt.datetime.now())

