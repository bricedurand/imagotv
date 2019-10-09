from django.core.management.base import BaseCommand, CommandError
from youtube_api.youtube_api_utils import (
    parse_yt_datetime,
    TimeoutError
)
import youtube_api.parsers as parsers
from datetime import datetime, timedelta
import googleapiclient.discovery
import googleapiclient.errors
from django.conf import settings

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


class Command(BaseCommand):
    help = 'Look up for new content from series'

    def handle(self, *args, **options):
        api_key = settings.YOUTUBE_API_KEY

        youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            # playlistId="PL2U07Dgr_jGVS9lUHpAscSkLtWXv_GOfv"
            playlistId="UU6-BWVphnrCj5xNL73qOd0w"
        )
        response = request.execute()

        videos = []
        published_after = datetime.now() - timedelta(days=7)
        if response.get('items'):
            for item in response.get('items'):
                publish_date = parse_yt_datetime(item['snippet'].get('publishedAt'))
                if publish_date <= published_after:
                    break
                videos.append(parsers.parse_video_url(item))

        print(videos)
