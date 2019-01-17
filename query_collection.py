# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:07:34 2018

PURPOSE: Execute a query of the Oracle database following establishing connection using connect_Oracle_DB.py script
INPUT:
    fields: str
        string of designated fields seperated by commas
    table: str
        table that contains desired fields
    collection_id: int
        unique numerical identifier for the collection that contains desired data
OUTPUT:
    bdm: pandas dataframe
        query reuslts with columns contained designated field names.  If field is '*' then columns are numbers

@author: duchezbr
"""

def query_collection(fields, table, collection_id):
    
    cursor.execute('select ' + fields + ' from ' + table + ' where collection_id = ' + str(collection_id))
    
    data=list()
    for row in cursor:
        data.append(row)

    if fields == '*':
        bdm = pd.DataFrame(data=data)
    else:
        new_columns= []
        columns=fields.split(',')
        for i in columns:
            k = str(i).replace(' ','')
            new_columns.append(k)
        bdm = pd.DataFrame(data=data, columns=new_columns)
    
    return bdm

