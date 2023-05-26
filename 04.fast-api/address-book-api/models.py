from database import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import Optional

# class Address(Base):
    
#     __tablename__ = 'addresses'
    
#     id = Column(Integer, primary_key=True, index=True)
#     address = Column(String)
#     city = Column(String)
#     state = Column(String)
#     latitude = Column(String)
#     longitude = Column(String)
    
class Address(BaseModel):
    id: int
    address: str
    city: str
    state: Optional[str]
    latitude: str
    longitude: str