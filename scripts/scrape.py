"""Scrape data from Google Sheet, which is where we currently run music club out of

1. First enable the google sheets API and download credentials from:
https://developers.google.com/sheets/api/quickstart/python

2. Install requirements:
pip install -r scripts/scrape.requirements.txt

3. Now you can run this script

Order of data ingestion...
1. Users (see data/users.json)
1.5 ListeningGroup
2. Albums
3. AlbumSubmission
4. AlbumReview
5. Comment
"""

from __future__ import print_function

import os
import os.path
import pickle
import sys
from datetime import datetime, timedelta

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def setup_django():
    import django
    sys.path.insert(0, os.getcwd())
    os.environ['DJANGO_SETTINGS_MODULE'] = 'demo_project.settings'
    django.setup()

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1v1EWfyeFCXOJywb3nCiReke0Zeq-PnfSEs2eh_nLmvo'
CREDENTIALS_FILE = os.path.join('scripts', 'google_sheets_credentials.json')

def parse_album_runtime(runtime):
    """convert album runtimes specified as HH:MM:SS into a datetime.timedelta"""
    t = datetime.strptime(runtime,"%H:%M:%S")
    # ...and use datetime's hour, min and sec properties to build a timedelta
    return timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)


def create_service():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    return service

def get_values(service, cell_range):
    """Get cell values from a Google Spreadsheet"""
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=cell_range).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            yield row

if __name__ == '__main__':
    # start with the first 10 albums
    # HACK: everyones review page MUST be sorted by listening date for this to work. we arent working with databases here!
    album_range = 'Main List!B8:O17'
    reviews = {
        'kent': 'Kent!B29:V38',
        # 'ian': 'Ian!B29:V38',
        # 'colin': 'Colin!B29:V38',
        # 'matt': 'Matt!B29:V38',
        # 'alex': 'Alex!B29:V38',
        # 'scott': 'Scott!B29:V38',
        # 'alexis': 'Alexis!B29:V38',
        # 'john': 'John!B29:V38',
    }

    # setup django so we can script stuff into the DB...
    setup_django()
    from music_club.models import Album, AlbumSubmission, ListeningGroup, AlbumReview
    from django.contrib.auth.models import User
    default_listening_group = ListeningGroup.objects.filter(name='Progenitors')[0]

    # scrape the spreadsheet
    service = create_service()
    for value in get_values(service, album_range):
        album = Album(
            title = value[1],
            artist = value[2],
            year = value[3],
            label = value[4],
            # TODO: mapping function...
            albumType = value[5].lower(),
            country = value[6],
            length = parse_album_runtime(value[7]),
            tracks = value[8],
            genre = value[9],
            subgenre = value[10],
        )
        album.save()

        AlbumSubmission(
            album=album,
            submittedBy=User.objects.get(first_name=value[11]),
            submittedTo=default_listening_group,
            round=value[12],
            theme=None
        ).save()

    for reviewer, cell_range in reviews.items():
        for value in get_values(service, cell_range):
            AlbumReview(
                album=Album.objects.get(title=value[2]),
                reviewedBy=User.objects.get(username=reviewer),
                reviewedOn=datetime.strptime(value[18], "%m/%d/%Y"),
                review=value[20],
                favouriteTrack=value[17],
                expectations=value[19],
            ).save()
