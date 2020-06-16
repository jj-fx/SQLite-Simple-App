from tabulate import tabulate
from backend.sqliteStuff import select_all, SQLite


sql = SQLite()
sql.create_connection()
s = select_all(sql.conn)

table = s

print(tabulate(table, tablefmt='html'))