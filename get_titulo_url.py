import yt_dlp

def obtener_titulos_y_urls(playlist_url, output_file):
    ydl_opts = {
        'quiet': True,  # Suprime la salida adicional
        'extract_flat': True,  # Extrae solo la metadata, no descarga los videos
        'skip_download': True,  # No descargar los videos
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
        
        # Asegurarse de que se trata de una playlist
        if 'entries' in result:
            video_entries = result['entries']
            
            with open(output_file, 'w', encoding='utf-8') as f:
                for entry in video_entries:
                    title = entry.get('title')
                    video_id = entry.get('id')  # Obtiene solo el ID del video
                    url = f"https://www.youtube.com/watch?v={video_id}"
                    
                    if title and video_id:
                        f.write(f"{title}\n{url}\n\n")
            
            print(f"El archivo '{output_file}' ha sido guardado con éxito.")
        else:
            print("No se encontró una playlist válida en la URL proporcionada.")

if __name__ == "__main__":
    playlist_url = input("Introduce la URL de la playlist o Mix de YouTube: ")
    output_file = "playlist_videos.txt"
    obtener_titulos_y_urls(playlist_url, output_file)
