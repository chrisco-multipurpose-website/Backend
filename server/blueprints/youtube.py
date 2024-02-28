from flask import Blueprint, jsonify, request
import requests

youtube_bp = Blueprint('youtube', __name__)

YOUTUBE_API_KEY = 'AIzaSyDdf_fWqeBxwtIfAihoayRMyl_idE64OKg'
CHANNEL_ID = 'UCx3_YD5Skpopibo0OUGKL0Q'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

@youtube_bp.get('/latest-videos')
def get_latest_videos():
    params = {
        'part': 'snippet',
        'channelId': CHANNEL_ID,
        'maxResults': 3,
        'order': 'date',
        'type': 'video',
        'key': YOUTUBE_API_KEY
    }
    response = requests.get(YOUTUBE_API_URL, params=params)
    videos = response.json().get('items', [])
    video_data = [
        {
            'title': video['snippet']['title'],
            'videoId': video['id']['videoId'],
            'thumbnail': video['snippet']['thumbnails']['high']['url']
        }
        for video in videos
    ]
    return jsonify(video_data), 200