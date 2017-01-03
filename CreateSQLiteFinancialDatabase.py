from pandas import DataFrame
from pandas_datareader import data
from datetime import datetime
import sqlite3
import csv

# connects to and possibly creates a database
cnx = sqlite3.connect('FinancialAnalysis.db')
c = cnx.cursor()

# defines and reads tickerSymbols.csv
with open('tickerSymbols.csv') as csvfile:
    ticker = csv.reader(csvfile, delimiter = ',')

    for row in ticker:
        try:
            # gathers data from the internet in a pandas DataFrame
            temp = data.DataReader(row[0], 'yahoo', datetime(2014,1,6), datetime(2014,1,11))

            # takes the pandas DataFrame and writes it to an sqlite table if it doesnt already exist
            temp.to_sql(row[0], cnx, if_exists = 'replace', flavor = 'sqlite')
        except:
            pass
