import unittest

from generate import extract_title, file_to_string

class GenerateTest(unittest.TestCase):
    def test_extract_title(self):
        path = "/home/deusvitae/workspace/github.com/SumDeusVitae/static_site_generator/content/index.md"
        title = extract_title(path)
        self.assertEqual(
            title,
            "Tolkien Fan Club",
        )
