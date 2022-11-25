from bson import ObjectId
from pydantic import Field, BaseModel


class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required')
        return str(v)


class SerializableObjectId(BaseModel):
    id: str = Field(alias='_id')
