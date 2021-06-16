# image-converter-api-v2

FastAPI:
- Receives multiples images as json string of Image files (from Js for example) 
- Converts it with Pillow by reducing its size up to 10 times
- Returns a list of base64 converted images 


pip install -r requirements.txt to install dependancies

uvicorn app.main:app --reload --port 5000 to run
