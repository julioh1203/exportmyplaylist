import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import oauth2


class ExportPlaylist():

    def __init__(self):
        CLIENT_ID = 'b3d2f843b2704af98b30dd0ef69ae597'
        CLIENT_SECRET = 'fb34a5614e014467bbfdad44fce36c2d'
        redirect_uri = 'https://www.google.com.br'
        scope = 'user-library-read playlist-read-private'
        self.username = '12186735364'

        client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        self.token = util.prompt_for_user_token(self.username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                redirect_uri=redirect_uri)

    def export_spotify_playlist(self, playlist_id):
            playlist_to_export = list()
            spotify = spotipy.Spotify(auth=self.token)
            playlist = spotify.user_playlist(self.username, playlist_id=playlist_id)
            tracks = spotify.user_playlist_tracks(self.username, playlist_id=playlist_id)
            playlist_name = playlist['name']
            for item in tracks['items']:
                track = item['track']
                playlist_to_export.append({'musica': track['name'],'artista': track['artists'][0]['name']})
                for i in playlist_to_export:
                    print(i['musica'])

            return (tracks['total'])
