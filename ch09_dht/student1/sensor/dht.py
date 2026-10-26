import adafruit_dht
import board
import config

pin = getattr(board, "D" + str(config.DHT_PIN))
sensor = adafruit_dht.DHT11(pin)


def get_now():
    """지금 온도와 습도를 dict 로 돌려줌. 읽기에 실패하면 None"""
    try:
        temperature = sensor.temperature
        humidity = sensor.humidity
    except RuntimeError:
        return None
    if temperature is None or humidity is None:     # 방금 읽기에 실패했으면 값이 비어 있을 수 있음
        return None
    return {"temperature": temperature, "humidity": humidity}
