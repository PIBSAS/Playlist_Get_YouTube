import requests
from bs4 import BeautifulSoup
import os

# Lista de URLs de los sitios web que quieres scrapear
site_urls = [
    'https://unmtube.unm.edu.ar/vEmbed/2804',
    'https://unmtube.unm.edu.ar/vEmbed/3174',
    'https://unmtube.unm.edu.ar/vEmbed/2913',
    'https://unmtube.unm.edu.ar/vEmbed/3024',
    'https://unmtube.unm.edu.ar/vEmbed/3120',
    'https://unmtube.unm.edu.ar/vEmbed/3147',
    'https://unmtube.unm.edu.ar/vEmbed/3176',
    'https://unmtube.unm.edu.ar/vEmbed/3215',
    'https://unmtube.unm.edu.ar/vEmbed/3251'
]

def descargar_videos(site_url):
    # Realiza una solicitud HTTP al sitio web
    response = requests.get(site_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Crea un directorio para guardar los videos
    os.makedirs('videos', exist_ok=True)

    # Encuentra todas las etiquetas <source> y extrae las URLs
    for source in soup.find_all('source'):
        video_url = source.get('src')
        if video_url and video_url.endswith('.mp4'):
            # Extrae el nombre del archivo de la URL
            video_name = video_url.split('/')[-1]
            video_path = os.path.join('videos', video_name)
            
            # Descarga el video
            print(f'Descargando {video_name} desde {site_url}...')
            video_response = requests.get(video_url, stream=True)
            with open(video_path, 'wb') as video_file:
                for chunk in video_response.iter_content(chunk_size=8192):
                    video_file.write(chunk)

            print(f'{video_name} descargado.')

    print('Descarga completada para:', site_url)

# Itera sobre cada URL y llama a la función de descarga
for url in site_urls:
    descargar_videos(url)
