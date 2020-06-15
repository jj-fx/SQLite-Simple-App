from backend.keyboard_input import command_line_input
from backend.sqliteStuff import SQLite, add_name, delete_name
from backend.table import sql_create_personal_details_table as table

import click


@click.command()
@click.option('--db', default=False, help='Used to create a database', type=bool)
@click.option('--add', default=0, help='How many records would you like to add?', type=int)
@click.option('--remove', default=0, help='Would you like to remove a record? (id)', type=int)
@click.option('--display', default=False, help='Would you like to display all records?', type=bool)
def main(db, add, remove, display):
    if db:
        # Create connection and object
        sql = SQLite()
        sql.create_connection()
        # Create table
        sql.create_table(sql.conn, table)

        with sql.conn:
            for i in range(add):
                print('Create record number {}:'.format(str(i + 1)))
                detail = command_line_input()
                add_name(sql.conn, detail)

        # close the connection
        sql.conn.close()

    if not remove == 0:
        # Create connection and object
        sql = SQLite()
        sql.create_connection()
        with sql.conn:
            delete_name(sql.conn, remove)

        # close the connection
        sql.conn.close()

    if display:
        # Create connection and object
        sql = SQLite()
        sql.create_connection()
        with sql.conn:
            # do stuff
            cursor = sql.conn.execute("SELECT id, name, address, phone_number from personal_details")
            for row in cursor:
                print("id: {}\tname: {}\taddress: {}\tphone_number: {}".format(row[0], row[1], row[2], row[3]))


        # close the connection
        sql.conn.close()


if __name__ == '__main__':
    main()
