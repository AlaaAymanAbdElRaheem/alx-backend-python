#!/usr/bin/env python3
"""unit test for client"""


import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import (
    GithubOrgClient,
    access_nested_map,
    get_json,
    memoize,
)
import fixtures


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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """test public_repos_url"""
        mock_org.return_value = {"repos_url": "http://example.com"}
        self.assertEqual(GithubOrgClient("google")._public_repos_url,
                         "http://example.com")

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """test pupblic_repos"""
        with patch('client.GithubOrgClient._public_repos_url') as mock_url:
            mock_url.return_value = 'http://example.com'
            mock_get.return_value = [{"name": "a"}, {"name": "b"}]
            self.assertEqual(
                GithubOrgClient("google").public_repos(), ["a", "b"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """test has_license"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected)


@parameterized_class([
    {
        "org_payload": fixtures.TEST_PAYLOAD[0][0],
        "repos_payload": fixtures.TEST_PAYLOAD[0][1],
        "expected_repos": fixtures.TEST_PAYLOAD[0][2],
        "apache2_repos": fixtures.TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration test for GithubOrgClient.public_repos"""
    @classmethod
    def setUpClass(cls):
        """set up class"""
        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()
        cls.get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """tear down class"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
