from fastapi import FastAPI
from database import engine
from sqlalchemy.orm import Session
import models


# Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(engine)

app = FastAPI(title="address-book", version="1.0.0")

@app.get('/')
def welcome_page():
    return {'msg': 'Welcome to Address Book App'}

@app.post('/add-address')
def add_address(address: models.Address):
    return address