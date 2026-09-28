from flask import Flask, render_template
from model.led_db import LedDB
import RPi.GPIO as GPIO
import config

app = Flask(__name__)
led_db = LedDB()
LED = config.LED_PIN

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def home():
    led_state = GPIO.input(LED)
    return render_template("index.html", state = led_state)

@app.route("/on", methods=["POST"])
def led_on():
    # LED를 켜고 "ok" 를 돌려줌. 실패하면 "fail"
    try:
        GPIO.output(LED, GPIO.HIGH)
        led_db.add(LED, 1)
        return "ok"
    except:
        return "fail",500


@app.route("/off", methods=["POST"])
def led_off():
    # LED를 끄고 "ok" 를 돌려줌. 실패하면 "fail"
    try:
        GPIO.output(LED, GPIO.LOW)
        led_db.add(LED, 0)
        return "ok"
    except:
        return "fail",500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
