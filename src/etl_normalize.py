import pandas as pd
import numpy as np
import get_geometric_info as getLocation

def normalize():
    #--- Prepare for the kpi.csv schema --------------------------------------------------------------------------
    # 1) Normal the indicator table for kpi.csv
    #-----df = pd.read_csv('../db/kpi/clean_2.csv')     must delete
    #-----df.to_csv('../db/kpi/kpi.csv', index=True)    must delete
    
    df = pd.read_csv('../db/kpi/clean_2.csv')

    # Retain all the LibraryName have 'No Name' in kpi.csv
    # drop any rows that contains 'No Name' in the LibraryName column
    df = df[df.LibraryName != 'No Name']

    cols = ["seqNo","indicator_id","financialYear","Total","April","May","June","Q1","July","August","September","Q2","October","November","December","Q3","January","February","March","Q4","Polarity"]
    df = df.reindex(columns=cols)
    df.set_index('seqNo')
    df['seqNo'] = df.index + 1
    df.to_csv('../db/kpi/kpi.csv', index=False)

    #--- Prepare for the kpi-percentage.csv schema --------------------------------------------------------------------------
    # 2) Normal the indicator table for kpi-percentage.csv
    df = pd.read_csv('../db/kpi/clean_2.csv')
    
    # Retain all the LibraryName have 'No Name' in kpi-percentage.csv
    # Retain any rows that have 'No Name' in the LibraryName column
    df = df[df.LibraryName == 'No Name']

    cols = ["seqNo","indicator_id","financialYear","Total","April","May","June","Q1","July","August","September","Q2","October","November","December","Q3","January","February","March","Q4","Polarity"]
    df = df.reindex(columns=cols)
    df.set_index('seqNo')
    df['seqNo'] = df.index + 1
    df.to_csv('../db/kpi/kpi-percentage.csv', index=False)


    #--- Prepare for the indicator schema --------------------------------------------------------------------------
    # 3) Normal the indicator table
    df = pd.read_csv('../db/kpi/clean_2.csv')
    df.to_csv('../db/kpi/tempIndicator.csv', index=False)

    df = pd.read_csv('../db/kpi/tempIndicator.csv')

    # Set up the Longidute
    longitude = 0.0
    latitude = 0.0

    # Create 2 new columns for Longitude
    df['Longitude'] = longitude
    df['Latitude'] = latitude

    # Finalize the table schema
    cols = ["indicator_id","Activity","LibraryName","CollectionFrequency","Latitude","Longitude","Polarity"]
    df = df.reindex(columns=cols)
    df.to_csv('../db/kpi/indicator.csv', index=False)
 
    # How to drop row & column in Pandas, refer:
    # https://www.shanelynn.ie/pandas-drop-delete-dataframe-rows-columns/

    # Trim down the row
    df = pd.read_csv('../db/kpi/indicator.csv')

    rowCount = -1
    libraryCount = 0
    deleteCount = 0
    dropThis = ""
    for id in df['indicator_id']:
        if dropThis == id:
           df.drop(labels=rowCount, axis=0, inplace=True)
           deleteCount += 1
           pass
        else:
            dropThis = id
            libraryCount += 1
            # print(dropThis)
        rowCount += 1

    # Keep counting the number of record that grap the Latitude and Longitude
    print('No of library is ', libraryCount)
    print('No of record deleted is ', deleteCount)
    df.to_csv('../db/kpi/indicator.csv', index=False)

    # Get the Longitude and Latitude from Google Maps
    df = pd.read_csv('../db/kpi/indicator.csv')
    
    tempList =[]
    i = 0
    for ind in df.index:
        if df['LibraryName'][ind] != 'No Name':
           tempList = getLocation.get_geometric(df['LibraryName'][ind])
           df.loc[i, 'Latitude'] = tempList[0]           
           df.loc[i, 'Longitude'] = tempList[1]
        i += 1

    df.to_csv('../db/kpi/indicator.csv', index=False)
normalize()