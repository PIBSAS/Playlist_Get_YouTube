## Require pythoon environment ##
## pip install yt-dlp ##
## sudo apt-get install ffmpeg ##

import os, subprocess, sys

def is_dependencies_installed():
    try:
        subprocess.check_output([sys.executable, "-m", "pip", "show", "yt_dlp"])
        return True
    except subprocess.CalledProcessError:
        return False

if not is_dependencies_installed():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt_dlp"])

import yt_dlp

def descargar_audio(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist_url = input("Introduce la URL de la playlist o Mix de YouTube: ")
    descargar_audio(playlist_url)
