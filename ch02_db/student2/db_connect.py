import pymysql
import config

# ① 연결
conn = pymysql.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    db="shopping_db",
    charset="utf8mb4"
)

# ② 커서 생성
cur = conn.cursor()

# ③ SQL 실행
cur.execute("select * from CUSTOMER")

# ④ 결과 꺼내기
rows = cur.fetchall()
for row in rows:
    print(row)

# ⑤ 연결 종료
conn.close()
