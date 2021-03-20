from flask import Flask, redirect, url_for, render_template, request
from pytube import YouTube


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
		return render_template("index.html")

@app.route("/<lk>")
def login(lk):
    return f"<h1>{lk}</h1>"

if __name__ == '__main__':
	app.run(debug=True)
