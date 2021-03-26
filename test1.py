from flask import Flask, redirect, url_for, render_template, request, flash, session
from pytube import YouTube

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == "POST":
		link = request.form["link"]
		yt = YouTube(link)
		video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
		video.first().download()
		return render_template("index.html")
	else :
		return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
