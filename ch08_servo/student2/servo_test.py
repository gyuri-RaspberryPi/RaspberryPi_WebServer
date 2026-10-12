import RPi.GPIO as GPIO
from time import sleep
import config

SERVO = config.SERVO_PIN

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO, GPIO.OUT)
servo = GPIO.PWM(SERVO, 50)     # 이 핀을 1초에 50번 신호를 보내는 PWM 으로 씀
servo.start(0)                  # 듀티 0 이라 아직 움직이지 않음


# 각도를 듀티로 바꿔서 서보모터를 움직임
def set_angle(angle):
    duty = 2.5 + 10 * angle / 180
    print(f"{angle}도 → 듀티 {duty}")
    servo.ChangeDutyCycle(duty)
    sleep(0.5)                  # 움직일 시간을 줌
    servo.ChangeDutyCycle(0)    # 신호를 끔 → 멈춘 뒤 떨림(드드드)이 없어짐


set_angle(0)
sleep(1)
set_angle(90)
sleep(1)
set_angle(180)
sleep(1)

servo.stop()
GPIO.cleanup()
