import os
import sqlite3
from sqlite3 import Error


def get_db_path():
    db_file = 'animal.db'
    path = os.getcwd()
    return os.path.join(path, db_file)


def add_name(conn, details):
    sql = ''' INSERT INTO personal_details(name, address, phone_number) VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, details)
    return cur.lastrowid


def delete_name(conn, id):
    sql = 'DELETE FROM personal_details WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def select_with_glob(conn, column, glob):
    cur = conn.cursor()
    cur.execute("SELECT * FROM personal_details WHERE {} GLOB '{}'".format(column, glob))

    rows = cur.fetchall()

    data = list()
    for row in rows:
        data.append(row)
        print(row)
    return data


class SQLite:
    def __init__(self):
        self.db_file = get_db_path()
        self.conn = None

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            return self.conn
        except Error as e:
            print(e)

    def create_table(self, connection, table):
        if connection is not None:
            try:
                c = connection.cursor()
                c.execute(table)
            except Error as e:
                print(e)

        else:
            print("Error! cannot create the database connection.")
