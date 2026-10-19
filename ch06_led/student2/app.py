from flask import Flask, render_template, request
from model.led_db import LedDB
import RPi.GPIO as GPIO
import config
import traceback

app = Flask(__name__)
led_db = LedDB()
LED = {
        "red":config.LED_RED,
        "green":config.LED_GREEN,
        "blue":config.LED_BLUE,}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
for pin in LED.values():
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def home():
    # 1. 기본 상태 초기화 (모두 OFF)
    is_on = {'red': 0, 'green': 0, 'blue': 0}

    # 2. GPIO 읽기 시도 (라즈베리파이 실물 환경용)
    for color, pin in LED.items():
        try:
            is_on[color] = GPIO.input(pin)
        except Exception:
            pass

    # 3. DB 기록 읽어오기
    records = led_db.get(10)

    # 4. 실물 GPIO가 없더라도 DB 최신 기록을 바탕으로 is_on 상태 반영
    if records:
        # DB에서 역순(옛날 기록 -> 최신 기록)으로 조회하여 최종 상태를 덮어씁니다.
        for r in reversed(records):
            # r.pin (또는 r['pin']) 이 숫자 핀 번호(12,18,22)인 경우
            if r['pin'] == 12 or r['pin'] == 'red':
                is_on['red'] = r['is_on']
            elif r['pin'] == 18 or r['pin'] == 'green':
                is_on['green'] = r['is_on']
            elif r['pin'] == 22 or r['pin'] == 'blue':
                is_on['blue'] = r['is_on']

    return render_template("index.html", is_on=is_on, records=records)

@app.route("/on", methods=["POST"])
def led_on():
    color = request.form.get("color")
    if not color or color not in LED:
        return "invalid color", 400

    pin = LED[color]

    # GPIO 제어 (라즈베리파이 미연결 시 스킵)
    try:
        GPIO.output(pin, GPIO.HIGH)
    except Exception as e:
        print(f"GPIO Skip: {e}")

    led_db.add(pin,1)

    return "ok"

@app.route("/off", methods=["POST"])
def led_off():
    color = request.form.get("color")
    if not color or color not in LED:
        return "invalid color", 400

    pin = LED[color]

    try:
        GPIO.output(pin, GPIO.LOW)
    except Exception as e:
        print(f"GPIO Skip : {e}")

    led_db.add(pin,0)

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
