## Aadhaar Card Verification Pipeline 

This project provides a **Python-based pipeline** to verify whether an image is an Aadhaar card or not. The verification is based on:
1. **QR Code Check**: Reads the QR code on the Aadhaar card and extracts the UID and other info.  
2. **Logo Detection**: Uses ORB feature matching to detect the Aadhaar logo.  
3. **Text Extraction**: Uses Tesseract OCR to extract the 12-digit Aadhaar number from the card.

The pipeline can run in two modes:
- **QR verification first** (preferred if the QR is present and readable)
- **Fallback to Logo + Text verification** if QR fails.
----
## Features
- Detects Aadhaar card using **QR code**.
- Detects Aadhaar card using **logo and OCR** as fallback.
- Returns the **Aadhaar number** if successfully verified.
---
## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Pyzbar (`pyzbar`)
- Tesseract OCR (`pytesseract`)
- NumPy
---
