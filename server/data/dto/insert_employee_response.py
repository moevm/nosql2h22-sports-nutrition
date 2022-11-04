from bson import ObjectId


class InsertEmployeeResponse:
    id: str

    def __init__(self, object_id: ObjectId):
        self.id = str(object_id)
