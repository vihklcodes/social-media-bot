#!/usr/bin/env python3
"""Mark Tee Jaye's March 1 Sunday post as POSTED"""

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

# Update row 16 (March 1 Sunday post)
row_number = 16
update_range = f'Calendar!I{row_number}'

print(f"Updating {update_range} to 'POSTED'...")

body = {'values': [['POSTED']]}

result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range=update_range,
    valueInputOption='RAW',
    body=body
).execute()

print(f"\n✓ Success!")
print(f"  Updated row: {row_number}")
print(f"  Post date: 2026-03-01 (Sun)")
print(f"  Occasion: Lent-Friendly Fish Sandwich")
print(f"  Cells updated: {result.get('updatedCells')}")
