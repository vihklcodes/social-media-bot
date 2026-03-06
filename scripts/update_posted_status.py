#!/usr/bin/env python3
"""Update POSTED status for Tee Jaye's Sunday post in Calendar tab"""

import json
import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Load credentials
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
TOKEN_PATH = os.path.expanduser('~/.config/gw-mcp/token.json')

with open(TOKEN_PATH, 'r') as token:
    token_data = json.load(token)

creds = Credentials.from_authorized_user_info(token_data, SCOPES)

if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())
    # Save refreshed token back
    with open(TOKEN_PATH, 'w') as token:
        token.write(creds.to_json())

service = build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1N-snGtkhdYilf4DBMulQLnPkgOlXIHi3Rtkon04Qi28'

# Read Calendar tab
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='Calendar!A:I'
).execute()

rows = result.get('values', [])

print(f"Found {len(rows)} rows in Calendar tab\n")

# Find Tee Jaye's Sunday post
for idx, row in enumerate(rows):
    if len(row) >= 3:
        merchant = row[2] if len(row) > 2 else ''
        day = row[1] if len(row) > 1 else ''

        if 'Tee Jaye' in merchant and 'Sunday' in day:
            print(f"Row {idx + 1}: {row}")
            print(f"  Post Date: {row[0] if len(row) > 0 else ''}")
            print(f"  Day: {day}")
            print(f"  Merchant: {merchant}")
            print(f"  Occasion: {row[4] if len(row) > 4 else ''}")
            print(f"  Current POSTED status: {row[8] if len(row) > 8 else 'empty'}")

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
            print(f"  Cells updated: {update_result.get('updatedCells')}")
            break
else:
    print("Could not find Tee Jaye's Sunday post")
