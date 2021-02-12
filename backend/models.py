from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

#SQA database model
class TodoSQA(Base):
    __tablename__ = 'Todos'
    id = Column(Integer, primary_key=True)
    title = Column(String)   
    completed = Column(Boolean)

    def __init__(self, TodoPYD):
        self.title = TodoPYD.title       
        self.completed = TodoPYD.completed
    
    def updateStatus(self, TodoPYD):                     
        self.completed = TodoPYD.completed
    
    
    def __repr__(self):
        return "<Item(title='{}', completed={})>"\
                .format(self.title, self.completed)


#Pydantic model - used for validation in fastapi
class TodoPYD(BaseModel):
    id: Optional[int] = None
    title: str
    completed: Optional[bool] = None