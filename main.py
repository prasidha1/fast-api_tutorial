from fastapi import FastAPI
app =FastAPI()

#get home page
@app.get('/')
async def read_route():
    return {"message": "Hello world"}

#get to custom page
@app.get('/greet/{name}')
async def greet_name(name:str, age:int)-> dict:
    return{"Message": f"Hello {name}", "age": age}
