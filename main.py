from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app =FastAPI()

#get home page
@app.get('/')
async def read_route():
    return {"message": "Hello world"}

#get to custom page
@app.get('/greet/')
async def greet_name(name: Optional [str] = "User", age:int = 0)-> dict:
    return{"Message": f"Hello {name}", "age": age}

#get books page
class Bookcreatemodel(BaseModel):
    title: str
    author: str
@app.post('/create_books')
async def create_books(createbooks: Bookcreatemodel):
     return{
         "title":createbooks.title,
         "author":createbooks.author
     }
