import os

import yt_dlp


def search_youtube_link(query):
    ydl_opts = {
        'quiet': True,
        'default_search': 'ytsearch1',  # Recherche une seule vidéo
        'noplaylist': True,
        'extract_flat': False  # Extraction complète
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(query, download=False)
            if 'entries' in result and result['entries']:
                return result['entries'][0]['webpage_url']
            elif 'webpage_url' in result:
                return result['webpage_url']
        except Exception as e:
            print(f"Erreur lors de la recherche YouTube pour {query}: {e}")
    return None

def download_mp3(video_url, save_dir="downloads"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print(f"Téléchargement terminé: {video_url}")
        except Exception as e:
            print(f"Erreur de téléchargement pour {video_url}: {e}")

def main():
    input_file = "titles.txt"
    if not os.path.exists(input_file):
        print(f"Fichier {input_file} introuvable.")
        return

    with open(input_file, "r") as file:
        queries = [line.strip() for line in file.readlines() if line.strip()]

    for query in queries:
        print(f"Recherche: {query}")
        video_url = search_youtube_link(query)
        if video_url:
            print(f"Vidéo trouvée: {video_url}")
            download_mp3(video_url)
        else:
            print(f"Aucune vidéo trouvée pour: {query}")

if __name__ == "__main__":
    main()
