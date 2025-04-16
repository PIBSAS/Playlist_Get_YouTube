## Require pythoon environment ##
## pip install yt-dlp ##
## sudo apt-get install ffmpeg ##
## Agregada normalizaciion de audio tras descarga por lo cual tarda mas
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

def normalizar_volumen_mp3(file):
    temp_file = f"temp_normalizado_{os.path.basename(file)}"
    print(f"Normalizando: {file}")
    if not os.path.exists(file):
        print(f"❌ El archivo {file} no existe.")
        return
    
    result = subprocess.run([
        "ffmpeg", "-y", "-i", file,
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-ar", "44100", "-ac", "2",
        temp_file
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ Error al normalizar {file}:\n{result.stderr}")
    else:
        os.replace(temp_file, file)
        print(f"✅ Normalizado: {file}")

def descargar_audio(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
    
    print("\n🔎 Buscando archivos .mp3 para normalizar...\n")
    for archivo in os.listdir():
        if archivo.endswith(".mp3"):
            normalizar_volumen_mp3(archivo)
            print(f"🎧 Postprocesando: {archivo}")

if __name__ == "__main__":
    playlist_url = input("🎵 Introduce la URL de la playlist o Mix de YouTube: ")
    descargar_audio(playlist_url)
