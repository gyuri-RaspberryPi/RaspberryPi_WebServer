from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
from time import sleep
from model.servo_db import ServoDB
import config

app = Flask(__name__)
SERVO = config.SERVO_PIN

app = Flask(__name__)
servo_db = ServoDB()
# ───── 서보모터 준비 ─────
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO, GPIO.OUT)
servo = GPIO.PWM(SERVO, 50)
servo.start(0)

def set_angle(angle):
    duty = 2.5 + 10 * angle / 180
    servo.ChangeDutyCycle(duty)
    sleep(0.5)
    servo.ChangeDutyCycle(0)
    set_angle(angle)
    servo_db.add(SERVO, angle)

@app.route("/")
def home():
    return render_template("index.html")

# ───── 서보모터 각도 제어 API ─────
@app.route("/api/angle", methods=["POST"])
def api_angle():
    data = request.get_json()
    angle = int(float(data["angle"]))

    # 1. 각도가 0~180 범위를 벗어나면 오류 반환
    if angle < 0 or angle > 180:
        return jsonify({"message": "0 ~ 180 사이만 가능"}), 400

    # 2. 유효한 각도이면 서보모터를 움직이고 결과 반환
    set_angle(angle)
    return jsonify({"message": f"{angle}도로 움직임"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
