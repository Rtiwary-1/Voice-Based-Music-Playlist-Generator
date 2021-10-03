## This code imports the results of all of the dependent programs and runs them. This the code which adds the returned list of songs to the playlist.

import os

from spotify_client import SpotifyClient

def run():
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    random_tracks = spotify_client.get_random_tracks()
    track_ids = [track['id'] for track in random_tracks]
    #track_names=[track['name'] for track in random_tracks]

    was_added_to_library = spotify_client.add_tracks_to_library(track_ids)
    if was_added_to_library:
        for track in random_tracks:
            print(f"Added {track['name']} to your library")
    
    #print(track_names)

if __name__ == '__main__':
    run()
