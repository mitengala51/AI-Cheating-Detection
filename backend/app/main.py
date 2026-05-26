from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from ultralytics import YOLO
import os
import shutil
import torch

print("Using Gpu: ", torch.cuda.is_available()) # Must output: True

app = FastAPI()

@app.post("/upload")
async def upload_video(file: UploadFile = File()):

    # Checking runs folder exist or not
    if os.path.isdir('runs'):
        print("Removing the runs folder")
        shutil.rmtree("runs")

    print("Detecting cheating")
    print(file)

    # Setting the custom yolo model
    model = YOLO("app/ajinkya_yolol_bsz6_70epochs.pt")
    
    # Reading and Writing the file
    with open(file.filename, "wb") as f:
        print("Reading File")
        content = await file.read()
        f.write(content)
    print("Calling the predict method")
    print("filename: ", file.filename)
    
    # Calling the predict method to detect cheating in the video
    results = model.predict(file.filename, save=True)
    print("Video Processed Result: ", results[0].save_dir)

    # Renaming the file to send correct file in the response
    proccessed_file = file.filename.rstrip(".mp4") + ".avi"
    print("Proccessed File: ", proccessed_file)

    return FileResponse("runs/detect/predict/" + proccessed_file)