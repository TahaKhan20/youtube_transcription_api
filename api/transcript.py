from fastapi import FastAPI, Request
from youtube_transcript_api import YouTubeTranscriptApi
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/transcript")
async def get_transcript(videoID: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(videoID)
        return JSONResponse(content={"transcript": transcript})
    except Exception as e:
        return JSONResponse(status_code=404, content={"error": str(e)})
