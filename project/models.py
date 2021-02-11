from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

#SQA database model
class ItemSQA(Base):
    __tablename__ = 'Items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    is_offer = Column(Boolean)

    def __init__(self, ItemPYD):
        self.name = ItemPYD.name
        self.price = ItemPYD.price
        self.is_offer = ItemPYD.is_offer
    
    def update(self, ItemPYD):
        self.name = ItemPYD.name
        self.price = ItemPYD.price
        self.is_offer = ItemPYD.is_offer
    
    
    def __repr__(self):
        return "<Item(name='{}', price='{}', is_offer={})>"\
                .format(self.name, self.price, self.is_offer)


#Pydantic model - used for validation in fastapi
class ItemPYD(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None