from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# The ID and range of your spreadsheet
# https://docs.google.com/spreadsheets/d/ - 1DidpF_fBmC0kIrX6rgAKtj9BsxXqeWQDGjiiQ4u5Q9A - /edit#gid=0
SAMPLE_SPREADSHEET_ID = '1DidpF_fBmC0kIrX6rgAKtj9BsxXqeWQDGjiiQ4u5Q9A' # ID is in the url
SAMPLE_RANGE = 'apiTest!A:B' # Make the range column1 : columnN

def main():
    creds = None
    # Move downloaded credentials to this directory or edit the path.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    # Initialize the google sheet using your credentials
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE).execute()

    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            # Print columns A and B, indicies 0 and 1
            print('%s, %s' % (row[0], row[1])) # Should be a way to eliminate hard coding here

if __name__ == '__main__':
    main()


    