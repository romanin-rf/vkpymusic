"""
This module contains the Converter class.
"""

import json
import logging
from typing import List

from requests import Response

from ..song import Song
from ..playlist import Playlist
from .logger import get_logger


logger: logging.Logger = get_logger(__name__)


class Converter:
    """A class that converts a response from VK to a list of songs or playlists.

    Methods:
        response_to_songs(response: Response) -> List[Song]: Converts a response to a list of songs.
        response_to_playlists(response: Response) -> List[Playlist]: Converts a response to a list of playlists.
    """

    @staticmethod
    def response_to_songs(response: Response):
        """Converts a response to a list of songs.

        Args:
            response (Response): The response object from VK.

        Returns:
            List[Song]: A list of songs converted from the response.
        """
        response = json.loads(response.content.decode("utf-8"))
        try:
            items = response["response"]["items"]
        except Exception as e:
            logger.error(e)
        songs: List[Song] = []
        for item in items:
            song = Song.from_json(item)
            songs.append(song)
        return songs

    @staticmethod
    def response_to_playlists(response: Response):
        """Converts a response to a list of playlists.

        Args:
            response (Response): The response object from VK.

        Returns:
            List[Playlist]: A list of playlists converted from the response.
        """
        response = json.loads(response.content.decode("utf-8"))
        try:
            items = response["response"]["items"]
        except Exception as e:
            logger.error(e)
        playlists: List[Playlist] = []
        for item in items:
            playlist = Playlist.from_json(item)
            playlists.append(playlist)
        return playlists
