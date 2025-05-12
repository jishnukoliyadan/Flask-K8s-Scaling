import uvicorn
import numpy as np
from random import choice, randint
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse


app = FastAPI()

ELECTRONICS = [
    {
        "name": "Smartphone",
        "model": "iPhone 14",
        "category": "Mobile",
        "prices": [1099.99, 999.99, 1050.00, 1150.00],
    },
    {
        "name": "Headphones",
        "model": "WH-1000XM5",
        "category": "Audio",
        "prices": [399.99, 349.99, 360.00, 379.99],
    },
    {
        "name": "Smartwatch",
        "model": "Galaxy Watch 5",
        "category": "Wearables",
        "prices": [299.99, 279.99, 290.00, 310.00],
    },
]


def matrixCalc(maxSize: int = 1500) -> np.ndarray:
    if maxSize > 2000:
        return "Matrix size above 2000"
    matrix_a = np.random.rand(maxSize, maxSize)
    matrix_b = np.random.rand(maxSize, maxSize)
    return np.matmul(matrix_a, matrix_b)


@app.get("/", response_class=HTMLResponse)
async def home():
    radint = randint(1, 50)
    return f"""
    <html>
        <head>
            <title>FastAPI Home</title>
        </head>
        <body>
            <h1>Welcome to the FastAPI App</h1>
            <p>Please go to the sample <a href="/products/{radint}?max_size=1000">Products Endpoint</a>.</p>
        </body>
    </html>
    """


@app.get("/products/{item_number}")
async def get_items(item_number: int, max_size: int = 1000) -> dict:
    product = choice(ELECTRONICS)
    if not isinstance(matrixCalc(max_size), np.ndarray):
        raise HTTPException(status_code=400, detail=f"Keep 'max_size' below 2000, current: {max_size}")
    return {
        "item_number": item_number,
        "name": product.get("name"),
        "model": product.get("model"),
        "category": product.get("category"),
        "price": choice(product.get("prices")),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
