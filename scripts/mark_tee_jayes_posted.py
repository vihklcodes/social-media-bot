#!/usr/bin/env python3
"""Mark Tee Jaye's Sunday post as POSTED in Calendar tab"""

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
print("Reading Calendar tab...")
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='Calendar!A:I'
).execute()

rows = result.get('values', [])
print(f"Found {len(rows)} rows\n")

# Find Tee Jaye's Sunday post
for idx, row in enumerate(rows):
    if idx == 0:  # Skip header
        continue

    if len(row) >= 3:
        merchant = row[2] if len(row) > 2 else ''
        day = row[1] if len(row) > 1 else ''

        if 'Tee' in merchant and 'Sunday' in day:
            print(f"Found at row {idx + 1}:")
            print(f"  Post Date: {row[0] if len(row) > 0 else ''}")
            print(f"  Day: {day}")
            print(f"  Merchant: {merchant}")
            print(f"  Occasion: {row[4] if len(row) > 4 else ''}")
            print(f"  Current POSTED status: {row[8] if len(row) > 8 else '(empty)'}")

            # Update POSTED column (column I, index 8)
            update_range = f'Calendar!I{idx + 1}'
            body = {'values': [['POSTED']]}

            update_result = service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=update_range,
                valueInputOption='RAW',
                body=body
            ).execute()

            print(f"\n✓ Updated {update_range} to 'POSTED'")
            print(f"  Updated cells: {update_result.get('updatedCells')}")
            break
else:
    print("⚠ Could not find Tee Jaye's Sunday post in the Calendar tab")
