from bson import ObjectId
from pydantic import BaseModel


class InsertEmployeeResponse(BaseModel):
    id: str


def insert_employee_response(object_id: ObjectId) -> InsertEmployeeResponse:
    response = InsertEmployeeResponse.construct()
    response.id = str(object_id)
    return response
