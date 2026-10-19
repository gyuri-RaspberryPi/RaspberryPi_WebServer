from flask import Flask, render_template, request, redirect
import config
from model.todo_db import TodoDB


app = Flask(__name__)
todo_db = TodoDB()


@app.route("/")
def home():
    """할 일 목록을 화면에 그림 (예시로 완성해둠)"""
    tasks = todo_db.get_all()
    return render_template("task.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    content = request.form.get("content", "").strip()
    if content:
        todo_db.add(content)
    return redirect("/")


@app.route("/complete/<int:todo_id>", methods=["POST"])
def complete(todo_id):
    todo_db.toggle(todo_id)
    return redirect("/")


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    todo_db.delete(todo_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=True)
