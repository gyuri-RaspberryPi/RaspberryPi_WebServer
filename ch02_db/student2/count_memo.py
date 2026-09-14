import pymysql
import config

conn = pymysql.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    db=config.DB_NAME,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)
cur = conn.cursor()

cur.execute("select count(*) from memo")
rows = cur.fetchall()
print(rows[count])


conn.close()
