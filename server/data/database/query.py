import json
import re
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


class CaseInsensitiveQueryRepresentation(QueryRepresentation):

    def __init__(self, value, field_name: str):
        self.value = value
        self.field_name = field_name

    def represent(self) -> json:
        return {self.field_name: re.compile('^' + re.escape(self.value) + '$', re.IGNORECASE)}


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
        self.query = {}

    def lazy_get_field_query_json(self):
        if not len(self.query):
            self.query[self.field_name] = {}

        return self.query[self.field_name]

    def represent(self) -> json:
        if self.interval.value_from:
            self.lazy_get_field_query_json()["$gt"] = self.interval.value_from

        if self.interval.value_to:
            self.lazy_get_field_query_json()["$lt"] = self.interval.value_to

        return self.query


class Query:

    def get_json(self):
        return [value.represent() for key, value in vars(self).items()]


class StockInBranchQuery(Query):
    id: IdQueryRepresentation
    supplier_id: FieldEqualsValueQueryRepresentation
    product_id: FieldEqualsValueQueryRepresentation
    name: CaseInsensitiveQueryRepresentation
    amount: IntervalQueryRepresentation
    price_from: IntervalQueryRepresentation


class EmployeeInBranchQuery(Query):
    id: IdQueryRepresentation
    name: CaseInsensitiveQueryRepresentation
    surname: CaseInsensitiveQueryRepresentation
    patronymic: CaseInsensitiveQueryRepresentation
    role: CaseInsensitiveQueryRepresentation
    phone_number: FieldEqualsValueQueryRepresentation
    dismissal_date: IntervalQueryRepresentation
    employment_date: IntervalQueryRepresentation
    salary: IntervalQueryRepresentation


class BranchQuery(Query):
    name: CaseInsensitiveQueryRepresentation
    city: CaseInsensitiveQueryRepresentation
    id: IdQueryRepresentation


def product_id_query(product_id: ObjectId) -> StockInBranchQuery:
    query = StockInBranchQuery()
    query.product_id = IdQueryRepresentation(product_id, "stocks.product._id")
    return query
