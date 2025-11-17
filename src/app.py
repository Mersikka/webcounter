from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/set_to", methods=["POST"])
def set_to():
    num = request.form.get("num")
    if not num.isdigit():
        return redirect("/")
    cnt.set_to(int(num))
    return redirect("/")
