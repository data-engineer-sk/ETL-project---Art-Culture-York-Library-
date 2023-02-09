-- Create Database for libraries data (Act & Culture)
CREATE database if not exists kpi_db;

use kpi_db;

-- Create kpi Table
Create table kpi (
	seqNo int UNSIGNED not null AUTO_INCREMENT,
	indicator_id VARCHAR(12),
    financialYear DATE,
    Total INT(15),
    April INT(15),
    May INT(15),
    June INT(15),
    Q1 INT(15),
    July INT(15),
    August int(15),
    September INT(15),
    Q2 INT(15),
    October INT(15),
    November INT(15),
    December INT(15),
    Q3 INT(15),
    January INT(15),
    February INT(15),
    March INT(15),
    Q4 INT(15),
    PRIMARY KEY (seqNo)
);

-- Create kpi_percentage Table
Create table kpi_percentage (
	seqNo int UNSIGNED not null AUTO_INCREMENT,
	indicator_id VARCHAR(12),
    financialYear DATE,
    Total INT(15),
    April INT(15),
    May INT(15),
    June INT(15),
    Q1 INT(15),
    July INT(15),
    August int(15),
    September INT(15),
    Q2 INT(15),
    October INT(15),
    November INT(15),
    December INT(15),
    Q3 INT(15),
    January INT(15),
    February INT(15),
    March INT(15),
    Q4 INT(15),
    PRIMARY KEY (seqNo)
);

-- Create indicator Table
CREATE TABLE indicator (
	indicator_id VARCHAR(12),
    Activity VARCHAR(200),
    LibraryName VARCHAR(100),
    CollectionFrequency VARCHAR(16),
    Latitude decimal(12,8),
    Longitude decimal(12,8),
    Polarity VARCHAR(12),
    PRIMARY KEY (indicator_id)
);