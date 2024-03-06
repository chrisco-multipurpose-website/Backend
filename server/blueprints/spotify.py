from flask import Blueprint, jsonify, request
import requests
import base64

spotify_bp = Blueprint('spotify', __name__)

SPOTIFY_CLIENT_ID = 'ea64374d1b2149ec9402efa4f22af814'
SPOTIFY_CLIENT_SECRET = '1a34cbb8694146859f13333c371aeee8'
SPOTIFY_PODCAST_ID = '7CcFvqZM7U0K0m6BouNfHe'
SPOTIFY_API_URL = 'https://api.spotify.com/v1'


def get_spotify_token():
    auth_response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={
            'grant_type': 'client_credentials'
        },
        headers={
            'Authorization': f'Basic {base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()}'
        }
    )
    return auth_response.json().get('access_token')


@spotify_bp.get('/latest-episodes')
def get_latest_podcast_episodes():
    token = get_spotify_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(
        f'{SPOTIFY_API_URL}/shows/{SPOTIFY_PODCAST_ID}/episodes',
        headers=headers,
        params={'limit': 9}
    )
    episodes = response.json().get('items', [])
    episode_data = [
        {
            'name': episode['name'],
            'uri': episode['uri'],
            'description': episode['description'],
            'release_date': episode['release_date']
        }
        for episode in episodes
    ]
    return jsonify(episode_data)