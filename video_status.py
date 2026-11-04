import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "LarissaLemos"
max_results = 50

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

def get_video_ids(playlist_id):

    video_ids = []

    pageToken = None

    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={max_results}&playlistId={playlist_id}"

    headers = {"X-Goog-Api-Key": API_KEY}

    try:

        while True:
            url = base_url
            if pageToken:
                url += f"&pageToken={pageToken}"

            response = requests.get(url, headers=headers)

            response.raise_for_status()

            data = response.json()

            for item in data.get('items', []):
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)

            pageToken = data.get('nextPageToken')

            if not pageToken:
                break
        
        return video_ids
    except requests.exceptions.RequestException as e:
        raise e
        
if __name__ == "__main__":
    playlist_id = get_playlist_id()
    video_ids = get_video_ids(playlist_id)
    # print(video_ids)
