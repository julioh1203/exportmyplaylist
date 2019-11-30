import unittest

from core import ExportPlaylist


class TestExportPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist_id = '4uVvklTsfJ9SBXJdxqgib6'
        self.export = ExportPlaylist()

    def test_export_spotify_playlist(self):        
        teste = self.export.export_spotify_playlist(self.playlist_id)        
        self.assertEqual(teste, 1)
