# Project      : Showcase Project
# Program Name : load_data.py
# Description  : Load the transformed data to data warehouse (mySQL)
#              : Load a consolidated art & culture csv files to database
#              :    1) kpi.csv
#              :    2) kpi-percentage.csv
#              :    3) indicator.csv
# Outputs      : Data in the remote database (e.g. MySQL/PostgreSQL under AWS)
# Developers   : Samuel Ko
###############################################################################################

import pandas as pd
import mysql_connector as db
import os
from dotenv import load_dotenv

def insert_to_kpi_db():
    load_dotenv()
 
    # Establish the database connection
    connection = db.mysql_connect()

    ############### Upload consolidated kpi.csv #############
    dataPath_db = os.environ.get("kpiPATH_db")
    fileName = dataPath_db + 'kpi.csv'
    # inserting stocks data to MySQL database (or to RDS in AWS)
    kpiData = pd.read_csv (fileName)   
    for row in kpiData.itertuples():
        sql = """
        INSERT INTO kpi (
            indicator_id, financialYear, April, May,
            June, Q1, July, August, September,
            Q2, October, November, December, 
            Q3, January, February, March, Q4)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """ 
        val = (row.indicator_id, row.financialYear, 
        row.April, row.May, row.June, row.Q1,
        row.July, row.August, row.September, row.Q2,
        row.October, row.November, row.December, row.Q3,
        row.January, row.February, row.March, row.Q4)
        cursor = connection.cursor()
        cursor.execute(sql, val)

    ####################### Upload kpi-percentage.csv #####################
    # inserting CPI data to MySQL database (or to RDS in AWS)
    dataPath_db = os.environ.get("kpiPATH_db")
    fileName = dataPath_db + 'kpi-percentage.csv'
    cpiData = pd.read_csv (fileName)   
    kpi_percentageData = pd.read_csv (fileName)   
    for row in kpi_percentageData.itertuples():
        sql = """
        INSERT INTO kpi_percentage (
            indicator_id, financialYear, April, May,
            June, Q1, July, August, September,
            Q2, October, November, December, 
            Q3, January, February, March, Q4)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """ 
        val = (row.indicator_id, row.financialYear, 
        row.April, row.May, row.June, row.Q1,
        row.July, row.August, row.September, row.Q2,
        row.October, row.November, row.December, row.Q3,
        row.January, row.February, row.March, row.Q4)
        cursor = connection.cursor()
        cursor.execute(sql, val)

    ####################### Upload indicator.csv #####################
    # For four selected stocks, inserting market capacity data 
    # to MySQL database (or to RDS in AWS)
    dataPath_db = os.environ.get("kpiPATH_db")
    fileName = dataPath_db + 'indicator.csv'
    indicatorData = pd.read_csv (fileName)   
    for row in indicatorData.itertuples():
        sql = """
        INSERT INTO indicator (
            indicator_id, Activity, LibraryName, CollectionFrequency,
            Latitude, Longitude, Polarity)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """ 
        val = (row.indicator_id, row.Activity, row.LibraryName, row.CollectionFrequency,
        row.Latitude, row.Longitude, row.Polarity)
        cursor = connection.cursor()
        cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    print("All Data Are Uploaded!.")

def load_data_to_db():
    # Upload all data to MySQL/ RDS in AWS
    # 1) kpi
    # 2) kpi_percentage
    # 3) indicator

    insert_to_kpi_db()

load_data_to_db()