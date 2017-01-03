from pandas import DataFrame
from pandas_datareader import data
from datetime import datetime
import sqlite3
import csv
import os

# connects to and possibly creates a database
cnx = sqlite3.connect('FinancialAnalysis.db')
c = cnx.cursor()

# defines and reads tickerSymbols.csv
with open('tickerSymbols.csv') as csvfile:
    ticker = csv.reader(csvfile, delimiter = ',')

    for row in ticker:

        # Financial Data doesnt go back the same length of time for every company.
        # Because of this, I need a loop to try and find the maximum amount of data
        # I can extract without an eroor occurring
        year = 2000
        month = 1
        while year < 2017:

            try:
                # gathers data from the internet in a pandas DataFrame
                temp = data.DataReader(row[0], 'yahoo', datetime(year,month,1), datetime(2016,12,30))
                # writes the maximum amount of data to an sqlite table
                temp.to_sql(row[0], cnx, if_exists = 'replace', flavor = 'sqlite')
                # if it works then were done with the while loop so we break out
                break
            except:
                # if it doesnt work then try the next month
                if month == 12:
                    year = year + 1
                    month = 1
                else:
                    month = month + 1

        # overall exception incase everything goes south
        if year == 2017:
            # records the symbols that didnt correctly pull data
            with open('failedSymbols.csv', 'a') as myfile:
                myfile.write('%s,' %row[0])

# notification that program has finished
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' %(3,500))
