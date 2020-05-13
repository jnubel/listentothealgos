# coding: utf-8

import os, sys, csv
import search_spotify as sspot

def readSourceCsv(file):
    """
    Read a csv file, return a list of rows
    """
    with open(file, 'r', newline='', encoding='utf-8') as csvfile:
        freader = csv.reader(csvfile, delimiter=',')
        rows = [row for row in freader]
        return rows[1:]

def writeResultCsv(file, dict_):
    """
    Write a csv file with a dict as source
    """
    with open(file, 'a', newline='', encoding='utf-8') as csvfile:
        fwriter = csv.writer(csvfile)
        for key, value in dict_.items():
            fwriter.writerow([value, key])

def searchCsvToCsvSpotify(source, destination, type='artist'):
    """
    Search Spotify from a csv file and write the results in another csv file
    """
    for row in readSourceCsv(source):
        writeResultCsv(destination, sspot.searchSpotifyID(row, 'artist'))