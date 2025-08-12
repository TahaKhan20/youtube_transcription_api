from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/transcript/{videoID}")
async def fetch_transcript(videoID: str):
    try:
        # Fetch transcript using video ID from the URL
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(videoID)

        # Extract text from all snippets
        text_snippets = [snippet['text'] for snippet in fetched_transcript]

        # Get the last snippet
        last_snippet = fetched_transcript[-1]

        # Get the total number of snippets
        snippet_count = len(fetched_transcript)

        return {
            "videoID": videoID,
            "snippet_count": snippet_count,
            "last_snippet": last_snippet,
            "text_snippets": text_snippets
        }

    except Exception as e:
        return JSONResponse(status_code=404, content={"error": str(e)})
