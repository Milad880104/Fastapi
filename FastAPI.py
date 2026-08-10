from fastapi import FastAPI, Query, status, HTTPException, UploadFile, UploadFile, File , Depends
from typing import List
import random
from contextlib import asynccontextmanager
from schemas import schemapersonCreate, schemaperResponse, schemapersonUpdate, schemapersonBeas
from database import engin, C1, get_DB, user
from sqlalchemy.orm import Session

@asynccontextmanager
async def life_time(app: FastAPI):
    print("app is start")
    C1.metadata.create_all(engin)
    yield
    print("app is shuting down")



app = FastAPI(lifespan=life_time)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/names",status_code=status.HTTP_201_CREATED, response_model=schemaperResponse)
def add_name(person: schemapersonCreate, DB:Session = Depends(get_DB)):
    us=user(name=person.name)
    DB.add(us)
    DB.commit()
    DB.refresh(us)
    return us
    
    

@app.get("/nemes",status_code=status.HTTP_302_FOUND,response_model=List[schemaperResponse])
def list_names(q :str| None=Query(alias="search", default=None, max_length=20),DB:Session = Depends(get_DB)):
    QU1=DB.query(user)
    if q:
        QU1=QU1.filter_by(name=q)
    re=QU1.all()
    return re
    
@app.get("/names/{name_id}",status_code=status.HTTP_200_OK, response_model=schemaperResponse)
def chek_name(name_id: int, DB:Session = Depends(get_DB)):
    QU2=DB.query(user)
    if name_id:
        QU2=QU2.filter_by(id=name_id)
    re=QU2.first()
    return re
    

@app.put("/names/{name_id}", status_code=status.HTTP_201_CREATED, response_model=schemaperResponse)
def up_name(person:schemapersonUpdate, name_id:int, DB:Session = Depends(get_DB)):
    PR=DB.query(user).filter_by(id=name_id).one_or_none()
    if PR:
        PR.name=person.name
        DB.commit()
        DB.refresh(PR)
        return PR
    

@app.delete("/names/{name_id}")
def del_item(name_id: int, DB: Session = Depends(get_DB)):
    PR = DB.query(user).filter_by(id=name_id).one_or_none()
    if PR:  
        DB.delete(PR)
        DB.commit()
        return HTTPException(status_code=status.HTTP_200_OK, detail="item deleted")
    else: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item not found")
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