import sqlite3
from sqlite3 import Error

db_file = r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\CMRE.db"

coll_details_sql = """
SELECT *
FROM
    COLL
WHERE
    USER_ID=:user
"""

my_collectors_sql = """
SELECT
    USER_ID,
    FIRST_NAME || " " || LAST_NAME
FROM
    COLL
WHERE
    MANAGER=:manager
"""

all_collectors_sql = """
SELECT
    USER_ID,
    FIRST_NAME || " " || LAST_NAME
FROM
    COLL
"""

daily_kpis_sql = """
SELECT *
FROM
    DAILY_KPIS
WHERE
    DAY=strftime('%d', 'now', 'localtime') AND
    USER_ID=:collector
"""

update_coll_sql = """
UPDATE COLL
SET
    LAST_NAME=:last,
    FIRST_NAME=:first,
    EMAIL=:email,
    EXT=:ext,
    MANAGER=:manager,
    USER_GROUP=:group,
    GOAL1_DESC=:desc1,
    GOAL1_BASE=:base1,
    GOAL1_GOAL=:goal1,
    GOAL2_DESC=:desc2,
    GOAL2_BASE=:base2,
    GOAL2_GOAL=:goal2,
    GOAL3_DESC=:desc3,
    GOAL3_BASE=:base3,
    GOAL3_GOAL=:goal3
WHERE
    ULTIPRO_ID=:primary_key
"""

managers_sql = """
SELECT NAME
FROM
    MANAGERS
"""

monthly_rpcs_sql = """
SELECT *
FROM(
    SELECT
        KPI_DATE,
        round(RPC_PER_HOUR, 2) "RPC_PER_HOUR"
    FROM
        MONTHLY_KPIS
    WHERE
        USER_ID=:user_id
    ORDER BY
        KPI_DATE DESC
    LIMIT 6
    )
ORDER BY
    KPI_DATE ASC
"""

weekly_rpcs_sql = """
SELECT *
FROM(
    SELECT
        WEEK_DATE,
        round(RPC_PER_HOUR, 2) "RPC_PER_HOUR"
    FROM
        WEEKLY_KPIS
    WHERE
        USER_ID=:user_id
    ORDER BY
        WEEK_DATE DESC
    LIMIT 5
    )
ORDER BY
    WEEK_DATE ASC
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


def coll_details(coll):
    """Simple function used to query SQLite database for a collector's details."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(coll_details_sql, (coll,))
    rows = cur.fetchall()
    conn.close()
    return rows[0]


def my_collectors(manager):
    """Simple function used to query SQLite database for a manager's collectors."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(my_collectors_sql, (manager,))
    rows = cur.fetchall()
    conn.close()
    return rows


def all_collectors():
    """Simple function used to query SQLite database for all collectors."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(all_collectors_sql)
    rows = cur.fetchall()
    conn.close()
    return rows


def daily_kpis(collector):
    """Simple function used to query SQLite database for collectors' stats."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(daily_kpis_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def update_coll(data):
    """Simple function used to update the COLL table of the SQLite database."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(update_coll_sql, data)
    conn.commit()
    conn.close()


def managers():
    """Simple function used to query SQLite database for managers."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(managers_sql)
    rows = cur.fetchall()
    conn.close()
    mgr_list = [man[0] for man in rows]
    return mgr_list


def monthly_rpcs(collector):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(monthly_rpcs_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def weekly_rpcs(collector):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(weekly_rpcs_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows
