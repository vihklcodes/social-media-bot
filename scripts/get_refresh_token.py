#!/usr/bin/env python3
"""Extract refresh token from Google OAuth token.json"""

import json
import os

TOKEN_PATH = os.path.expanduser('~/.config/gw-mcp/token.json')

try:
    with open(TOKEN_PATH, 'r') as f:
        token_data = json.load(f)

    if 'refresh_token' in token_data:
        print(f"export GOOGLE_WORKSPACE_REFRESH_TOKEN=\"{token_data['refresh_token']}\"")
    else:
        print("No refresh_token found in token.json")
        print("Token data keys:", list(token_data.keys()))
except FileNotFoundError:
    print(f"Token file not found at {TOKEN_PATH}")
except Exception as e:
    print(f"Error: {e}")
