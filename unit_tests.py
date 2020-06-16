import unittest
import os

from backend.table import sql_create_personal_details_table as table
from backend.sqliteStuff import SQLite, add_name, delete_name, select_with_glob


class SQLiteTests(unittest.TestCase):
    def test_01_create_a_database_file(self):
        sql = SQLite(True)
        file = os.path.isfile(sql.db_file)
        self.assertFalse(file, msg='Tastcase database detected!')
        sql.create_connection()
        file = os.path.isfile(sql.db_file)
        self.assertTrue(file, msg='Creating database failed')
        sql.conn.close()
        os.remove(sql.db_file)

    def test_02_connect_to_database(self):
        sql = SQLite(True)
        conn1 = None
        conn2 = None
        conn2 = sql.create_connection()
        self.assertNotEqual(conn1, conn2, msg='Connection failed')
        conn2.close()
        os.remove(sql.db_file)

    # This test should test if you added a table to the database, but it doesn't work. Not sure how to test that
    # def test_create_table(self):
    #     sql = SQLite(True)
    #     sql.create_connection()
    #     sql.create_table(sql.conn, table)
    #     cursor = sql.conn.cursor()
    #     table_check = cursor.execute("SELECT name FROM sqlite_master WHERE name='personal_details';")
    #     self.assertEqual(table_check, 'personal_details', msg='Creating table failed')
    #     sql.conn.close()
    #     os.remove(sql.db_file)

    def test_03_add_record(self):
        sql = SQLite(True)
        file = os.path.isfile(sql.db_file)
        self.assertFalse(file, msg='Tastcase database detected!')
        sql.create_connection()
        sql.create_table(sql.conn, table)
        row1 = 0
        row2 = 0
        with sql.conn:
            detail = ['Sarah Connor', '12 Lambert St', '123 345 567']
            row1 = add_name(sql.conn, detail)
            detail = ['Jesse Pinkman', '23 Lame Road', '323 453 876']
            row2 = add_name(sql.conn, detail)
        self.assertEqual(row1, 1)
        self.assertEqual(row2, 2)
        sql.conn.close()
        os.remove(sql.db_file)

    def test_04_delete_record(self):
        sql = SQLite(True)
        file = os.path.isfile(sql.db_file)
        self.assertFalse(file, msg='Tastcase database detected!')
        sql.create_connection()
        sql.create_table(sql.conn, table)
        result = 1
        with sql.conn:
            detail = ['Sarah Connor', '12 Lambert St', '123 345 567']
            add_name(sql.conn, detail)
            detail = ['Jesse Pinkman', '23 Lame Road', '323 453 876']
            id = add_name(sql.conn, detail)
            delete_name(sql.conn, id)
            cur = sql.conn.cursor()
            cur.execute("SELECT * FROM personal_details WHERE {} GLOB '{}'".format('name', '*Jesse*'))
            rows = cur.fetchall()
            result = len(rows)
        self.assertEqual(result, 0, msg='Did not remove properly')
        sql.conn.close()
        os.remove(sql.db_file)

    def test_05_glob_filter(self):
        sql = SQLite(True)
        file = os.path.isfile(sql.db_file)
        self.assertFalse(file, msg='Tastcase database detected!')
        sql.create_connection()
        sql.create_table(sql.conn, table)
        result = 0
        with sql.conn:
            detail = ['Sarah Connor', '12 Lambert St', '123 345 567']
            add_name(sql.conn, detail)
            detail = ['Jesse Pinkman', '23 Lame Road', '323 453 876']
            add_name(sql.conn, detail)
            detail = ['Cole Finklang', '88 Fancy St', '324 666 876']
            add_name(sql.conn, detail)
            rows = select_with_glob(sql.conn, 'name', '*ink*')
            result = len(rows)
        self.assertEqual(result, 2, msg='Glob filter failed')
        sql.conn.close()
        os.remove(sql.db_file)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
