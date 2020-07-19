# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model.player import Player


class TestPlayer(unittest.TestCase):
    """Player unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlayer(self):
        """Test Player"""
        # we can make a player without an enemy_player property
        jane = Player(name="Jane")
        # we can make a player with an enemy_player
        sally = Player(name="Sally", enemy_player=jane)
        # we can make a player with an inline enemy_player
        jim = Player(
            name="Jim",
            enemy_player=Player(name="Sam")
        )


if __name__ == '__main__':
    unittest.main()
