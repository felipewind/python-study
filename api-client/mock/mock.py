from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, q: Union[str, None] = None):
    # Example data for demonstration; in a real application,
    # this might come from a database or other source
    example_item = Item(name="Sample Item", price=100.0,
                        is_offer=True if q else False)
    return example_item
