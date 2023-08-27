from rembg import remove
from fastapi.responses import Response
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def read_root():
    return "OK"

@app.post("/upload/", response_class=Response, responses={200: {"content": {"image/png": {}}}})
async def create_upload_file(file: UploadFile = File(...)):
    content = file.file.read()
    output_data = remove(content)
    return Response(content=output_data, media_type="image/png")
