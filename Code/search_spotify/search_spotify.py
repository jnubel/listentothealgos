# coding: utf-8

import spotipy
import spotipy.oauth2 as oauth2
import spotipy.util as util
import csv
import os

redirect_uri = "http://localhost/"
scope = "user-library-read playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative"
token_type = ""

marketall = [ "AD", "AR", "AT", "AU", "BE", "BG", "BO", "BR", "CA", "CH", "CL", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "EC", "EE", "ES", "FI", "FR", "GB", "GR", "GT", "HK", "HN", "HU", "ID", "IE", "IS", "IT", "JP", "LI", "LT", "LU", "LV", "MC", "MT", "MX", "MY", "NI", "NL", "NO", "NZ", "PA", "PE", "PH", "PL", "PT", "PY", "SE", "SG", "SK", "SV", "TH", "TR", "TW", "US", "UY", "VN" ]


def spotifyPublic():
     """
     Public connection to Spotify. 
     Credentials must be set in your environment variables.
     """
     credentials = oauth2.SpotifyClientCredentials()
     token = credentials.get_access_token()
     spot = spotipy.Spotify(auth=token)
     return spot

def artistSearchId(artist):
      """
      Searching for an artist, return a dictionary of spotify ids which match with the query
      """
      spot = spotifyPublic()
      artist = spot.search(artist, limit=50, offset=0, type='artist', market=marketall)
      artist_ids = {}
      for art in artist['artists']['items']:
            artist_ids[art['id']] = art['name']
      return artist_ids

def playlistSearchId(playlist, owner='Spotify'):
      """
      Searching for a playlist from a particular owner or owned by Spotify (default), return a dictionary of spotify ids which match with the query
      """
      spot = spotifyPublic()
      playlist = spot.search(playlist, limit=50, offset=0, type='playlist', market=marketall)
      playlists_id = {}
      for play in playlist['playlists']['items']:
            if play['owner']['display_name'] == owner:
                        playlists_id[play['id']] = play['name']
      return playlists_id
