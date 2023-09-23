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


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    firebase_reference_id: str
    authored_recipes: Optional[List[str]]
    favorites: Optional[List[str]]
    profile_photo: Optional[str]
    profile_description: Optional[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "User": {
                "username":"username",
                "firebase_reference_id":"EZonoo2pWjhfhkgDaHsfUdZvwsJ2",
                "authored_recipes": ["Bolognese"],
                "favorites": ["TEST Food"],
                "profile_photo":"HTML link to where photo is stored",
                "profile_description":"I am a good cook"
            }
        }


class UpdateUser(BaseModel):
    username: Optional[str]
    firebase_reference_id: Optional[str]
    authored_recipes: Optional[List[str]]
    favorites: Optional[List[str]]
    profile_photo: Optional[str]
    profile_description: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "User": {
                "username":"user_name",
                "firebase_reference_id":"EZonoo2pWjhfhkgDaHsfUdZvwsJ2",
                "authored_recipes": ["Bolognese"],
                "favorites":["TEST Food"],
                "profile_photo":"HTML link to the hosted location of the profile photo",
                "profile_description":"I am a good cook"
            }
        }