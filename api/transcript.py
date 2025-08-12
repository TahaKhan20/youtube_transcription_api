from fastapi import FastAPI
from fastapi.responses import JSONResponse
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/api/transcript/{videoID}")
async def fetch_transcript(videoID: str):
    try:
        fetched_transcript = YouTubeTranscriptApi.get_transcript(videoID)
        text_snippets = [snippet['text'] for snippet in fetched_transcript]
        return {
            "videoID": videoID,
            "snippet_count": len(fetched_transcript),
            "last_snippet": fetched_transcript[-1],
            "text_snippets": text_snippets
        }
    except Exception as e:
        return JSONResponse(status_code=404, content={"error": str(e)})
