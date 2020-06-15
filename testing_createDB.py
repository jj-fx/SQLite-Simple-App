from backend.keyboard_input import command_line_input
from backend.sqliteStuff import SQLite, add_name
from backend.table import sql_create_personal_details_table as table

# Create connection and object
sql = SQLite()
sql.create_connection()
# Create table
sql.create_table(sql.conn, table)

# Add a name
# details = ('John Doe', '123 Nuke Street', '098 765 432')
with sql.conn:
    for i in range(1):
        print('Give name {}'.format(str(i)))
        detail = command_line_input()
        name_id = add_name(sql.conn, detail)
