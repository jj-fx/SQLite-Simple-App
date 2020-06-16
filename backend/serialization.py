import csv
from backend.sqliteStuff import SQLite, select_all
from tabulate import tabulate


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


def output_to_txt(filename):
    file = filename + '.txt'
    sql = SQLite()
    sql.create_connection()
    sel = select_all(sql.conn)
    with open(file, 'w') as f:
        for row in sel:
            for item in row:
                f.write("{},\t".format(item))
            f.write(";\n")
    sql.conn.close()


def output_to_html(filename):
    file = filename + '.html'
    sql = SQLite()
    sql.create_connection()
    sel = select_all(sql.conn)
    sel = tabulate(sel, tablefmt='html')
    with open(file, 'w') as f:
        f.write("{},\t".format(sel))
        # for row in sel:
        #     for item in row:
        #         f.write("{},\t".format(item))
        #     f.write(";\n")
    sql.conn.close()


if __name__ == '__main__':
    output_to_csv('../output')
