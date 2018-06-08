#!/usr/bin/python
import sys
import ssl
from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
from datetime import datetime
from datetime import timedelta
import datetime
import psycopg2
import httplib
import requests
import csv

#jhttplib.debuglevel = 1
#httplib.HTTPConnection.debuglevel = 1

# Try to connect

try:
    conn=psycopg2.connect("dbname='vagrant' host='localhost' user='vagrant' password='password'")
except Exception as e:
    print(e)
    print "I am unable to connect to the database."
    
cur = conn.cursor()
try:
    cur.execute("""select symbol from trade group by symbol""")
except Exception as e:
    print "can't select symbols"

results = cur.fetchall()
symbols = []
for r in results:
    symbols.append(r[0])
print str(symbols)

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

# get start date argument 
if len(sys.argv) == 2:
    start_date = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d')

# find the next friday (data is grouped into batches dated the friday of the week)
# iterate by fridays until past today.
next_friday = next_weekday(start_date, 4)
today = datetime.datetime.now()

def getdata2(url):
    # need to spoof a browser as the site rejects python user-agent.
    headers = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    if (r.status_code == 200):
        z = ZipFile(StringIO(r.content))
        for i in z.infolist():
            if (i.filename.endswith('txt')):
                f = z.open(i.filename)
                reader = csv.DictReader(f, ['symbol','date','open','high','low','close','turnover'])
                for row in reader:
                    if (row['symbol'] in symbols):
                        try:
                            cur.execute("""
                            insert into price_snapshot(symbol, open, high, low, close, turnover, date) values (%s, %s, %s, %s, %s, %s, %s)
                            """, (row['symbol'], row['open'], row['high'], row['low'], row['close'], row['turnover'], datetime.datetime.strptime(row['date'], '%Y%m%d')))
                            conn.commit()
                        except psycopg2.IntegrityError as e:
                            conn.rollback()


while (next_friday < today):
    weekurl = next_friday.strftime('https://www.asxhistoricaldata.com/data/week%Y%m%d.zip')
    getdata2(weekurl)
    next_friday += datetime.timedelta(days=7)
