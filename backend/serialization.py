import sqlite3
import csv
from backend.sqliteStuff import SQLite


def output_to_csv(filename):
    sql = SQLite()
    conn = sqlite3.connect(sql.db_file)
    cur = conn.cursor()
    cur.execute('SELECT * FROM personal_details')
    with open(filename, 'w') as out_csv_file:
        csv_out = csv.writer(out_csv_file)
        csv_out.writerow([d[0] for d in cur.description])
        for result in cur:
            csv_out.writerow(result)
    conn.close()


if __name__ == '__main__':
    output_to_csv('output.csv')
