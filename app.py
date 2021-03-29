from flask import Flask, redirect, url_for, render_template, request, flash, session
from pytube import YouTube

app = Flask(__name__)
app.secret_key = "SSKhp"

@app.route("/", methods=["POST", "GET"])
def home():
	try:
		if request.method == "POST":
			if request.method == "POST":
			link = request.form["link"]
			session["link"] = link
			yt = YouTube(link)
			video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
			video = video.first().url
			chunk_size = 256
			r = requests.get(video, stream=True)
			with open("Youtube Video", "wb") as f:
				for chunk in r.iter_content(chunk_size = chunk_size):
					f.write(chunk)
			flash("Video Downloaded Successfully")
			return render_template("index.html")
		else :
			return render_template("index.html")
	except(Exception):
		flash("Video inaccessible. Check the Link and try again!")
		return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
