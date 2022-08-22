#!/usr/bin/env python
# coding: utf-8

# In[108]:


import psycopg2
import creds
from sqlalchemy import create_engine
import pandas as pd 
import pandas.io.sql as sqlio
import datetime as dt
from os import listdir
from os.path import isfile, join


# In[122]:


def getFilename(filePath):
    fileList = [f for f in listdir(filePath) if isfile(join(filePath, f))]
    return fileList

conn_stg = psycopg2.connect(
    host="db-datamart.cpawye9eytzs.us-east-1.rds.amazonaws.com",
    database="staging",
    port="5432",
    user="mart",
    password="martyuk123"
    )


# In[124]:


path = "\sql"
filename = getFilename(path)
o=0
for i in filename:
    tblname = i.replace(".sql","")
    sqlfile = open(path+"\\"+i,"r", encoding="utf-8")
    sql=sqlfile.read()
    dat = pd.read_sql_query(sql, conn_stg)
    df = pd.DataFrame(data=dat)
    engine = create_engine("postgresql://mart:martyuk123@db-datamart.cpawye9eytzs.us-east-1.rds.amazonaws.com:5432/datawarehouse")
    df['etl_loadtime'] = dt.datetime.now()
    df.to_sql(tblname, con=engine, if_exists='append')

