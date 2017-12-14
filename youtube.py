import flask
import requests
import json
import random
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


API_KEY = "AIzaSyARr1Hzel4aDC8sbmWSgvtxT3yHvZ_eo90"
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(search_argument):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
  search_response = youtube.search().list(
    q = search_argument,
    part='id,snippet',
  ).execute()

  video_id = []
  #This will grab the video ID from the API and append them to an array. 
  #It will return a random id in the array.
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      video_id.append(search_result['id']['videoId'])  
  random_video = random.choice(video_id)
  return random_video

