import pandas as pd 
import sqlite3


df = pd.read_csv('buddymove_holidayiq.csv')
print(df.shape)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

df.to_sql('review', con=conn)

curs.execute('SELECT COUNT(*) FROM review;')
print('Row Count:', curs.fetchall()[0])

QUERY = """
    SELECT Nature, Shopping
    FROM review 
    WHERE Nature >= 100 AND Shopping >= 100;
"""

curs.execute(QUERY)
print('Reviews:', curs.fetchall()[:20])
