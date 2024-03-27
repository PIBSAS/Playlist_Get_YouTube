import yt_dlp

def descargar_videos(playlist_url):
    ydl_opts = {
        'format': 'best[height<=720]',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist_url = input("Introduce la URL de la playlist de YouTube: ")
    descargar_videos(playlist_url)
