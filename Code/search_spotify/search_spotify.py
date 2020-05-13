# coding: utf-8

import spotify_connect as sc

def searchSpotifyID(query,type='artist',owner='Spotify'):
      """"
      Search for a Spotify object that match a query, artist by default.
      Could be playlist, a track, an album...
      """

      spot = sc.spotifyPublic()

      if type == 'artist':
            """
            Searching for an artist. 
            Return a dictionary of spotify ids which match with the query
            """

            artist = spot.search(query, limit=50, offset=0, type='artist', market=sc.marketall)
            artist_ids = {}
            for art in artist['artists']['items']:
                  artist_ids[art['id']] = art['name']
            return artist_ids
    
      if type == 'playlist':
            """
            Searching for a playlist from a particular owner or owned by Spotify (default).
            Return a dictionary of spotify ids which match with the query
            """

            playlist = spot.search(query, limit=50, offset=0, type='playlist', market=sc.marketall)
            playlists_id = {}
            for play in playlist['playlists']['items']:
                  if play['owner']['display_name'] == owner:
                        playlists_id[play['id']] = play['name']
            return playlists_id
      else:
            pass