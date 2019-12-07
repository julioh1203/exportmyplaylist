import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import oauth2
from decouple import config
import json
import csv


class ExportPlaylist:

    def __init__(self, username):
        CLIENT_ID = config('CLIENT_ID')
        CLIENT_SECRET = config('CLIENT_SECRET')
        redirect_uri = 'https://www.google.com.br'
        scope = 'user-library-read playlist-read-private'
        self.username = username

        client_credentials_manager = SpotifyClientCredentials(
            client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        spotify = spotipy.Spotify(
            client_credentials_manager=client_credentials_manager)

        self.token = util.prompt_for_user_token(self.username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                redirect_uri=redirect_uri)

    def write_tracks_to_dict(self, tracks, playlist_to_export):        
        for item in tracks['items']:
            track = item['track']
            playlist_to_export.append(
                {'musica': track['name'], 'artista': track['artists'][0]['name']})
        return playlist_to_export

    def create_csv(self, playlist_to_export, csv_filename):
        headers = playlist_to_export[0].keys()
        with open(csv_filename, 'w+') as csv_file:
            dict_writer = csv.DictWriter(
                csv_file, restval='-', fieldnames=headers, delimiter=',')
            dict_writer.writeheader()
            dict_writer.writerows(playlist_to_export)
        csv_file.close()
        return csv_filename

    def export_spotify_playlist(self, playlist_id):
        playlist_to_export = list()
        spotify = spotipy.Spotify(auth=self.token)
        playlist = spotify.user_playlist(
            self.username, playlist_id=playlist_id, fields='name,tracks,artist,next')
        csv_filename = '{}.csv'.format(playlist['name'])

        # write the first 100 tracks
        tracks = playlist['tracks']
        self.write_tracks_to_dict(tracks, playlist_to_export)

        # While have tracks will write the dict
        while tracks['next']:
            tracks = spotify.next(tracks)
            self.write_tracks_to_dict(tracks, playlist_to_export)
        # Create CSV file
        self.create_csv(playlist_to_export, csv_filename)

        return (tracks['total'])
