# to run this code
#  $env:FLASK_APP="application.py"
# flask run

from flask import Flask, render_template, request
from pytube import YouTube, Playlist
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def Download(link):
    status = ""
    youtubeObject = YouTube(link)
    # youtubeObject = youtubeObject.streams.get_highest_resolution
    try:
        youtubeObject.streams.get_by_resolution("720p").download()
    except:
        status="An error has occfurred"
    status = "Download is completed successfully"
    return status

def DownloadPlaylist(playListLink,resolution):
    playlist = Playlist(playListLink)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video in playlist.videos:
        video.streams.get_by_itag(22).download()
        print("video done",video.description)
        # video.streams.get_highest_resolution.download()
        # video.streams.get_highest_resolution.download()


@app.route("/download", methods=["POST"])
def download():
    link = request.form.get('url')
    return Download(link)

@app.route("/downloadPlaylist", methods=["POST"])
def downloadPlaylist():
    link = request.form.get('listUrl')
    DownloadPlaylist(link,"480p")
    return "end"