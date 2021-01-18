import sqlite3 
from query import *


def establish_connection(db='rpg_db.sqlite3'):
    return sqlite3.connect(db)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == '__main__':
    #connect to db
    conn = establish_connection()
    #create cursor
    curs = conn.cursor()
    tc_results = execute_query(curs, TOTAL_CHARACTERS)
    print('TOTAL_CHARACTERS:', tc_results[0])
    
    ts_results = execute_query(curs, TOTAL_SUBCLASS)
    print('TOTAL_SUBCLASS:', ts_results[0])
    
    ti_results = execute_query(curs, TOTAL_ITEMS)
    print('TOTAL_ITEMS:', ti_results[0])

    tw_results = execute_query(curs, TOTAL_WEPONS)
    print('TOTAL_WEPONS:', tw_results[0])

    nw_results = execute_query(curs, NON_WEPONS)
    print('NON_WEPONS:', nw_results[0])

    ci_results = execute_query(curs, CHARACTER_ITEMS)
    print('CHARACTER_ITEMS:', ci_results[:20])
