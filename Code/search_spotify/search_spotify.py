# coding: utf-8

import spotify_connect as sc

def artistSearchId(artist):
      """
      Searching for an artist, return a dictionary of spotify ids which match with the query
      """
      spot = sc.spotifyPublic()
      artist = spot.search(artist, limit=50, offset=0, type='artist', market=sc.marketall)
      artist_ids = {}
      for art in artist['artists']['items']:
            artist_ids[art['id']] = art['name']
      return artist_ids

def playlistSearchId(playlist, owner='Spotify'):
      """
      Searching for a playlist from a particular owner or owned by Spotify (default), return a dictionary of spotify ids which match with the query
      """
      spot = sc.spotifyPublic()
      playlist = spot.search(playlist, limit=50, offset=0, type='playlist', market=sc.marketall)
      playlists_id = {}
      for play in playlist['playlists']['items']:
            if play['owner']['display_name'] == owner:
                        playlists_id[play['id']] = play['name']
      return playlists_id
