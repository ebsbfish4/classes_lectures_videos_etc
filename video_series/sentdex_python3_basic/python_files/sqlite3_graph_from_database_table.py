#! python3

import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

# random note: size of database is almost entirely dependent on the number of
# characters, so if you have a timestamp with 8 trailing digits, for example,
# you would most likely be better off shortening them.

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stufftoPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(14532234, '2016-01-01', 'Python', 5)")
    conn.commit()
    # Essential to close after in order to not waste memory
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix,date,keyword,value))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM stuffToPlot WHERE value=2')
    data = c.fetchall()
    for row in data:
        print(row)

def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        #print(row[0])
        #print (datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


        
graph_data()
#read_from_db()


#create_table()
#data_entry()

#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)

c.close()
conn.close()
