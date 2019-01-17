# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:07:47 2018

PURPOSE: Establish Oracle DB connection then and perform sample query and drop results to pandas dataframe

#SAMPLE QUERY

import pandas as pd

fields = 'col_1' , 'col_2'
table = 'table'
cursor.execute('select ' + fields + ' from ' + table) # use triple quotes if you want to spread your query across multiple lines

data=list()
for row in cursor:
    data.append(row)

new_columns= []
columns=fields.split(',')
for i in columns:
    k = str(i).replace(' ','')
    new_columns.append(k)

df = pd.DataFrame(data=data, columns=new_columns)
df
#cursor.close()
#connection.close()

@author: duchezbr
"""

#%% ESTABLISH CONNECTION TO Oracle DB
import cx_Oracle
print("cx_Oracle version:",cx_Oracle.version)
print("Oracle client version:",cx_Oracle.clientversion())

host='' 
user='user'
password='pw'
port='####'
db='db name'

dsn=cx_Oracle.makedsn(host, port, db)
connection=cx_Oracle.connect(user, password, dsn)
cursor = connection.cursor()
print("Oracle database version:",connection.version)
print("db dsn:",connection.dsn)



