#!/usr/bin/env python3
"""unit test for client"""


import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import (
    GithubOrgClient,
    access_nested_map,
    get_json,
    memoize,
)


class TestGithubOrgClient(unittest.TestCase):
    """unit test for GithubOrgClient"""
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, payload, mock_get):
        """test org"""
        mock_get.return_value = payload
        self.assertEqual(GithubOrgClient(org_name).org, payload)
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == "__main__":
    unittest.main()
