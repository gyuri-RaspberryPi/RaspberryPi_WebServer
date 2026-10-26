from flask import Flask, render_template, jsonify
import config
from sensor import dht
from model import dht_db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/now")                                 # 추가
def api_now():
    now = dht.get_now()
    if now is None:
        return jsonify({"message": "센서를 읽지 못함"}), 500
    return jsonify(now)                                # dict 를 그대로 JSON 으로

@app.route("/api/records", methods=["POST"])
def api_save():
    now = dht.get_now()
    if now is None:
        return jsonify({"message" : "센서를 읽지 못함"}), 500

    save = dht_db.add(now["temperature"], now["humidity"])
    save["created_at"] = str(save["created_at"])
    return jsonify(save)

@app.route("/api/records")
def api_records():
    all = dht_db.get_all()
    for row in all:
        if "created_at" in row and row["created_at"]:
            row["created_at"] = str(row["created_at"])
    return jsonify(all)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
