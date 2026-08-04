from fastapi import FastAPI, Query, status, HTTPException, UploadFile, UploadFile, File
from typing import List
import random
from contextlib import asynccontextmanager
from schemas import schemapersonCreate, schemaperResponse, schemapersonUpdate, schemapersonBeas
@asynccontextmanager
async def life_time(app: FastAPI):
    print("app is start")
    yield
    print("app is shuting down")



app = FastAPI(lifespan=life_time)
my_list=[{"id":1, "name":"Eli"}, 
         {"id":2, "name":"Milad"},
         {"id":3, "name":"jadi"}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/names",status_code=status.HTTP_201_CREATED, response_model=schemaperResponse)
def add_name(person: schemapersonCreate):
    obj={"id":random.randint(4,100) ,"name":person.name}
    my_list.append(obj)
    return obj

@app.get("/nemes",status_code=status.HTTP_302_FOUND,response_model=List[schemaperResponse])
def list_names(q :str| None=Query(alias="search", default=None, max_length=20)):
    for item in my_list:
        if item["name"]==q:
            return item
    else: return my_list
    
@app.get("/names/{name_id}",status_code=status.HTTP_200_OK, response_model=schemaperResponse)
def chek_name(name_id: int):
    for name in my_list:
       if name["id"]==name_id:
            return name
    

@app.put("/names/{name_id}", status_code=status.HTTP_201_CREATED, response_model=schemaperResponse)
def up_name(person:schemapersonUpdate, name_id:int):
    for oskol in my_list:
        if oskol["id"]==name_id:
            oskol["name"]=person.name
            return oskol

@app.delete("/names/{name_id}",status_code=status.HTTP_204_NO_CONTENT)
def del_item(name_id: int):
    for name in my_list:
        if name["id"]==name_id:
            my_list.remove(name)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item delete")
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item not found")

@app.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()  
    return {"filename": file.filename, "content_type": file.content_type, "file_size": len(content)}



@app.post("/upload-multiple/")
async def upload_multiple(files: List[UploadFile] = File(...)):
    return [
        {"filename": file.filename, "content_type": file.content_type}
        for file in files
    ]