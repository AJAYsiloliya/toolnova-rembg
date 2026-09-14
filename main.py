from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove

app = FastAPI()

@app.post("/remove")
async def remove_background(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data)

    return Response(
        content=output_data,
        media_type="image/png"
    )
  
