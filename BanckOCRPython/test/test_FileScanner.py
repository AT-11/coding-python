from unittest import TestCase
from banckocr.FileScanner import FileScanner


class TestFileScanner(TestCase):
    def test_scan_file_file_numbers123456789_123456789(self):
        file = FileScanner()
        file_path = "BanckOCRPython/banckocr/files/123456789.txt"
        actual = file.scan_file(file_path)
        expected = "123456789"
        assert expected is actual
