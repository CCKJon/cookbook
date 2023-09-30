from models import Review, UpdateReviewModel
import motor.motor_asyncio  # MongoDB Driver
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('CLUSTER_PASSWORD')


# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(api_key)
database = client.ReviewList
collection = database.review


async def fetch_one_review(id):
    review = await collection.find_one({"_id": id})
    if review is not None:
        return review

async def fetch_all_reviews():
    reviews = []
    cursor = collection.find({})
    async for document in cursor:
        reviews.append(Review(**document))
    return reviews

async def create_review(review):
    document = review
    result = await collection.insert_one(document)
    return document

async def update_review(id, review):
    update_result = await collection.update_one({"_id": id}, {"$set": review})
    if update_result.modified_count == 1:
        updated_review = await collection.find_one({"_id": id})
        if updated_review is not None:
            return updated_review
    existing_review = await collection.find_one({"_id": id})
    if existing_review is not None:
        return existing_review

async def remove_review(id):
    await collection.delete_one({"_id": id})
    return True