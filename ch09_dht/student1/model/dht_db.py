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
    db_connection = get_connection()
    cursor = db_connection.cursor()
    """온습도를 한 건 저장하고, 방금 저장한 기록을 돌려줌"""
    try:
        insert_sql = "INSERT INTO dht_record (temperature, humidity) VALUES (%s, %s)"
        cursor.execute(insert_sql, (temperature, humidity))
        db_connection.commit()

        select_sql = "SELECT * FROM dht_record WHERE id = %s"
        cursor.execute(select_sql, (cursor.lastrowid,))
        return cursor.fetchone()
    finally:
        db_connection.close()

def get_all():
    db_connection = get_connection()
    cursor = db_connection.cursor()
    """전체 기록을 최신순으로 돌려줌"""
    try:
        select_sql = "SELECT * FROM dht_record ORDER BY created_at DESC, id DESC"
        cursor.execute(select_sql)
        return cursor.fetchall()
    finally:
        db_connection.close()
