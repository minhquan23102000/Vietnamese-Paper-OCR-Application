import base64
import io
import os
import shutil
from os import getcwd
from pathlib import Path
from tempfile import NamedTemporaryFile

import cv2
import numpy
from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import JSONResponse
from paper_ocr.ocr_reader import OCRReader
from PIL import Image
from starlette.responses import RedirectResponse


def create_api():
    # init app
    app = FastAPI()

    @app.get("/")
    def index():
        return RedirectResponse("/docs")

    @app.post("/api")
    def api(file: UploadFile = File(...)):
        # ràng buộc mở rộng
        ext = file.filename.split(".")[-1] in ("png", "jpg", "jpeg", "jfif")
        if not ext:
            return "Ảnh không đúng định dạng. Vui lòng thử lại!"

        try:
            suffix = Path(file.filename).suffix
            with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                shutil.copyfileobj(file.file, tmp)
                tmp_path = Path(tmp.name)
        finally:
            file.file.close()

        # #lý tưởng
        pil_image = Image.open(tmp_path).convert("RGB")
        open_cv_image = numpy.array(pil_image)
        # Convert RGB to BGR
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        # image = cv2.imread(image_cv2)
        ocr = OCRReader()
        result = dict()
        result = ocr.read("hocba", open_cv_image)
        return result

    @app.post("/api_base64")
    async def get_body(request: Request):
        # receive body from client
        json = await request.json()
        type = json["type"]
        print("body : ", type)
        # get image
        img_base64 = json["image"]
        print("image deco: ", img_base64)
        # read and open image from body
        img = base64.b64decode(str(img_base64))
        print(img)
        image = Image.open(io.BytesIO(img))

        if len(json["image"]) == 0:
            return "Error"

        open_cv_image = cv2.cvtColor(numpy.array(image), cv2.COLOR_BGR2RGB)
        # Convert RGB to BGR
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        # image = cv2.imread(image_cv2)
        ocr = OCRReader()
        result = dict()
        result = ocr.read(str(type), open_cv_image)
        return result

    return app
