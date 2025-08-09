from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI(title="PitStop-AI Lite", version="0.1.0")

@app.get("/health")
def health():
    return {"ok": True, "version": "0.1.0"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    # TODO: save file, run pipeline, build timeline
    return JSONResponse({"video_id": file.filename, "fps": 30, "events": []})
