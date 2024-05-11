from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from typing import Union
import requests
import os
import logging

# Configure basic logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


API_SERVER_URL = os.getenv("API_SERVER_URL", default="http://localhost:8010")


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, q: Union[str, None] = None):
    try:
        response = requests.get(
            f"{API_SERVER_URL}/items/{item_id}", params={"q": q})
        # Raises HTTPError for bad responses (4XX or 5XX)
        response.raise_for_status()
        item_data = response.json()
        item = Item(**item_data)  # Deserialize the JSON into an Item object
        return item
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")  # Log the error
        raise HTTPException(status_code=500, detail=str(e))
