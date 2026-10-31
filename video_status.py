import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

CHANNEL_HANDLE = "LarissaLemos"

def get_playlist_id():

    try:

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}"

        headers = {"X-Goog-Api-Key": API_KEY}

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()

        # print(json.dumps(data, indent=4))

        channel_items = data['items'][0]

        channels_playlist_id = channel_items['contentDetails']['relatedPlaylists']['uploads']

        print(channels_playlist_id)

        return channels_playlist_id

    except requests.exceptions.RequestException as e: 
        raise e

if __name__ == "__main__":
    get_playlist_id()
