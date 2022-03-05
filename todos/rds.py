import sys
import logging
import os
import pymysql

# rds settings


logger = logging.getLogger()
logger.setLevel(logging.INFO)

rds_host = "rds-instance-endpoint"
name = os.environ['DB_NAME']
password = os.environ['db_password']
db_name = os.environ['db_name_user']


def handler():

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except Exception as e:
        raise e('This is broken')

    logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

    """
    This function fetches content from MySQL RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table Employee ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        cur.execute('insert into Employee (EmpID, Name) values(1, "Joe")')
        cur.execute('insert into Employee (EmpID, Name) values(2, "Bob")')
        cur.execute('insert into Employee (EmpID, Name) values(3, "Mary")')
        conn.commit()
        cur.execute("select * from Employee")
        for row in cur:
            item_count += 1
            logger.info(row)
            # print(row)
    conn.commit()

    return "Added %d items from RDS MySQL table" % (item_count)
