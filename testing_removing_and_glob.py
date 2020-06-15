from backend.sqliteStuff import delete_name, SQLite, select_with_glob

sql = SQLite()
sql.create_connection()

# delete:
# delete_name(sql.conn, 1)

# blob:
select_with_glob(sql.conn, 'name', '*an*')
