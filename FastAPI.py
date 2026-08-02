from fastapi import FastAPI, Query, status, HTTPException
import random
app = FastAPI()
my_list=[{"id":1, "name":"Eli"}, 
         {"id":2, "name":"Milad"},
         {"id":3, "name":"jadi"}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/names",status_code=status.HTTP_201_CREATED)
def add_name(name):
    obj={"id":random.randint(4,100) ,"name":name}
    my_list.append(obj)
    return obj

@app.get("/nemes",status_code=status.HTTP_302_FOUND)
def list_names(q :str| None=Query(alias="search", default=None, max_length=20)):
    for item in my_list:
        if item["name"]==q:
            return item
    else: return my_list
    
@app.get("/names/{name_id}",status_code=status.HTTP_200_OK)
def chek_name(name_id):
    for name in my_list:
       if name["id"]==name_id:
            return
    

@app.put("/names/{name_id}", status_code=status.HTTP_201_CREATED)
def up_name(name_id:int,item:str):
    for oskol in my_list:
        if oskol["id"]==name_id:
            oskol["name"]=item
            return oskol

@app.delete("/names/{name_id}",status_code=status.HTTP_204_NO_CONTENT)
def del_item(name_id: int):
    for name in my_list:
        if name["id"]==name_id:
            my_list.remove(name)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item delete")
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item not found")

