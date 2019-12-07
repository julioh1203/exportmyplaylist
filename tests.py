import unittest
import os

from core import ExportPlaylist


class TestExportPlaylist(unittest.TestCase):

    def setUp(self):        
        self.playlist_id = '4uVvklTsfJ9SBXJdxqgib6'
        self.username = '12186735364'
        self.export = ExportPlaylist(self.username)
        self.playlist_to_export = [{'musica': 'Howlin’ For You', 'artista': 'The Black Keys'}, {'musica': 'Gold on the Ceiling', 'artista': 'The Black Keys'}]
        self.csv_filename = 'playlist_teste.csv'
        self.tracks = {
                    'href': 'https://api.spotify.com/v1/playlists/4uVvklTsfJ9SBXJdxqgib6/tracks?offset=0&limit=100', 
                    'items': [{'added_at': '2019-12-01T14:02:46Z', 'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/12186735364'}, 'href': 'https://api.spotify.com/v1/users/12186735364', 'id': '12186735364', 'type': 'user', 'uri': 'spotify:user:12186735364'}, 'is_local': False, 'primary_color': None, 'track': {'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4gwpcMTbLWtBUlOijbVpuu'}, 'href': 'https://api.spotify.com/v1/artists/4gwpcMTbLWtBUlOijbVpuu', 'id': '4gwpcMTbLWtBUlOijbVpuu', 'name': 'Capital Cities', 'type': 'artist', 'uri': 'spotify:artist:4gwpcMTbLWtBUlOijbVpuu'}],
                    'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 
                    'external_urls': {'spotify': 'https://open.spotify.com/album/3WrufJir7I61NkvkDwxero'}, 'href': 'https://api.spotify.com/v1/albums/3WrufJir7I61NkvkDwxero', 'id': '3WrufJir7I61NkvkDwxero', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/deed481c6f370b2c544752fb7315bf6dcc08d96a', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/7a615580ac63efd37471d5fec78e787739b9301d', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/bc5f0d41caa41c30b8ba7a5e5bf2ae786dbfd9e9', 'width': 64}], 'name': 'In A Tidal Wave Of Mystery (Deluxe Edition)', 'release_date': '2013', 'release_date_precision': 'year', 'total_tracks': 16, 'type': 'album', 'uri': 'spotify:album:3WrufJir7I61NkvkDwxero'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4gwpcMTbLWtBUlOijbVpuu'}, 'href': 'https://api.spotify.com/v1/artists/4gwpcMTbLWtBUlOijbVpuu', 'id': '4gwpcMTbLWtBUlOijbVpuu', 'name': 'Capital Cities', 'type': 'artist', 'uri': 'spotify:artist:4gwpcMTbLWtBUlOijbVpuu'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 192789, 'episode': False, 'explicit': False, 'external_ids': {'isrc': 'USCA21203108'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/6Z8R6UsFuGXGtiIxiD8ISb'}, 'href': 'https://api.spotify.com/v1/tracks/6Z8R6UsFuGXGtiIxiD8ISb', 'id': '6Z8R6UsFuGXGtiIxiD8ISb', 'is_local': False, 'name': 'Safe And Sound', 'popularity': 77, 'preview_url': 'https://p.scdn.co/mp3-preview/9100a200837a871f6f1c2cda42b2b5749cf9f11f?cid=b3d2f843b2704af98b30dd0ef69ae597', 'track': True, 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:6Z8R6UsFuGXGtiIxiD8ISb'}, 'video_thumbnail': {'url': None}}], 'limit': 100, 'next': None, 'offset': 0, 'previous': None, 'total': 1
                    }        
        self.playlist_test = []


    def test_export_spotify_playlist(self):
        teste = self.export.export_spotify_playlist(self.playlist_id)
        self.assertEqual(teste, 1)

    def test_create_csv(self):        
        self.export.create_csv(self.playlist_to_export, self.csv_filename)
        self.assertTrue(self.csv_filename in os.listdir('.'))
    
    def test_write_tracks_to_dict(self):
        teste = self.export.write_tracks_to_dict(self.tracks, self.playlist_test)
        self.assertEqual([{'musica': 'Safe And Sound', 'artista': 'Capital Cities'}], teste)

# spotify:playlist:0WAjP99fKlugTYbBkSWVOg
# spotify:playlist:1yMK5IHUjTouRk74tiWmSa(MAN AT WORK)
# spotify:playlist:4uVvklTsfJ9SBXJdxqgib6 (teste)
