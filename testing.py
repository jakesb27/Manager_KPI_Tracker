from datetime import date, timedelta
import sqlite3
import time
from sqlite3 import Error

db_file = r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\CMRE.db"

my_sql = """
SELECT
    ISSUE_DATE
FROM
    REVIEWS
WHERE
    RVW_TYPE='One on One' AND
    ISSUE_DATE BETWEEN :sdate AND :edate
"""


def create_connection():
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def my_query(dates):
    """Simple function used to query SQLite database for a collector's details."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(my_sql, dates)
    rows = cur.fetchall()
    conn.close()
    return rows


new_list = []
day_count = 0
this_month = date.today().replace(day=1).strftime('%Y-%m')
end_date = start_date - timedelta(days=210)
while day_count < 181:
    new_list.append((start_date - timedelta(days=day_count)).strftime('%Y-%m'))
    day_count += 30

data = my_query([end_date.strftime('%Y-%m-%d'), date.today().strftime('%Y-%m-%d')])
print(new_list)
print(data)
