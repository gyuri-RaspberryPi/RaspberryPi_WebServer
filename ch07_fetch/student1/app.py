from flask import Flask, render_template
import requests
from flask import Flask, render_template, request, jsonify
import config

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("gallery.html")

@app.route("/api/photos")                                    # 추가
def api_photos():
    page = request.args.get("page", 1)
    url = f"https://jsonplaceholder.typicode.com/photos?_page={page}&_limit=3"
    response = requests.get(url)
    data = response.json()
    photos = []
    for p in data:
            photos.append({"title": p["title"], "img": p["url"]})
    return jsonify(photos)
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
