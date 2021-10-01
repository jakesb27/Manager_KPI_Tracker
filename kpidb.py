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
SELECT
    KPI.USER_ID,
    COLL.USER_GROUP,
    KPI.START_TIME,
    KPI.DAY,
    KPI.RPCS,
    KPI.CONV,
    KPI.LAST_UPDATE
FROM
    DAILY_KPIS KPI
JOIN COLL ON COLL.USER_ID = KPI.USER_ID
WHERE
    DAY=strftime('%d', 'now', 'localtime') AND
    KPI.USER_ID=:collector
"""

add_coll_sql = """
INSERT INTO COLL (
    ULTIPRO_ID,
    LAST_NAME,
    FIRST_NAME,
    USER_ID,
    EMAIL,
    EXT,
    MANAGER,
    USER_GROUP,
    GOAL1_DESC,
    GOAL1_BASE,
    GOAL1_GOAL,
    GOAL2_DESC,
    GOAL2_BASE,
    GOAL2_GOAL,
    GOAL3_DESC,
    GOAL3_BASE,
    GOAL3_GOAL,
    ACTIVE
    )
VALUES (
    :ultipro_id,
    :last_name,
    :first_name,
    :user_id,
    :email,
    :ext,
    :manager,
    :group,
    :desc1,
    :base1,
    :goal1,
    :desc2,
    :base2,
    :goal2,
    :desc3,
    :base3,
    :goal3,
    :active
    )
"""

update_coll_sql = """
UPDATE
    COLL
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

users_with_access_sql = """
SELECT
    NET_NAME
FROM
    MANAGERS
WHERE
    APP_ACCESS=1
"""

current_managers_sql = """
SELECT
    FIRST_NAME
FROM
    MANAGERS
WHERE
    STAFF_MGR=1
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

add_review_sql = """
INSERT INTO REVIEWS (
    REVIEW_ID,
    EMP_ID,
    EMP_USERID,
    DESK,
    EXT,
    EMP_GROUP,
    RVW_LOC,
    ISSUED_BY,
    ISSUE_DATE,
    TOPIC,
    RVW_TYPE,
    DISC_TYPE,
    RVW_NOTES
    )
VALUES (
    :review_id,
    :emp_id,
    :emp_userid,
    :desk,
    :ext,
    :emp_group,
    :rvw_loc,
    :issued_by,
    :issue_date,
    :topic,
    :rvw_type,
    :disc_type,
    :rvw_notes
    )
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


def add_coll(data):
    """Simple function used to add collector to the COLL table of the SQLite database."""
    conn = create_connection()
    cur = conn.cursor()
    try:
        cur.execute(add_coll_sql, data)
        conn.commit()
        conn.close()
        return True
    except Error:
        conn.close()
        return False


def update_coll(data):
    """Simple function used to update the COLL table of the SQLite database."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(update_coll_sql, data)
    conn.commit()
    conn.close()


def users_with_access():
    """Simple function used to query SQLite database for managers."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(users_with_access_sql)
    rows = cur.fetchall()
    conn.close()
    mgr_list = [man[0] for man in rows]
    return mgr_list


def current_managers():
    """Simple function used to query SQLite database for managers."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(current_managers_sql)
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


def add_review(data):
    """Simple function used to add an employee review to the CMRE database."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(add_review_sql, data)
    conn.commit()
    conn.close()


def agent_reviews(search_sql):
    """Simple function used to query SQLite database for employee reviews."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(search_sql)
    rows = cur.fetchall()
    conn.close()
    return rows
