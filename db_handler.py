import psycopg2
import sys, os
import numpy as np
import pandas as pd
import db_credentials as creds
import pandas.io.sql as psql

conn_string = "host=" + creds.PGHOST + " port=" + "5432" + " dbname=" + creds.PGDATABASE + " user=" + creds.PGUSER \
              + " password=" + creds.PGPASSWORD
conn = psycopg2.connect(conn_string)

print("Connected!")

cursor = conn.cursor()


def load_data(table):
    sql_command = "SELECT * FROM {}".format(str(table))
    print(sql_command)

    # Load the data
    data = pd.read_sql(sql_command, conn)

    print(data.shape)

    return data


def create_table():

    try:
        sql_command = (
            """
            CREATE TABLE tickers (
                ticker_id SERIAL PRIMARY KEY,
                ticker_name VARCHAR(255) NOT NULL
            )
            """
        )
        # read the connection parameters
        # connect to the PostgreSQL server
        # create table one by one
        cursor.execute(sql_command)
        # close communication with the PostgreSQL database server
        cursor.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


create_table()
