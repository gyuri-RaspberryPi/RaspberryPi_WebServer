import pymysql
import config


def get_connection():
    return pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        db=config.DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )


def get_counts():
    """저장된 기록을 최신순으로 가져옴"""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("select * from counter order by id desc")
        return cur.fetchall()
    finally:
        conn.close()


def add_count(num):
    """클릭 수를 한 건 저장함"""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("insert into counter (num) values (%s)", (num,))
        conn.commit()
    finally:
        conn.close()
