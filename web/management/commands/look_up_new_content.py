from django.core.management.base import BaseCommand, CommandError
from youtube_api.youtube_api_utils import (
    parse_yt_datetime,
    TimeoutError
)
from datetime import datetime, timedelta
import googleapiclient.discovery
import googleapiclient.errors
from django.conf import settings

from web.models import ImagoInfoVideo, ImagoInfoContent
import isodate

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


class Command(BaseCommand):
    help = 'Look up for new content from series'

    def handle(self, *args, **options):
        api_key = settings.YOUTUBE_API_KEY

        youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

        # Lookup all contents
        for content in ImagoInfoContent.objects.filter(type='tvshow', source_id__isnull=False):
            request = youtube.playlistItems().list(
                part = "snippet,contentDetails",
                fields = "items(id,snippet(title,publishedAt),contentDetails)",
                playlistId = content.source_id
            )
            response = request.execute()

            # Only consider content from yesterday on
            published_after = datetime.now() - timedelta(days=1)

            # Create new video for each result
            for item in response.get('items'):
                published_at = parse_yt_datetime(item['snippet'].get('publishedAt'))
                if published_at <= published_after:
                    break
                youtube_video_id = item['contentDetails']['videoId']
                video = ImagoInfoVideo(publication_date=published_at,
                                       title=item['snippet']['title'],
                                       content_id=content.content_id,
                                       thumbnail='youtube',
                                       hosting='youtube',
                                       youtube_id=youtube_video_id,
                                       start_time=0,
                                       end_time=0,
                                       type='tvshow')

                # Grab video duration through another API call
                request = youtube.videos().list(
                    part="contentDetails",
                    id=youtube_video_id,
                    fields = "items(contentDetails(duration))"
                )
                response = request.execute()

                duration = response.get('items')[0]['contentDetails']['duration']
                duration_in_seconds = isodate.parse_duration(duration).total_seconds()
                video.duration = duration_in_seconds

                video.save()
