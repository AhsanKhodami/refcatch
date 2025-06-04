"""
Tests for the RefCatch package.
"""

import os
import unittest
from unittest.mock import patch, MagicMock
from refcatch import refcatch

class TestRefCatch(unittest.TestCase):
    """Test cases for RefCatch."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.test_input = os.path.join(self.test_dir, "test_refs.md")
        self.test_output = os.path.join(self.test_dir, "test_output.md")
        self.test_doi = os.path.join(self.test_dir, "test_dois.txt")
        
        # Create a test reference file
        with open(self.test_input, "w", encoding="utf-8") as f:
            f.write("1.\tTest Author. Test Title. Test Journal. 2020;10(1):1-10.\n")
    
    def tearDown(self):
        """Tear down test fixtures."""
        # Remove test files
        for file in [self.test_input, self.test_output, self.test_doi]:
            if os.path.exists(file):
                os.remove(file)
    
    @patch("refcatch.core.get_doi_for_reference")
    def test_refcatch_basic(self, mock_get_doi):
        """Test basic functionality of refcatch."""
        # Mock the DOI lookup function to return a test DOI
        mock_get_doi.return_value = "10.1234/test.doi"
        
        # Run refcatch
        success, message, doi_count = refcatch(
            self.test_input, 
            self.test_output, 
            self.test_doi, 
            log=False
        )
        
        # Check results
        self.assertTrue(success)
        self.assertEqual(doi_count, 1)
        self.assertTrue(os.path.exists(self.test_output))
        self.assertTrue(os.path.exists(self.test_doi))
        
        # Check output file content
        with open(self.test_output, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("1.\tTest Author", content)
            self.assertIn("DOI: 10.1234/test.doi", content)
        
        # Check DOI file content
        with open(self.test_doi, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("10.1234/test.doi", content)

if __name__ == "__main__":
    unittest.main()
