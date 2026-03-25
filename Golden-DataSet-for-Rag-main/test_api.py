#!/usr/bin/env python3
from youtube_transcript_api import YouTubeTranscriptApi

try:
    result = YouTubeTranscriptApi.get_transcript("aircAruvnKk")
    print("API works! Got transcript with", len(result), "entries")
except AttributeError as e:
    print("AttributeError:", e)
except Exception as e:
    print("Other error:", type(e).__name__, "-", e)
