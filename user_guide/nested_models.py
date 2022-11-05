from typing import Union, List, Set, Dict

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []
    uniq_tags: Set[str] = []
    avatar: Union[Image, None] = None
    images: Union[List[Image], None] = None

#deeply nested models
class Offer(BaseModel):
    name: str
    desription: Union[str, None] = None
    price: float
    items: List[Item]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

#dict with ogher types
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights