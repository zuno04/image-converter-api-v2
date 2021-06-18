from fastapi import FastAPI, Body, Request, UploadFile, File
from typing import List, Optional
from .library.iconverter import CustomImage
from random import randint
from pprint import pprint
import json

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

db = []

origins = [
    "http://localhost:5000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/api/reduce_image/")
async def upload_file(files: List[UploadFile] = File(...)):

    db.clear()

    filenames = []

    for file in files:
        contents = await file.read()
        db.append(contents)
        filenames.append(file.filename)

    return { "filenames": filenames }



@app.get("/api/images/")
async def read_random_file(request: Request):

    filenames = json.loads(request.query_params["filenames"])

    reduced_images = []

    if len(db) > 0:

        # print(dir(filenames))

        for index, file in enumerate(filenames):

            # Convert image
            new_image = CustomImage(db[index], file)
            
            response_dic = new_image.reduce_image(size=1, new_quality=50)

            reduced_images.append({ "image_data": response_dic["img"], "image_name": response_dic["image_filename"] })


        return { "converted_images": reduced_images }
    else:
        return {"error": "No image uploaded !!!"}


