from model import dht_db
from flask import Flask, render_template, jsonify
import config
from sensor import dht

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/now")                              
def api_now():
    now = dht.get_now()
    if now is None:
        return jsonify({"message": "센서를 읽지 못함"}), 500
    return jsonify(now)

@app.route("/api/records", methods=["POST"])
def api_save():
    data = dht.get_now()

    if data is None:
        return jsonify({"message": "센서를 읽지 못함"}), 500

    record = dht_db.add(data["temperature"], data["humidity"])
    record["created_at"] = str(record["created_at"])

    return jsonify(record)


@app.route("/api/records")
def api_records():
    records = dht_db.get_all()

    for record in records:
        record["created_at"] = str(record["created_at"])

    return jsonify(records)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
