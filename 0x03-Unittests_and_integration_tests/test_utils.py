#!/usr/bin/env python3
"""unit test for utils"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """unit test for utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with different inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access_nested_map with exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """unit test for utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, payload, mock_get):
        """Test get_json"""
        mock_get.return_value.json.return_value = payload
        self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """unit test for utils.memoize"""

    def test_memoize(self):
        """test memoize"""
        class TestClass:
            """test class"""
            def a_method(self):
                """a method"""
                return 42

            @memoize
            def a_property(self):
                """a property"""
                return self.a_method()

        with patch.object(
                        TestClass,
                        'a_method',
                        return_value=42) as mock_method:
            test_object = TestClass()
            test_object.a_property
            test_object.a_property
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
