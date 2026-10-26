import requests
from flask import Flask, render_template, request, jsonify
import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("gallery.html")

@app.route("/api/photos")
def api_photos():
    page = request.args.get("page", 1)
    res = requests.get(f"https://jsonplaceholder.typicode.com/photos?_page={page}&_limit=3")
    photos = []
    for p in res.json():
        photos.append({"title": p["title"], "img": p["url"]})
    return jsonify(photos)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config.PORT)


