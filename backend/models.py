# from typing import Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from typing import Optional, List
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# Recipe Models Start

class RecipeStep(BaseModel):
    step_number: int
    description: str

class RecipeIngredient(BaseModel):
    name: str
    amount: str

class RecipeImage(BaseModel):
    photo_id: str


class Recipe(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    category: Optional[str]
    title: str
    description: Optional[str]
    create_date: str
    ingredients: List[RecipeIngredient]
    steps: List[RecipeStep]
    images: Optional[List[RecipeImage]]
    serving_size: Optional[str]
    cooking_time: Optional[str]
    difficulty: Optional[str]
    author: str


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "Recipe": {
                "category": "Entree",
                "title": "Bolognese",
                "description": "Classic Italian Sunday Ragu",
                "create_date": "2008-09-15",
                "ingredients": [{"name":"carrots","amount":"200g"},{"name":"celery", "amount":"200g"},{"name":"onions", "amount":"200g"}],
                "steps": [{"step_number":1, "description":"prep stuff"},{"step_number":2, "description":"cook stuff"},{"step_number":3, "description":"eat stuff"}],
                "images":[{"url":"https://shorturl.at/nDIR5","alt_text":"bolognese"},{"url":"https://shorturl.at/gzU37","alt_text":"mirepoix"}],
                "author":"EZonoo2pWjhfhkgDaHsfUdZvwsJ2"
            }
        }


class UpdateRecipeModel(BaseModel):
    category: Optional[str]
    title: Optional[str]
    description: Optional[str]
    create_date: str
    ingredients: Optional[List[RecipeIngredient]]
    steps: Optional[List[RecipeStep]]
    images: Optional[List[RecipeImage]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "Recipe": {
                "category": "Entree",
                "title": "Bolognese",
                "description": "Classic Italian Sunday Ragu",
                "create_date": "2008-09-15",
                "ingredients": [{"name":"carrots","amount":"200g"},{"name":"celery", "amount":"200g"},{"name":"onions", "amount":"200g"}],
                "steps": [{"step_number":1, "description":"prep stuff"},{"step_number":2, "description":"cook stuff"},{"step_number":3, "description":"eat stuff"}],
                "images":[{"url":"https://shorturl.at/nDIR5","alt_text":"bolognese"},{"url":"https://shorturl.at/gzU37","alt_text":"mirepoix"}]
            }
        }