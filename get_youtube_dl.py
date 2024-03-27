import youtube_dl

def descargar_videos(playlist_url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist_url = input("Introduce la URL de la playlist de YouTube: ")
    descargar_videos(playlist_url)
