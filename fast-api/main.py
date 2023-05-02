from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

inventory = {
    1 : {
        "name": "milk",
        "price": 40.98,
        "brand": "Amul"
    }
}

class Item(BaseModel):
    name:str
    price:float
    brand: Optional[str] = None
    
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def say_hello():
    return {"greet": "Good Afternoon!!!"}

@app.get('/get-all')
def get_all_items():
    return inventory

@app.get('/get-items/{item_id}')
def get_item(item_id: int = Path(description="The ID of the item need to be passed here!!!", gt=0, lt=2)):
    return inventory[item_id]

@app.get('/get-by-name')  # http://localhost:8000/get-by-name?test=2&name=milk ==> works
def get_by_name(test:int, name:Optional[str]): # keep mandatory first, later optional
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found")


@app.post('/create-item/{item_id}')
def create_item(item: Item, item_id:int):
    if item_id in inventory.keys():
        return {"Error": "Id is already exist"}
    # inventory[item_id] = {"name": item.name, "price": item.price, "brand": item.brand}
    inventory[item_id] = item
    
    return inventory[item_id]

@app.put('/update-item/{item_id}')
def update_item(item_id: int, item:UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item Id doesn't exist"}
    # inventory[item_id].update(item)
    
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]


@app.delete('/delete-item/{item_id}')
def delete_item(item_id: int):
    if item_id not in inventory.keys():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found")
    del inventory[item_id]
    
    return {"Success": "Item got deleted sucessfully!!!"}

