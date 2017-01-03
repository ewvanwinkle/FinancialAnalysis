from yahoo_finance import Share
import csv

with open('tickerSymbols.csv') as csvfile:
    ticker = csv.reader(csvfile, delimiter = ',')
    for row in ticker:
        sharePrice = Share(row)
        print row, sharePrice.get_open()
