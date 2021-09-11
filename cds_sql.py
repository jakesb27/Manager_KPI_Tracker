import cx_Oracle
import datetime
from datetime import date
from cryptography.fernet import Fernet


# Connection credentials
dsn_tns = cx_Oracle.makedsn("172.16.33.11", 1521, service_name="CMRE")

# Today's date in CDS
cds_date = 153403 + (date.today() - date(2021, 1, 1)).days


# SQL statement used to get desk totals
desk_tot_sql = """
SELECT
    DSK.DSK_GOAL,
    DSK.DSK_MTD3,
    DSK.DSK_MTD4,
    (DSK.DSK_MTD3 + DSK.DSK_MTD4),
    DSK.DSK_MTD7
FROM
    CDS.DSK DSK
WHERE
    DSK.DSK_CODE=:desk
"""

# SQL statement to get active desks
act_desks_sql = """
SELECT
    DSK.DSK_CODE,
    USR.USR_CODE
FROM CDS.DSK DSK
    JOIN CDS.USR USR ON USR.USR_DEF_MOT_DESK=DSK.DSK_CODE
WHERE
    DSK.DSK_DESK_GROUP IN ('ANC', 'SHC', 'CSA', 'CSI', 'CSU')
ORDER BY
    DSK.DSK_CODE
"""


def cds_password():
    """Function used open encrypted file with Oracle DB password."""
    key = b'uQiGedrG3Xq9NS3d5RphnZON59Sn-nU3-J5crpQp-Wo='
    cipher_suite = Fernet(key)
    with open(r'\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\cds_pw.bin', 'rb') as file_object:
        for line in file_object:
            enc_pw = line
    un_ciph = (cipher_suite.decrypt(enc_pw))
    pwd = bytes(un_ciph).decode("utf-8")
    return pwd


def get_desk_totals(desk):
    """Function used to connect to Oracle DB and run SQL query."""
    try:
        # Connect to oracle database
        with cx_Oracle.connect(user="CDS", password=cds_password(), dsn=dsn_tns) as connection:
            with connection.cursor() as cursor:
                try:
                    # Execute query
                    cursor.execute(desk_tot_sql, (desk, ))
                    results = cursor.fetchall()
                    # Returns results of query
                    return results
                except cx_Oracle.Error as error:
                    # Saves error to error file for debugging
                    with open(r'Desk Totals Oracle Query Errors.txt', 'w') as file:
                        file.write(f"Desk Totals query execution error: ** {error} **")
    except cx_Oracle.Error as error:
        # Saves error to error file for debugging
        with open(r'Oracle Connection Errors.txt', 'w') as file:
            file.write(f"Oracle connection error: ** {error} **")


def get_act_desks():
    """Function used to update CMRE database with collector's desk and goal."""
    try:
        # Connect to oracle database
        with cx_Oracle.connect(user="CDS", password=cds_password(), dsn=dsn_tns) as connection:
            with connection.cursor() as cursor:
                try:
                    # Execute query
                    cursor.execute(act_desks_sql)
                    results = cursor.fetchall()
                    # Returns results of query
                    return results
                except cx_Oracle.Error as error:
                    # Saves error to error file for debugging
                    with open(r'Update CMRE DB Oracle Query Errors.txt', 'w') as file:
                        file.write(f"Desk Totals query execution error: ** {error} **")
    except cx_Oracle.Error as error:
        # Saves error to error file for debugging
        with open(r'Oracle Connection Errors.txt', 'w') as file:
            file.write(f"Oracle connection error: ** {error} **")
