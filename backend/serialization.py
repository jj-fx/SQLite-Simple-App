import sqlite3
import csv
from backend.sqliteStuff import SQLite, select_all


def output_to_csv(filename):
    file = filename + '.csv'
    sql = SQLite()
    sql.create_connection()
    cur = sql.conn.cursor()
    cur.execute('SELECT * FROM personal_details;')
    with open(file, 'w') as out_csv_file:
        csv_out = csv.writer(out_csv_file)
        csv_out.writerow([d[0] for d in cur.description])
        for result in cur:
            csv_out.writerow(result)
    sql.conn.close()

def output_to_html(filename):
    file = filename + '.html'
    sql = SQLite()
    conn = sqlite3.connect(sql.db_file)
    sel = select_all(sql.conn)

if __name__ == '__main__':
    output_to_csv('../output')
