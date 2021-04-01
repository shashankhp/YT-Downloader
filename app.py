from flask import Flask, redirect, url_for, render_template, request, flash, session, send_file
from pytube import YouTube

app = Flask(__name__)
app.secret_key = "SSKhp"

@app.route("/", methods=["POST", "GET"])
def home():
	try:
		if request.method == "POST":
			link = request.form["link"]
			session["link"] = link
			yt = YouTube(link)
			video = yt.streams.filter(progressive=True).order_by('resolution').desc()
			video.first().download(filename='Video')
			return redirect(url_for("download_file", nam = yt.title))
		else :
			return render_template("index.html")
	except(Exception):
		flash("Video inaccessible. Check the Link and try again!")
		return render_template("index.html")


@app.route('/<nam>')
def download_file(nam):
	path = nam + ".mp4"
	return send_file(path, as_attachment=True)

if __name__ == '__main__':
	app.run(debug=True)
