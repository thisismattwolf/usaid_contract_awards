# -*- coding: utf-8 -*-
'''
Created on Wed Aug 29 13:46:13 2018

@author: Matthew Wolf

A script to take contract award files from usaspending.gov, clean them, analyze 
them, and join them for further analysis and visualization in Tableau

Files downloaded as .csv and saved in a folder on the desktop:
    C:\\Users\\Matthew Wolf\\Desktop\\US Agencies CAs

File Names:
    FY 2017 USAID Prime Contract Data.csv
    FY 2017 USAID Prime Assistance Data.csv
    FY 2017 USAID Prime Contract Data Subawards.csv
    FY 2017 USAID Prime Assistance Data Subawards.csv
    
===============================================================================
STEP ONE: LOAD LIBRARIES AND DATA
'''

import os, pandas as pd

#point to correct directory
os.chdir('C:\\Users\\Matthew Wolf\\Desktop\\US Agencies CAs')
list_of_sources = []
#read in USAID contracts data
print('--------Loading USAID Contracts Data--------')
usaid_contracts = pd.read_csv('.\\FY 2017 USAID Prime Contract Data.csv')
list_of_sources.append(usaid_contracts)
print('--------USAID Contracts Data loaded--------')
print('Data shape: ' + str(usaid_contracts.shape))
print()

#read in USAID assistance data
print('--------Loading USAID Assistance Data--------')
usaid_assistance = pd.read_csv('.\\FY 2017 USAID Prime Assistance Data.csv')
list_of_sources.append(usaid_assistance)
print('--------USAID Assistance Data loaded--------')
print('Data shape: ' + str(usaid_assistance.shape))
print()

#read in USAID contracts subcontracts data
print('--------Loading USAID Contracts Subawards Data--------')
usaid_contracts_subs = pd.read_csv('.\\FY 2017 USAID Prime Contract Data Subawards.csv')
list_of_sources.append(usaid_contracts_subs)
print('--------USAID Contracts Subawards Data loaded--------')
print('Data shape: ' + str(usaid_contracts_subs.shape))
print()

#read in USAID assistance subcontracts data
print('--------Loading USAID Assistance Subawards Data--------')
usaid_assistance_subs = pd.read_csv('.\\FY 2017 USAID Prime Assistance Data Subawards.csv')
list_of_sources.append(usaid_assistance_subs)
print('--------USAID Assistance Subawards Data loaded--------')
print('Data shape: ' + str(usaid_assistance_subs.shape))
print()
print('Date ready to go!')
print()
'''
===============================================================================
STEP TWO: DEAL WITH BLANKS AND UNWANTED DIMENSIONS
'''
#Delete any columns that are only blank values, and "bad columns"
#See errata file for a list of "good" and "bad" columns
print('--------Searching for blank or unwanted dimensions--------')
os.chdir('C:\\Users\\Matthew Wolf\\Desktop\\US Agencies CAs\\scripts')
from variables import usaid_contracts_fields, usaid_assistance_fields, usaid_contracts_subs_fields, usaid_assistance_subs_fields

#create a dictionary to hold a list of dimensions deleted from 
#TO DO

#For each source DataFrame, check its columns for any all-blank columns
#if any are found, delete them
for source in list_of_sources:
    for column in source.columns:
        if source[column].isnull().sum() == source.shape[0]:
            del source[column]

print('Blank columns deleted from all data sources.')

#Clean unwanted columns from Prime Contracts data
for column in usaid_contracts.columns:
    if column not in usaid_contracts_fields:
        del usaid_contracts[column]
print('USAID Prime Contracts Data cleaned of unwanted dimensions')

#Clean unwanted columns from Prime Assistance data
for column in usaid_assistance.columns:
    if column not in usaid_assistance_fields:
        del usaid_assistance[column]
print('USAID Prime Assistance Data cleaned of unwanted dimensions')

#Clean unwanted columns from Contracts Subawards data
for column in usaid_contracts_subs.columns:
    if column not in usaid_contracts_subs_fields:
        del usaid_contracts_subs[column]
print('USAID Contracts Subawards Data cleaned of unwanted dimensions')

#Clean unwanted columns from Assistance Subawards data
for column in usaid_assistance_subs.columns:
    if column not in usaid_assistance_subs_fields:
        del usaid_assistance_subs[column]
print('USAID Assistance Subawards Data cleaned of unwanted dimensions')
print()

'''
===============================================================================
STEP THREE: CLEAN SOME DIMENSIONS
Copy all four dataframes. For the Primes datasets, cut all except the columns
they have in common, and combine Prime Contracts and Prime Assistance into one.
For Subawards datasets, cut all except the columns they have in common, and
combine Contracts Subs and Assistance Subs into one.
'''
#rename the prime contracts column award_id_piid to award_id
#rename the prime assistance column award_id_fain to award_id
usaid_contracts.rename(columns = {'award_id_piid': 'award_id'}, inplace = True)
usaid_assistance.rename(columns = {'award_id_uri': 'award_id'}, inplace = True)
usaid_contracts_subs.rename(columns = {'prime_award_piid': 'award_id'}, inplace = True)
usaid_assistance_subs.rename(columns = {'prime_award_fain': 'award_id'}, inplace = True)
#remove '-' from the award_id's of the assistance data
usaid_assistance['award_id'].replace(regex=True, inplace=True, to_replace='-',value='')


'''
===============================================================================
STEP FOUR: CREATE SIMPLIFIED DATAFRAMES
Copy all four dataframes. For the Primes datasets, cut all except the columns
they have in common, and combine Prime Contracts and Prime Assistance into one.
For Subawards datasets, cut all except the columns they have in common, and
combine Contracts Subs and Assistance Subs into one.
'''
#TO DO: function to find common fields across data sources, put them in lists

#import lists of columns in common from variables page
print('--------Pulling common fields for contracts and assistance data--------')
print()
print('--------Note to self - add this function--------')
print()
print('--------Creating primes dataframe--------')
#get lists of desired columns
from variables import primes_fields, subs_fields
#create df from prime contracts data with desired columns - add a column for
#'type' to indicate these rows come from a contract
simple_contracts = usaid_contracts[primes_fields].copy()
simple_contracts['type'] = 'contract'
simple_contracts['award_or_idv_flag'] = usaid_contracts['award_or_idv_flag']
simple_contracts['award_type'] = usaid_contracts['award_type']
simple_contracts['idv_type'] = usaid_contracts['idv_type']
simple_contracts['multiple_or_single_award_idv'] = usaid_contracts['multiple_or_single_award_idv']
simple_contracts['type_of_idc'] = usaid_contracts['type_of_idc']
simple_contracts['type_of_contract_pricing'] = usaid_contracts['type_of_contract_pricing']
simple_contracts['solicitation_identifier'] = usaid_contracts['solicitation_identifier']
simple_contracts['product_or_service_code_description'] = usaid_contracts['product_or_service_code_description']
simple_contracts['naics_description'] = usaid_contracts['naics_description']
simple_contracts['domestic_or_foreign_entity'] = usaid_contracts['domestic_or_foreign_entity']
simple_contracts['number_of_offers_received'] = usaid_contracts['number_of_offers_received']

#create df from prime assistance data with desired columns - add a column for
#'type' to indicate these rows come from a contract    
simple_assistance = usaid_assistance[primes_fields].copy()
simple_assistance['type'] = 'assistance'

#join the simple_contracts and simple_assistance frames for visualization
frames = [simple_contracts, simple_assistance]
viz_data = pd.concat(frames)
print('Combined contracts and assistance dataframe created')
print('Shape: ' + str(viz_data.shape))
print()

print('--------Creating subs dataframe--------')
#create df from contracts sub data with desired columns - add a column for
#'type' to indicate these rows come from a contract sub
simple_contracts_subs = usaid_contracts_subs[subs_fields].copy()
simple_contracts_subs['type'] = 'contract sub'

#create df from assistance sub data with desired columns - add a column for
#'type' to indicate these rows come from a assistance sub
simple_assistance_subs = usaid_assistance_subs[subs_fields].copy()
simple_assistance_subs['type'] = 'assistance sub'

frames_subs = [simple_contracts_subs, simple_assistance_subs]
viz_subs_data = pd.concat(frames_subs)
print('Combined subawards dataframe created')
print('Shape: ' + str(viz_subs_data.shape))
print()

print('--------Simplified primes and subs Dataframes created--------')

'''
===============================================================================
STEP FIVE: WRITE DATAFRAMES TO CSV FOR TABLEAU VISUALIZATION
Write the viz_data and viz_data_subs dfs to csv in the same folder as the source
datafiles
'''
#viz_data.to_csv('C:\\Users\\Matthew Wolf\\Desktop\\US Agencies CAs\\results\\USAID_main_data.csv', index=False)
#viz_subs_data.to_csv('C:\\Users\\Matthew Wolf\\Desktop\\US Agencies CAs\\results\\USAID_subs_data.csv', index=False)


