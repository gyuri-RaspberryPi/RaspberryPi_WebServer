from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
from time import sleep
import config

app = Flask(__name__)
SERVO = config.SERVO_PIN

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

@app.route("/")
def home():
        return render_template("index.html")

@app.route("/api/angle", methods=["POST"])
def api_angle():
    data = request.get_json()
    angle = int(float(data["angle"]))
    if angle<0 or angle >180:
        return jsonify({"message": "0 ~ 180 사이만 가능"}), 400
    set_angle(angle)
    return jsonify({f"message": "{angle}도로 움직임"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=config.PORT)
