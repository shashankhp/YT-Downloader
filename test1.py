from flask import Flask, redirect, url_for, render_template, request, flash, session
from pytube import YouTube


if __name__ == '__main__':
	socketio.run(app)

app = Flask(__name__)
app.secret_key = "SSKhp"

@app.route("/", methods=["POST", "GET"])
def home():
	try:
		if request.method == "POST":
			link = request.form["link"]
			session["link"] = link
			yt = YouTube(link)
			video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
			video.first().download()
			flash("Video Downloaded Successfully")
			return render_template("index.html")
		else :
			return render_template("index.html")
	except(Exception):
		flash("Video inaccessible. Check the Link and try again!")
		return render_template("index.html")

	
