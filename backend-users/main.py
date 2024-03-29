from database import(
    fetch_one_user,
    fetch_all_users,
    create_user,
    update_user,
    remove_user
)

from fastapi import (FastAPI, HTTPException, Body)
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from models import User, UpdateUser

#App object
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# def read_root():
#     return {"Ping":"Pong"}

@app.get("/")
async def read_root():
    response = {"hello": "world"}
    return response

@app.post("/api/user", response_description="Add a new user", response_model=User, tags=["Users"])
async def post_user(user: User = Body(...)):
    user = jsonable_encoder(user)
    response = await create_user(user)
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")

@app.get("/api/user", tags=["Users"])
async def get_users():
    response = await fetch_all_users()
    return response

@app.get("/api/user/{id}", response_description="Get a single user", response_model=User, tags=["Users"])
async def get_user_by_id(id: str):
    response = await fetch_one_user(id)
    if response:
        return response
    raise HTTPException(404, f"ID {id} not found")

@app.put("/api/user/{id}", response_description="Update a user", response_model=User, tags=["Users"])
async def put_user(id: str, user: UpdateUser = Body(...)):
    user = {k: v for k, v in user.dict().items() if v is not None}
    if len(user) >= 1:
        print("this is user", user)
        response = await update_user(id, user)
    if response:
        return response
    raise HTTPException(404, f"There is no user with this id {id}")

@app.delete("/api/user/{id}", response_description="Delete a user", tags=["Users"])
async def delete_user(id: str):
    response = await remove_user(id)
    if response:
        return "Successfully deleted user item"
    raise HTTPException(404, f"There is no user item with this id:{id}")