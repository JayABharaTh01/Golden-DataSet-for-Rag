# from youtube_transcript_api import YouTubeTranscriptApi
# import os
# import sys
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from config import VIDEO_IDS

# from youtube_transcript_api import YouTubeTranscriptApi
# import os
# import sys
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from config import VIDEO_IDS

# def fetch_transcript(video_id):
#     """Fetch transcript from YouTube"""
#     try:
#         # Instance the API and call fetch method
#         api = YouTubeTranscriptApi()
#         transcript = api.fetch(video_id)
#         if isinstance(transcript, list):
#             text = " ".join([t.get('text', '') for t in transcript])
#         else:
#             text = str(transcript)
#     except Exception as e:
#         print(f"Could not fetch transcript for {video_id}: {e}")
#         # Return mock data for testing
#         text = f"Sample transcript for {video_id}. This is mock data for testing the pipeline."
#     return text

# def save_transcripts():
#     os.makedirs("data/transcripts", exist_ok=True)
    
#     for vid in VIDEO_IDS:
#         text = fetch_transcript(vid)
#         with open(f"data/transcripts/{vid}.txt", "w", encoding="utf-8") as f:
#             f.write(text)

# if __name__ == "__main__":
#     save_transcripts()


from youtube_transcript_api import YouTubeTranscriptApi
import os

VIDEO_IDS = [
    "aircAruvnKk",
    "wjZofJX0v4M",
    "fHF22Wxuyw4",  # Hindi
    "C6YtPJxNULA"   # Hindi
]

def fetch(video_id):
    api = YouTubeTranscriptApi()

    try:
        # 🔥 Try English first, then Hindi
        transcript = api.fetch(video_id, languages=["en", "hi"])

        text = " ".join([item.text for item in transcript])
        return text

    except Exception as e:
        print(f"❌ Error for {video_id}: {e}")
        return ""


def run():
    os.makedirs("data/transcripts", exist_ok=True)

    for vid in VIDEO_IDS:
        print(f"Fetching: {vid}")
        text = fetch(vid)

        if text.strip():
            with open(f"data/transcripts/{vid}.txt", "w", encoding="utf-8") as f:
                f.write(text)
        else:
            print(f"⚠️ Skipped empty transcript: {vid}")


if __name__ == "__main__":
    run()