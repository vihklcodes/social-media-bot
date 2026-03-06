#!/usr/bin/env python3
"""Complete OAuth flow to get fresh Google Workspace credentials"""

import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Scopes needed for Google Workspace
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/presentations'
]

# Your credentials
CLIENT_ID = "765308622148-94boo15oji019tce2ndkgk8goprhuk56.apps.googleusercontent.com"
CLIENT_SECRET = "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"

# Create client config
client_config = {
    "installed": {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": ["http://localhost"]
    }
}

# Save to temp file
config_path = '/tmp/client_config.json'
with open(config_path, 'w') as f:
    json.dump(client_config, f)

print("Starting OAuth flow...")
print("This will open a browser window for you to authorize Google Workspace access.\n")

# Run OAuth flow
flow = InstalledAppFlow.from_client_secrets_file(config_path, SCOPES)
creds = flow.run_local_server(port=0)

# Save tokens
token_dir = os.path.expanduser('~/.config/gw-mcp')
os.makedirs(token_dir, exist_ok=True)
token_path = os.path.join(token_dir, 'token.json')

token_data = {
    'token': creds.token,
    'refresh_token': creds.refresh_token,
    'token_uri': creds.token_uri,
    'client_id': creds.client_id,
    'client_secret': creds.client_secret,
    'scopes': creds.scopes
}

with open(token_path, 'w') as token:
    json.dump(token_data, token)

print(f"\n✓ Success! Tokens saved to {token_path}")
print(f"\nRefresh token: {creds.refresh_token}")
print("\nTo make this permanent, add this to your ~/.zshrc:")
print(f'export GOOGLE_WORKSPACE_REFRESH_TOKEN="{creds.refresh_token}"')

# Clean up temp file
os.remove(config_path)
