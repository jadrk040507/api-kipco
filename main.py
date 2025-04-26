from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/analyze/")
async def analyze(
    photo: UploadFile = File(...),
    size: str = Form(...),
    material: str = Form(...),
    complexity: str = Form(...)
):
    # Simulamos la lógica de cotización
    base_price = 20

    if size == "Mediano":
        base_price += 10
    elif size == "Grande":
        base_price += 20

    if material == "Premium":
        base_price += 15

    if complexity == "Detallado":
        base_price += 25

    quote = base_price

    category = f"Peluche {size} - {material} - {complexity}"

    return JSONResponse(content={"category": category, "quote": quote})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)