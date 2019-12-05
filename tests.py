import unittest

from core import ExportPlaylist


class TestExportPlaylist(unittest.TestCase):

    def setUp(self):
        #self.playlist_id = '4uVvklTsfJ9SBXJdxqgib6'
        self.playlist_id = '1yMK5IHUjTouRk74tiWmSa'
        self.username = '12186735364'
        self.export = ExportPlaylist(self.username)

    def test_export_spotify_playlist(self):
        teste = self.export.export_spotify_playlist(self.playlist_id)
        self.assertEqual(teste, 174)

#spotify:playlist:0WAjP99fKlugTYbBkSWVOg
#spotify:playlist:1yMK5IHUjTouRk74tiWmSa(MAN AT WORK)
