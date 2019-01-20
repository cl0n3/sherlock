#!/usr/bin/python

import psycopg2

try:
    conn = psycopg2.connect("dbname='vagrant' host='localhost' user='vagrant' password='password'")
except Exception as e:
    print(e)

cur = conn.cursor()

# get all the transactions in the income category
try:
    cur.execute("""
select month(date), sum(amount)
  from transaction t, transaction_category tc, category_group cg, reporting_group rg
 where t.category = tc.id
   and tc.category_group = cg.id
   and cg.reporting_group = rg.id
   and rg.name = 'Income'
group by month(date)
    """

