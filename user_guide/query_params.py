from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/items/')
def get_params(needed: int, not_needed: Union[str, None] = None):
    result = {'needed': needed}
    if not_needed:
        result.update({'not_needed': not_needed})
    return result