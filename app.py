from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
from pathlib import Path
from aadhaar_verification import verify_aadhaar_card

app = FastAPI(title="Aadhaar Verification API")

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

LOGO_PATH = "aadhaar_logo.png"

@app.post("/verify_aadhaar/")
async def verify_aadhaar(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run verification
    result = verify_aadhaar_card(str(file_path), LOGO_PATH)

    # Clean up uploaded file
    os.remove(file_path)

    return JSONResponse(content=result)

@app.get("/")
def home():
    return {"message": "Aadhaar Verification API is running!"}
