import pymysql
import config


def get_connection():
    """데이터베이스 연결을 만들어 돌려줌 (LED와 같은 코드)"""
    return pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        db=config.DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )


def add(temperature, humidity):
    """온습도를 한 건 저장하고, 방금 저장한 기록을 돌려줌"""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("insert into dht_record (temperature, humidity) values(%s, %s)", (temperature, humidity))
        conn.commit()
        cur.execute("select id,temperature, humidity, created_at from dht_record order by id desc limit 1")
        return cur.fetchone()
    finally:
        conn.close()

def get_all():
    """전체 기록을 최신순으로 돌려줌"""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("select id,temperature, humidity, created_at from dht_record order by created_at desc")
        conn.commit()
        return cur.fetchall()
    finally:
        conn.close()
