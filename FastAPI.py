from fastapi import FastAPI
import random
app = FastAPI()
my_list=[{"id":1, "name":"Eli"}, 
         {"id":2, "name":"Milad"},
         {"id":3, "name":"jadi"}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/names")
def add_name(name):
    obj={"id":random.randint(4,100) ,"name":name}
    my_list.append(obj)
    return obj

@app.get("/nemes")
def list_names():
    return my_list
@app.get("/names/{name_id}")
def chek_name(name_id):
    for name in my_list:
       if name["id"]==name_id:
            return
    

@app.put("/names/{name_id}")
def up_name(name_id:int,item:str):
    for oskol in my_list:
        if oskol["id"]==name_id:
            oskol["name"]=item
            return oskol

@app.delete("/names/{name_id}")
def del_item(name_id: int):
    for name in my_list:
        if name["id"]==name_id:
            my_list.remove(name)
            return "item delete"
    return "item not found"

