import time
import adafruit_dht
import board
import config

pin = getattr(board, "D" + str(config.DHT_PIN))       # 4 이면 board.D4 를 고름
sensor = adafruit_dht.DHT11(pin)
# 자신의 파이썬 버전이 3.13이면 아래 코드로 대체
# sensor = adafruit_dht.DHT11(board.D14, use_pulseio=False)

while True:
    try:
        print(f"온도 {sensor.temperature}°C, 습도 {sensor.humidity}%")
    except RuntimeError as e:
        print("읽기 실패, 다시 시도 :", e)
    time.sleep(2)
