
from models import ItemPYD, ItemSQA, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI
from fastapi import FastAPI, APIRouter
import routes

app = FastAPI()
# router = APIRouter()
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


#Get all items
@app.get("/", 
    summary="Get all items",
    description="Returns a list of all items",
    response_description="List of all items",)
async def get_all_items():
    s = Session()
    itemList = s.query(ItemSQA).all()    
    s.close()
    return itemList

#Get specific item
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    s = Session()
    item = s.query(ItemSQA).filter_by(id= item_id).first()    
    s.close()
    return item

#Update item
@app.put("/items/{item_id}")        
async def update_item(item: ItemPYD):
    s = Session()
    result = s.query(ItemSQA).filter_by(name=item.name).first()
    result.update(item)
    s.commit()
    s.close()
    return item

#Post item
@app.post("/items/post/",
    summary="Create an item",
    response_description="The created item")
async def save_new_item(item: ItemPYD):
    #Save in db
    s = Session()
    itemSQA = ItemSQA(item)
    s.add(itemSQA)
    s.commit()  #push to db
    s.refresh(itemSQA) # sets id on obj
    s.close()

    return itemSQA

#Delete item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    s = Session()
    item = s.query(ItemSQA).filter_by(id= item_id).first()
    s.delete(item)
    s.commit()    
    s.close()
    return {"status": "success!"}


def configure():
    app.include_router(routes.router)
    #Add all routers here

def recreate_database():
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


recreate_database()

configure()

if __name__ == '__main__':
   pass
   
    #recreate_database()