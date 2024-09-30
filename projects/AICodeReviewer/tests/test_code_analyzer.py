"""Unit tests for the CodeAnalyzer module."""

import unittest
from aicodereviewer.code_analyzer import CodeAnalyzer


class TestCodeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = CodeAnalyzer()

    def test_analyze_empty_code(self):
        result = self.analyzer.analyze("")
        self.assertEqual(result, [])

    # Add more tests here


if __name__ == "__main__":
    unittest.main()
