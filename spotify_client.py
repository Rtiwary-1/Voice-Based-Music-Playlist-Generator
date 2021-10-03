## This code is utilised for getting the songs from the database by using Spotify API and providing mood and keyword as endpoint parameter. 
## The code returns n (default is 20) number of songs as output.

import random
import requests
import string
import urllib
import speechtotext


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def get_random_tracks(self):
        word1=speechtotext.analysis()
        #print(word1)
        #wildcard = f'%{random.choice(string.ascii_lowercase)}%'
        wildcard = f'%{word1[random.randint(0,len(word1)-1)]}%'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(0, 2000)
        url = f"https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()

        tracks = [
            track for track in response_json['tracks']['items']
        ]

        print(f'Found {len(tracks)} tracks to add to your library')

        return tracks

    def add_tracks_to_library(self, track_ids):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            url,
            json={
                "ids": track_ids
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        
        return response.ok
