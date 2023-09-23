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

class ProfilePhoto(BaseModel):
    photo_id: str

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    firebase_reference_id: str
    authored_recipes: Optional[List[str]]
    favorites: Optional[List[str]]
    profile_photo: Optional[ProfilePhoto]
    profile_description: Optional[str]



    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "User": {
                "firebase_reference_id":"EZonoo2pWjhfhkgDaHsfUdZvwsJ2",
                "authored_recipes": "Bolognese",
                "favorites":"TEST Food",
                "profile_photo":[{"url":"https://shorturl.at/nDIR5","alt_text":"bolognese"},{"url":"https://shorturl.at/gzU37","alt_text":"mirepoix"}],
                "profile_description":"I am a good cook"
            }
        }


class UpdateUser(BaseModel):
    firebase_reference_id: str
    authored_recipes: Optional[List[str]]
    favorites: Optional[List[str]]
    profile_photo: Optional[ProfilePhoto]
    profile_description: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "User": {
                "firebase_reference_id":"EZonoo2pWjhfhkgDaHsfUdZvwsJ2",
                "authored_recipes": "Bolognese",
                "favorites":"TEST Food",
                "profile_photo":[{"url":"https://shorturl.at/nDIR5","alt_text":"bolognese"},{"url":"https://shorturl.at/gzU37","alt_text":"mirepoix"}],
                "profile_description":"I am a good cook"
            }
        }