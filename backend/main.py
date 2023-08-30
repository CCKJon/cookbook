from fastapi import FastAPI, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

#App object
app = FastAPI()

from models import Recipe, UpdateRecipeModel

from database import(
    fetch_one_recipe,
    fetch_all_recipes,
    create_recipe,
    update_recipe,
    remove_recipe
)

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

@app.get("/api/recipe", tags=["Recipes"])
async def get_recipes():
    response = await fetch_all_recipes()
    return response

@app.get("/api/recipe/{id}", response_description="Get a single recipe", response_model=Recipe, tags=["Recipes"])
async def get_recipe_by_id(id: str):
    response = await fetch_one_recipe(id)
    if response:
        return response
    raise HTTPException(404, f"ID {id} not found")

@app.post("/api/recipe", response_description="Add a new recipe", response_model=Recipe, tags=["Recipes"])
async def post_recipe(recipe: Recipe = Body(...)):
    recipe = jsonable_encoder(recipe)
    response = await create_recipe(recipe)
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")

@app.put("/api/recipe/{id}", response_description="Update a recipe", response_model=Recipe, tags=["Recipes"])
async def put_recipe(id: str, recipe: UpdateRecipeModel = Body(...)):
    recipe = {k: v for k, v in recipe.dict().items() if v is not None}
    if len(recipe) >= 1:
        response = await update_recipe(id, recipe)
    if response:
        return response
    raise HTTPException(404, f"There is no recipe with this id {id}")

@app.delete("/api/recipe/{id}", response_description="Delete a recipe", tags=["Recipes"])
async def delete_recipe(id: str):
    response = await remove_recipe(id)
    if response:
        return "Successfully deleted recipe item"
    raise HTTPException(404, f"There is no recipe item with this id:{id}")