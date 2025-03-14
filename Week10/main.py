import sqlite3
from contextlib import closing

try:
    with closing(sqlite3.connect('test.db')) as db_conn:
        db_conn.row_factory = sqlite3.Row
        with closing(db_conn.cursor()) as cursor:
            try:
                query_1 = "SELECT * FROM demo WHERE ID > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()
                for row in rows:
                    print(row["name"])
            except Exception as e:
                print(f"Error Executing Query 1") 
except sqlite3.Error as e:
    print(f"Database Connection Error")     