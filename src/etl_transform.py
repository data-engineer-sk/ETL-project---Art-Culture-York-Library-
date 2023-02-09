import pandas as pd
import numpy as np

def transform():
    
    # Phase I Process
    df = pd.read_csv('../data/kpi/kpi-art-culture.csv')

    # Read thought the Year column and convert it to 'YYYY-mm-dd' format
    count = 0
    for financialYear in df['Year']:
        df.loc[count,'Year'] = financialYear[5:]+'-03-31'
        count += 1

    # Drop the 'YearType' column
    df = df.drop(['YearType'], axis=1)

    df.rename(columns = {'Year':'financialYear'}, inplace = True)
    
    df.to_csv('../db/kpi/clean_1.csv', index=False)

    df1 = pd.read_csv('../db/kpi/clean_1.csv')
    # Change 'NC' to -1
    df1.replace('NC', -1, inplace = True)

    new_columns = df1['Indicator'].str.split(' - ', expand=True)

    df1['Activity']=new_columns[0]
    df1['LibraryName']=new_columns[1]

    # Rename Id column to indicator_id
    df1.rename(columns = {'Id':'indicator_id'}, inplace = True)
     
    # Set the NaN value to No Name
    df1['LibraryName'].replace(np.nan, 'No Name', inplace = True) 

    df1.to_csv('../db/kpi/clean_1.csv', index=False)
    print(df1.info())

    #--------------------------------------------------------
   # Phase II Process (Re-order the columns sequence)
    df = pd.read_csv('../db/kpi/clean_1.csv')

    # Drop the 'Indicator' column
    df = df.drop(['Indicator'], axis=1)

    # cols = ["indicator_id","Activity","LibraryName","CollectionFrequency","financialYear","Total","April","May","June","Q1","July","August","September","Q2","October","November","December","Q3","January","February","March","Q4","Polarity"]
    # df = df.reindex(columns=cols)
    cols = ["indicator_id","Activity","LibraryName","CollectionFrequency","financialYear","Total","Apr","May","Jun","Q1","Jul","Aug","Sep","Q2","Oct","Nov","Dec","Q3","Jan","Feb","Mar","Q4","Polarity"]
    df = df.reindex(columns=cols)

    # Rename some of the column names
    df.rename(columns = {'Apr':'April','Jun':'June','Jul':'July','Sep':'September'}, inplace = True)
    df.rename(columns = {'Oct':'October','Nov':'November','Dec':'December','Jan':'January'}, inplace = True)
    df.rename(columns = {'Feb':'February','Mar':'March'}, inplace = True)

    # Clean the NaN with zero
    df.replace(np.nan, 0.0, inplace = True)

    df.to_csv('../db/kpi/clean_2.csv', index=False)
    
transform()