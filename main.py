from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

products = []


class Product(BaseModel):
    id: int
    name: str


@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/products")
def get_products():
    return products


@app.post("/products")
def add_product(product: Product):
    products.append(product.dict())
    return {
        "message": "Product added successfully",
        "product": product
    }
