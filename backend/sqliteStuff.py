import os
import sqlite3
from tabulate import tabulate
from sqlite3 import Error


# returns the path to db, relative to where it's called
def get_db_path(unittest=False):
    db_file = 'animal.db'
    if unittest:
        db_file = 'animal_unittest.db'
    path = os.getcwd()
    return os.path.join(path, db_file)


# Adds a record (name, address, phone_number)
def add_name(conn, details):
    sql_command = ''' INSERT INTO personal_details(name, address, phone_number) VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql_command, details)
    conn.commit() # just added
    return cur.lastrowid


# Deletes the record by primary key
def delete_name(conn, id):
    sql = 'DELETE FROM personal_details WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    return cur.lastrowid


# Searches the column for a glob expression and returns records that match
def select_with_glob(conn, column, glob):
    cur = conn.cursor()
    cur.execute("SELECT * FROM personal_details WHERE {} GLOB '{}'".format(column, glob))
    rows = cur.fetchall()
    data = list()
    for row in rows:
        data.append(row)
        print(row)
    return data


def select_all(conn, display=False):
    cur = conn.cursor()
    cur.execute("SELECT * FROM personal_details;")
    rows = cur.fetchall()
    data = list()
    for row in rows:
        data.append(row)
    if display:
        print(tabulate(data, '', tablefmt="psql"))
    return data

# Class for creating db, establishing the connection
class SQLite:
    def __init__(self, unittest=False):
        self.db_file = get_db_path(unittest)
        self.conn = None

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            return self.conn
        except Error as e:
            print(e)

    # creates the table how it's defined in table.py
    def create_table(self, connection, table):
        if connection is not None:
            try:
                c = connection.cursor()
                c.execute(table)
            except Error as e:
                print(e)

        else:
            print("Error! cannot create the database connection.")
