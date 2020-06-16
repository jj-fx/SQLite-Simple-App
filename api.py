from backend.keyboard_input import command_line_input
from backend.sqliteStuff import SQLite, add_name, delete_name, select_with_glob, select_all
from backend.table import sql_create_personal_details_table as table
from backend.serialization import output_to_csv, output_to_html, output_to_txt

import click


@click.command()
@click.option('--makedb', default=False, help='Creates an empty database with a table', type=bool)
@click.option('--add', default=0, help='Adds X number of records', type=int)
@click.option('--remove', default=0, help='Removing a record with id X (run --display True to see the ids)', type=int)
@click.option('--display', default=False, help='Displays all records', type=bool)
@click.option('--filter', default='', help='Filter db with glob, eg. --filter *Joe*', type=str)
@click.option('--output', default=0, help='Output to: 1-CSV, 2-TXT, 3-HTML', type=int)
def main(makedb, add, remove, display, filter, output):
    if makedb:
        # Create connection and object
        sql = SQLite()
        sql.create_connection()
        # Create table
        sql.create_table(sql.conn, table)
        # close the connection
        sql.conn.close()

    if not add == 0:
        # Create connection and object
        sql = SQLite()
        sql.create_connection()

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
            select_all(sql.conn, display=True)

        # close the connection
        sql.conn.close()

    if len(filter) > 0:
        # Create connection and object
        sql = SQLite()
        sql.create_connection()
        with sql.conn:
            select_with_glob(sql.conn, 'name', filter)

        # close the connection
        sql.conn.close()

    if not output == 0:
        if output == 1:
            output_to_csv('output/output')
        elif output == 2:
            output_to_txt('output/output')
        elif output == 3:
            output_to_html('output/output')
        else:
            pass


if __name__ == '__main__':
    main()
