#! /usr/bin/python

import glob
import csv
import sys
import psycopg2
from datetime import datetime

acc_line = 3;
dat_line = 7;

def connect_db():
    try:
        conn=psycopg2.connect("dbname='vagrant' host='localhost' user='vagrant' password='password'")
        return conn
    except Exception as e:
        print(e)
        print "I am unable to connect to the database."

def write_trade(conn, account, code, price, size, side, date, brokerage, trade_id):
    try:
        cur = conn.cursor()
        cur.execute('insert into trade(symbol, account, price, volume, side, brokerage, time, exchange_trade_id) values (%s, %s, %s, %s, %s, %s, %s, %s)',
        (code, account, price, size, side, brokerage, date, trade_id))
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()

def get_account(conn, account_no):
    try:
        cur = conn.cursor()
        cur.execute('select id from account where account_no = %s'%(account_no))
        fetch = cur.fetchall()
        return fetch[0][0]
    except psycopg2.IntegrityError as e:
        conn.rollback()

def parse_file(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)
        line_cnt = 1;
        with connect_db() as conn:
            trade_cnt = 0
            for row in csvreader:
                if line_cnt == acc_line:
                    account = row[0][9:16]
                    account_id = get_account(conn, account)
                if line_cnt >= dat_line:
                    if len(row) ==0:
                        break

                    code = row[0]
                    date = datetime.strptime(row[2], '%d/%m/%Y')
                    side = row[3][0:1]
                    size = row[4]
                    price = row[5]
                    brokerage = row[7]
                    trade_id = row[9]
                    write_trade(conn, account_id, code, price, size, side, date, brokerage, trade_id)
                    trade_cnt += 1
                line_cnt += 1
        print '%s - %d trades'%(filename, trade_cnt)

files = glob.glob('*.csv')
for filename in files:
    parse_file(filename)
