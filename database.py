import pymysql
from pymysql.constants import CLIENT

def create_conn(dbname):
    conn = pymysql.connect(host='localhost',
                       port=3360,
                       user='root',
                       password='100560',
                       database=dbname,
                       client_flag=CLIENT.MULTI_STATEMENTS)
    return conn


def run_sql(sql, dbname):
    conn = create_conn(dbname)
    conn.connect()
    cursor = conn.cursor()
    # print(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def run_query(sql, dbname):
    conn = create_conn(dbname)
    conn.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result