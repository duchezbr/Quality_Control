# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:33:45 2019

PURPOSE: determine if norm_study_time values are valid depending on the associated norm_study_time_unit assignment
         ensure that naming of nort_study_time_unit is consistent with buisness rules

DEPENDENCIES: requires import of... 
    pandas
    numpy
    re

INPUT:
    df: pandas dataframe
        contains norm_study_time and norm_study_time_unit query result from bdm
    fields: ordered list 
        contains the column names for norm_study_time, norm_study_time_unit, and collection_name|id in this exact order

        
OUTPUT:
    bad_values: dict
        names of df norm_study_time_unit (key) and a list of associated norm_study_time (values) that do not conform to business rulls
    units_not_present: np.array
        Unit names that do not align with convention for naming 'norm study time units'
        

@author: duchezbr
"""

def check_nst_values(df, fields):
    
    units = df[fields[1]].value_counts().index
    
    adict = {"B-CELL RECOVERY": '95\d{2}',
    "CYCLE/DAY": '1001',
    "DAY": '(-|'')\d+',
    "DAY, RETREATMENT": '77\d{5}',
    "DAYS FROM FIRST DOSE": '(-|'')\d+',
    "DAYS FROM RUNIN START": '(-|'')\d+',
    "DAYS FROM RANDOMIZATION": '(-|'')\d+',
    "DRT": '(-|'')\d+',
    "EARLY DISCONTINUATION": '9660',
    "END OF RETREATMENT": '7709990',
    "END OF STUDY": '9990',
    "END OF TREATMENT": '9990',
    "ENDPOINT": '(-|'')\d+',
    "MAINTENANCE VISIT": '200002',
    "POST VISIT": '999\d{2}',
    "POST VISIT, RETREATMENT": '77999\d{2}',
    "SCREENING": '-1',
    "SCREENING, RETREATMENT": '7700000',
    "SCREENING/RUN-IN": '7700000',
    "UNSCHEDULED": '9930',
    "VISIT": '(-|'')\d+',
    "WEEK": '(-|'')\d+'}
    
    #!!! find nstu from query that are standard bdm nstu then identify those not present (can return or print in future)
    units_intersect = np.intersect1d(units, list(adict.keys()))
    units_not_present = np.setdiff1d(units, units_intersect)
    
    print("\nNSTU not consistent with buisness rules:")
    [print(i) for i in units_not_present]
    print('\n')
    
    lst = list()
    collections = list()
    bad_vals = dict()
    
    # loop through standard nstu from query 
    for unit in units_intersect:
        print(unit)
        idx = df[df[fields[1]] == unit].index.values
        df1 = df.iloc[idx, ::].dropna(subset=[fields[0]])
        nst_values = df1.loc[::, fields[0]].values 
        collection_name = df1.loc[::, fields[2]].values    
        value = adict[unit]
        p = re.compile(value)
        # identify nst values that are not appropriately associated with nstu 
        for cnt, val in enumerate(nst_values):
            if p.match(str(val)):
                continue
            else:
                lst.append(val)
                collections.append(collection_name[cnt])
                print(collection_name[cnt], str(val))
                #print(str(val))
        if len(lst) > 0:
            # values contain list of nst values that are not appropriate for corresponding nstu and the collections that contain bad nst values
            bad_vals[unit] = lst, list(set(collections))
        lst = list()
        collections = list()
    
    return bad_vals, units_not_present

