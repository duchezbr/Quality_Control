# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:31:23 2019

PURPOSE: Evaluate how closely aligned 'Days From First Dose' or 'Days From Rand' are to 'Norm Study Time'.

INPUT: 
    df: pandas data frame
    fields: list
        contains field names for 'Norm Study Time' and 'Days From First Dose' OR 'Days From Rand', 'Src Timepoint', 'Collection Name (ID)' in this order 
    differenece: int
        threshold for allowed difference between 'Norm Study Time' and DFFD or DFR and not be flagged
    max_diff: int
        maximum difference thershold between the 'Norm Study Time' and DFFD or DFR fields
        
OUTPUT:
    num_not_equal: pandas dataframe
        contains 'Norm Study Time', 'DFFD or DFR', 'Src Timepoint' and 'Collection Name' where the difference between NST and DDFD OR DFR exceed allowed threshold

@author: duchezbr
"""

def compare_nst_daysFromX(df, fields, difference, max_diff):

    diff = np.abs(df[fields[0]] - df[fields[1]])
    diff_drop_na = diff.dropna()
    idx = diff_drop_na[(diff_drop_na > difference) & (diff_drop_na < max_diff)].dropna().index
    num_not_equal = df.loc[idx, fields]

    return num_not_equal