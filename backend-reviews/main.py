from fastapi import FastAPI, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

#App object
app = FastAPI()

from models import Review, UpdateReviewModel

from database import(
    fetch_one_review,
    fetch_all_reviews,
    create_review,
    update_review,
    remove_review
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

@app.get("/api/review", tags=["Reviews"])
async def get_reviews():
    response = await fetch_all_reviews()
    return response

@app.get("/api/review/{id}", response_description="Get a single review", response_model=Review, tags=["Reviews"])
async def get_review_by_id(id: str):
    response = await fetch_one_review(id)
    if response:
        return response
    raise HTTPException(404, f"ID {id} not found")

@app.post("/api/review", response_description="Add a new review", response_model=Review, tags=["Reviews"])
async def post_review(review: Review = Body(...)):
    review = jsonable_encoder(review)
    response = await create_review(review)
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")

@app.put("/api/review/{id}", response_description="Update a review", response_model=Review, tags=["Reviews"])
async def put_review(id: str, review: UpdateReviewModel = Body(...)):
    review = {k: v for k, v in review.dict().items() if v is not None}
    if len(review) >= 1:
        response = await update_review(id, review)
    if response:
        return response
    raise HTTPException(404, f"There is no review with this id {id}")

@app.delete("/api/review/{id}", response_description="Delete a review", tags=["Reviews"])
async def delete_review(id: str):
    response = await remove_review(id)
    if response:
        return "Successfully deleted review item"
    raise HTTPException(404, f"There is no review item with this id:{id}")