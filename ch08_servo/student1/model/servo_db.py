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


class ServoDB:
    """서보모터 기록을 다루는 계층"""

    def add(self, pin, angle):
        """움직인 각도를 한 건 추가함"""
        # ✏️ 직접 작성하기 : 각도를 한 건 저장 (led_db.py 의 add 참고)
