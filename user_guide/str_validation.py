from typing import Union, List

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/list/")
async def read_list(q: Union[List[str], None] = Query(default=['foo', 'bar'])):
    list_items = {"q": q}
    return list_items

@app.get("/show_meta/")
async def show_meta(param: Union[str, None] = Query(
    default=None,
    title='meta_title',
    description='meta_description'
)):
    return {"param": param}
