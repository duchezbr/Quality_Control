# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:28:27 2018

Filter rows from source table where subjectID does not mactch subjectID from BDM SUBJECT table. This is typically applied as a FILTER statement to the Parse_Prelim table to generate the PARSE output table

INPUT: 
    src: pandas table
        table from which rows are to be removed when subjectIDs don't match bdm
    bdm: pandas table
        table that contains distinct subjectIDs contained in BDM
    src_subject_field: 'string'
        name of column that contains subjectIDs
    bdm_subjectID: 'string'
        name of column that contains subjectIDs

@author: duchezbr
"""


def subjid_equals_subjid(src, bdm, src_subject_field, bdm_subject_field):

    ids = np.setdiff1d(src[src_subject_field].astype(str), bdm[bdm_subject_field])
    ids = ids.astype('int64')
    for i in ids:
        src = src[src[src_subject_field] != i]
        
    return src
        
        

