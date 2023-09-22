from models import Recipe, UpdateRecipeModel
import motor.motor_asyncio  # MongoDB Driver
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('CLUSTER_PASSWORD')


# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(api_key)
database = client.Users
collection = database.user


async def fetch_one_recipe(id):
    recipe = await collection.find_one({"_id": id})
    if recipe is not None:
        return recipe

async def fetch_all_recipes():
    recipes = []
    cursor = collection.find({})
    async for document in cursor:
        recipes.append(Recipe(**document))
    return recipes

async def create_recipe(recipe):
    document = recipe
    result = await collection.insert_one(document)
    return document

async def update_recipe(id, recipe):
    update_result = await collection.update_one({"_id": id}, {"$set": recipe})
    if update_result.modified_count == 1:
        updated_recipe = await collection.find_one({"_id": id})
        if updated_recipe is not None:
            return updated_recipe
    existing_recipe = await collection.find_one({"_id": id})
    if existing_recipe is not None:
        return existing_recipe

async def remove_recipe(id):
    await collection.delete_one({"_id": id})
    return True