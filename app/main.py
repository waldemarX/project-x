from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    id: int
    name: str


items = {}


@app.get("/")
def create_item():
    if items:
        id = max(items.keys()) + 1
    else:
        id = 0
    item = Item(id=id, name=f"Item {id}")
    items[id] = item
    return {"message": f"Item created with id {item.id}"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    item: Item = items.get(item_id)
    if item:
        return {"item": item.model_dump()}
    else:
        return {"message": "Item not found"}


@app.get("/items/")
def get_all_items():
    return {"items": items}