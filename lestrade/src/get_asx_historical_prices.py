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

def connect_db():
    try:
        conn=psycopg2.connect("dbname='vagrant' host='localhost' user='vagrant' password='password'")
        return conn
    except Exception as e:
        print(e)
        print "I am unable to connect to the database."

def get_start_date(conn):
    try:
        cur = conn.cursor()
        cur.execute('select min(time) from trade')
        res = cur.fetchall()
        d = res[0][0]
        print 'start date: %s'%d
        return d
    except Exception as e:
        print(e)

def get_trade_codes(conn):
    cur = conn.cursor()
    try:
        cur.execute("""select symbol from trade group by symbol""")
        results = cur.fetchall()
        symbols = []
        for r in results:
            symbols.append(r[0])

        print str(symbols)
        return symbols

    except Exception as e:
        print "can't select symbols"

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def write_snapshot(conn, code, open, high, low, close, turnover, date):
    try:
        cur = conn.cursor()
        cur.execute("""
        insert into price_snapshot(symbol, open, high, low, close, turnover, date) 
               values (%s, %s, %s, %s, %s, %s, %s)
        """, (code, open, high, low, close, turnover, date))
        conn.commit()
        print 'wrote snapshot %s %s %s'%(date, code, close)
    except psycopg2.IntegrityError as e:
        conn.rollback()

hist_arch = None
def get_hist_arch():
   
    global hist_arch
    if hist_arch is None:
        weekurl = 'https://www.asxhistoricaldata.com/data/2013-2016.zip'
        headers = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(weekurl, headers=headers)
        if (r.status_code == 200):
            hist_arch = ZipFile(StringIO(r.content))
    
        print 'retrieved 2013-2016 archive'
    return hist_arch

h12017_arch = None
def get_h12017_arch():
    global h12017_arch
    if h12017_arch is None:
        weekurl = 'https://www.asxhistoricaldata.com/data/2017jan-june.zip'
        headers = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(weekurl, headers=headers)
        if (r.status_code == 200):
            h12017_arch = ZipFile(StringIO(r.content))
        print 'retrieved H1 2017 archive'
    return h12017_arch

h22017_arch = None
def get_h22017_arch():
    global h22017_arch
    if h22017_arch is None:
        weekurl = 'https://www.asxhistoricaldata.com/data/2017july-december.zip'
        headers = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(weekurl, headers=headers)
        if (r.status_code == 200):
            h22017_arch = ZipFile(StringIO(r.content))
        print 'retrieved H2 2017 archive'
    return h22017_arch

def get_week_arch(date):

    # find the next friday (data is grouped into batches dated the friday of the week)
    status = 404
    next_friday = date
    cnt = 0;
    while status != 200 and cnt < 7:
        weekurl = next_friday.strftime('https://www.asxhistoricaldata.com/data/week%Y%m%d.zip')
        headers = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(weekurl, headers=headers)
        status = r.status_code
        print '%s -> %s'%(weekurl,status)
        next_friday = next_friday + datetime.timedelta(days=1)
        cnt += 1
        
    print 'retrieved data for week %s'%str(next_friday)
    try:
        return ZipFile(StringIO(r.content))
    except Exception as e:
        print(e)
    return None

def get_asx_data_for(date, symbols, conn):
    
    if date < datetime.datetime(2017, 1,1):
        z = get_hist_arch()
    elif date < datetime.datetime(2017, 7, 1):
        z = get_h12017_arch()
    elif date < datetime.datetime(2018, 1, 1):
        z = get_h22017_arch()
    else:
        z = get_week_arch(date)
    
    if z is None:
        return

    filename = datetime.datetime.strftime(date, '%Y%m%d')
    for i in z.infolist():
        if (filename in i.filename):
            f = z.open(i.filename)
            reader = csv.DictReader(f, ['symbol','date','open','high','low','close','turnover'])
            for row in reader:
                if (row['symbol'] in symbols):
                    write_snapshot(conn,
                        row['symbol'], 
                        row['open'], 
                        row['high'], 
                        row['low'], 
                        row['close'], 
                        row['turnover'], 
                        datetime.datetime.strptime(row['date'], '%Y%m%d'))

with connect_db() as conn:
    # get start date argument 
    if len(sys.argv) == 2:
        start_date = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d')
    else:
        start_date = get_start_date(conn)

    symbols = get_trade_codes(conn)
    today = datetime.datetime.now()
    while (start_date < today):
        if start_date.weekday() < 5:
            get_asx_data_for(start_date, symbols, conn)
        start_date += datetime.timedelta(days=1)
