from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    1: {
        "name": "milk",
        "price": 3.34,
        "brand": "Pınar"
    }
}


@app.get("/items/{id}")
def home(item_id: int = Path(None, description="the id must be")):
    return inventory[item_id]
