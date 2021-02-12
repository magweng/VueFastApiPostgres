
from models import TodoPYD, TodoSQA, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import routes

app = FastAPI()

#Speak to frontend on localhost
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# router = APIRouter()
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


#Get all items
@app.get("/todos/", 
    summary="Get all todos",
    description="Returns a list of all todos",
    response_description="List of all todos",)
async def get_all_todos():
    s = Session()
    todos = s.query(TodoSQA).all()    
    s.close()
    return todos

#Get specific item
@app.get("/todo/{todo_id}")
async def get_todo_with_id(todo_id: int):
    s = Session()
    todo = s.query(TodoSQA).filter_by(id= todo_id).first()    
    s.close()
    return todo

#Update item
@app.put("/todo/update/{todo_id}")        
async def update_todo(todo: TodoPYD, todo_id: int):
    s = Session()
    result = s.query(TodoSQA).filter_by(id= todo_id).first()
    result.updateStatus(todo)
    s.commit()
    s.close()
    return TodoPYD

#Post item
@app.post("/todo/post/")   
async def save_new_todo(todo: TodoPYD):
    #Save in db
    s = Session()
    todo = TodoSQA(todo)
    s.add(todo)
    s.commit()  #push to db
    s.refresh(todo) # sets id on obj
    s.close()

    return todo

#Delete item
@app.delete("/todo/{id}")
async def delete_todo(id: int):
    s = Session()
    todo = s.query(TodoSQA).filter_by(id= id).first()
    s.delete(todo)
    s.commit()    
    s.close()
    return {"status": "success!"}


def configure():
    app.include_router(routes.router)
    #Add all routers here

def recreate_database():
   # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

configure()
recreate_database()

if __name__ == '__main__':
   pass