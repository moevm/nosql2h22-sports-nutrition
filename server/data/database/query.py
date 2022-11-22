import json
from abc import ABC, abstractmethod

from bson import ObjectId


class IntervalHolder:

    def __init__(self, value_from, value_to):
        self.value_from = value_from
        self.value_to = value_to


class QueryRepresentation(ABC):

    @abstractmethod
    def represent(self) -> json:
        pass


class FieldEqualsValueQueryRepresentation(QueryRepresentation):

    def __init__(self, value, field_name: str):
        self.value = value
        self.field_name = field_name

    def represent(self) -> json:
        return {self.field_name: self.value}


class IdQueryRepresentation(FieldEqualsValueQueryRepresentation):

    def __init__(self, value, field_name='_id'):
        super().__init__(value, field_name)


class IntervalQueryRepresentation(QueryRepresentation):

    def __init__(self, interval: IntervalHolder, field_name: str):
        self.interval = interval
        self.field_name = field_name

    def represent(self) -> json:
        json_query = {}

        if self.interval.value_from:
            json_query[self.field_name] = {"$gt": self.interval.value_from}

        if self.interval.value_to:
            json_query[self.field_name] = {"$lt": self.interval.value_to}

        return json_query


class Query:

    def get_json(self):
        return [value.represent() for key, value in vars(self).items()]


class StockInBranchQuery(Query):
    id: IdQueryRepresentation
    supplier_id: FieldEqualsValueQueryRepresentation
    product_id: FieldEqualsValueQueryRepresentation
    name: FieldEqualsValueQueryRepresentation
    amount: IntervalQueryRepresentation
    price_from: IntervalQueryRepresentation


class EmployeeInBranchQuery(Query):
    id: IdQueryRepresentation
    name: FieldEqualsValueQueryRepresentation
    surname: FieldEqualsValueQueryRepresentation
    patronymic: FieldEqualsValueQueryRepresentation
    role: FieldEqualsValueQueryRepresentation
    phone_number: FieldEqualsValueQueryRepresentation
    dismissal_date: IntervalQueryRepresentation
    employment_date: IntervalQueryRepresentation
    salary: IntervalQueryRepresentation


class BranchQuery(Query):
    name: FieldEqualsValueQueryRepresentation
    city: FieldEqualsValueQueryRepresentation
    id: IdQueryRepresentation


def product_id_query(product_id: ObjectId) -> StockInBranchQuery:
    query = StockInBranchQuery()
    query.product_id = IdQueryRepresentation(product_id, "stocks.product._id")
    return query
