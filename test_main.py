#!/usr/bin/env python3
"""
Tests for the main module.
"""

import unittest
import sys
from io import StringIO
from main import hello_world, main


class TestMain(unittest.TestCase):
    """Test cases for main module functions."""

    def test_hello_world(self):
        """Test that hello_world prints the correct message."""
        captured_output = StringIO()
        sys.stdout = captured_output
        hello_world()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

    def test_main_function(self):
        """Test that main function runs without error."""
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Hello, World!", output)
        self.assertIn("This is a sample project implementation.", output)


if __name__ == "__main__":
    unittest.main()