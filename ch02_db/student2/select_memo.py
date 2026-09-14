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

cur.execute("select * from memo order by id desc")
rows = cur.fetchall()

for row in rows:
    print(row["id"], row["content"], row["created_at"])

conn.close()
