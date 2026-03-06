#!/usr/bin/env python3
"""View Calendar tab to find Tee Jaye's post"""

import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Credentials
CLIENT_ID = "765308622148-94boo15oji019tce2ndkgk8goprhuk56.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REFRESH_TOKEN = "1//05-Nxla1JZH70CgYIARAAGAUSNwF-L9IrACD3zo32RUsEftKnk4EVhP1bXjEzrJTAnB7JRP7WHL7kqtEc_iCS7gfGY1SxpJK6sGQ"

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Create credentials
creds = Credentials(
    token=None,
    refresh_token=REFRESH_TOKEN,
    token_uri="https://oauth2.googleapis.com/token",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scopes=SCOPES
)

# Refresh to get access token
creds.refresh(Request())

# Build service
service = build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1N-snGtkhdYilf4DBMulQLnPkgOlXIHi3Rtkon04Qi28'

# Read Calendar tab
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='Calendar!A:I'
).execute()

rows = result.get('values', [])

print(f"Total rows: {len(rows)}\n")
print("Searching for Tee Jaye's posts...\n")

# Print all rows that contain "Tee" or "Sunday"
for idx, row in enumerate(rows):
    if len(row) >= 3:
        merchant = row[2] if len(row) > 2 else ''
        day = row[1] if len(row) > 1 else ''

        if 'Tee' in merchant or 'Sunday' in day:
            print(f"Row {idx + 1}:")
            for i, cell in enumerate(row):
                print(f"  Col {chr(65+i)}: {cell}")
            print()
