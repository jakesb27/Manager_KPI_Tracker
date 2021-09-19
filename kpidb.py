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
    MANAGER=:manager AND
    ACTIVE='Y'
"""

all_act_collectors_sql = """
SELECT
    USER_ID,
    FIRST_NAME || " " || LAST_NAME
FROM
    COLL
WHERE
    ACTIVE='Y'
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
    GOAL3_GOAL=:goal3,
    ACTIVE=:active
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
        RPC_TOTAL
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

monthly_rpcs_ph_sql = """
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

monthly_conn_sql = """
SELECT *
FROM(
    SELECT
        KPI_DATE,
        CONN_TOTAL
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

monthly_conn_ph_sql = """
SELECT *
FROM(
    SELECT
        KPI_DATE,
        round(CONN_PER_HOUR, 2) "CONN_PER_HOUR"
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

monthly_conv_sql = """
SELECT *
FROM(
    SELECT
        KPI_DATE,
        CONV_RATE
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

monthly_fees_sql = """
SELECT *
FROM(
    SELECT
        KPI_DATE,
        FEES_TOTAL
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

monthly_totals_sql = """
SELECT *
FROM(
    SELECT
        MONTH_DATE,
        TOTAL_COLL
    FROM
        TOTALS
    WHERE
        USER_ID=:user_id
    ORDER BY
        MONTH_DATE DESC
    LIMIT 6
    )
ORDER BY
    MONTH_DATE ASC
"""

weekly_rpcs_sql = """
SELECT *
FROM(
    SELECT
        WEEK_DATE,
        RPC_TOTAL
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

weekly_rpcs_ph_sql = """
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

weekly_conn_sql = """
SELECT *
FROM(
    SELECT
        WEEK_DATE,
        CONN_TOTAL
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

weekly_conn_ph_sql = """
SELECT *
FROM(
    SELECT
        WEEK_DATE,
        round(CONN_PER_HOUR, 2) "CONN_PER_HOUR"
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

weekly_conv_sql = """
SELECT *
FROM(
    SELECT
        WEEK_DATE,
        CONV_RATE
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

weekly_fees_sql = """
SELECT *
FROM(
    SELECT
        WEEK_DATE,
        FEES_TOTAL
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

update_desks_sql = """
UPDATE
    COLL
SET
    DESK=:desk
WHERE
    USER_ID=:user_id    
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


def all_act_collectors():
    """Simple function used to query SQLite database for all collectors."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(all_act_collectors_sql)
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
    """Simple function used to query SQLite database for monthly RPC's."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(monthly_rpcs_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def monthly_rpcs_ph(collector):
    """Simple function used to query SQLite database for monthly RPC's per hour."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(monthly_rpcs_ph_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def monthly_conn(collector):
    """Simple function used to query SQLite database for monthly Connects."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(monthly_conn_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def monthly_conn_ph(collector):
    """Simple function used to query SQLite database for monthly Connects per hour."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(monthly_conn_ph_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def monthly_conv(collector):
    """Simple function used to query SQLite database for monthly conversion rate."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(monthly_conv_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def monthly_fees(collector):
    """Simple function used to query SQLite database for monthly fees."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(monthly_fees_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def monthly_totals(collector):
    """Simple function used to query SQLite database for monthly totals."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(monthly_totals_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def weekly_rpcs(collector):
    """Simple function used to query SQLite database for weekly RPC's."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(weekly_rpcs_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def weekly_rpcs_ph(collector):
    """Simple function used to query SQLite database for weekly RPC's per hour."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(weekly_rpcs_ph_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def weekly_conn(collector):
    """Simple function used to query SQLite database for weekly connects."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(weekly_conn_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def weekly_conn_ph(collector):
    """Simple function used to query SQLite database for weekly connects per hour."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(weekly_conn_ph_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def weekly_conv(collector):
    """Simple function used to query SQLite database for weekly conversion rate."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(weekly_conv_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def weekly_fees(collector):
    """Simple function used to query SQLite database for weekly fees."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(weekly_fees_sql, (collector, ))
    rows = cur.fetchall()
    conn.close()
    return rows


def update_desks(data):
    """Simple function used to update collector desk details from CDS database."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(update_desks_sql, data)
    conn.commit()
    conn.close()
