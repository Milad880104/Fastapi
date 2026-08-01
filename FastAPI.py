from fastapi import FastAPI

app = FastAPI()
my_list=[{"id":1, "name":"Eli"}, 
         {"id":2, "name":"Milad"},
         {"id":3, "name":"jadi"}]

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/nemes")
def list_names():
    return my_list
@app.get("/names/{name_id}")
def chek_name(name_id):
    for name in my_list:
       if name["id"]==name_id:
            return
    
