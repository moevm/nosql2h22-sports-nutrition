import json
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from logging import info

from bson import ObjectId

from server.common.exceptions import EmptyQuery


@dataclass
class Constant:
    AND: str = "$and"


@dataclass
class IntervalHolder:

    def __init__(self, value_from, value_to):
        self.value_from = value_from
        self.value_to = value_to


class QueryRepresentation(ABC):

    @abstractmethod
    def represent(self) -> json:
        pass


class RegexQueryRepresentation(QueryRepresentation):

    def __init__(self, field_name: str, value: str):
        self.value = value
        self.field_name = field_name

    def represent(self) -> json:
        return {self.field_name: re.compile(re.escape(self.value), re.IGNORECASE)}


class FieldEqualsValueQueryRepresentation(QueryRepresentation):

    def __init__(self, field_name: str, value):
        self.value = value
        self.field_name = field_name

    def represent(self) -> json:
        return {self.field_name: self.value}


class IdQueryRepresentation(FieldEqualsValueQueryRepresentation):

    def __init__(self, value, field_name='_id'):
        if isinstance(value, str):
            super().__init__(field_name, ObjectId(value))
        elif isinstance(value, ObjectId):
            super().__init__(field_name, value)
        else:
            raise ValueError("Id in IdQueryRepresentation must be instance of str or ObjectId")

    @staticmethod
    def from_first_element(self, elements: list):
        return self.__init__(elements[0])


class IntervalQueryRepresentation(QueryRepresentation):

    def __init__(self, field_name: str, interval: IntervalHolder):
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


class ArraySizeIntervalQueryRepresentation(IntervalQueryRepresentation):

    def __init__(self, field_name: str, interval: IntervalHolder):
        super().__init__(field_name, interval)

    def represent(self) -> json:
        if self.interval.value_from:
            self.lazy_get_field_query_json()["$gt"] = {
                "$size": self.interval.value_from
            }

        if self.interval.value_to:
            self.lazy_get_field_query_json()["$lt"] = {
                "$size": self.interval.value_to
            }

        return self.query


class AllArrayQueryRepresentation(QueryRepresentation):

    def __init__(self, field_name: str, value: list):
        self.value = value
        self.field_name = field_name

    def represent(self) -> json:
        return {
            self.field_name: {
                "$all": self.value
            }
        }


@dataclass
class Query:
    def __init__(self, query_json: json):
        self.__query_json = query_json

    def get_json(self):
        return self.__query_json


class ConditionBuilder:

    def __init__(self, target: list, parent, field_name: str):
        self.__target = target
        self.__parent = parent
        self.__field_name = field_name

    def __build(self, value, supplier):
        if value is None:
            return self.__parent

        self.__target.append(supplier())
        return self.__parent

    def contains_all(self, array: list):
        return self.__build(array, lambda: AllArrayQueryRepresentation(self.__field_name, array))

    def equals(self, value):
        return self.__build(value, lambda: FieldEqualsValueQueryRepresentation(self.__field_name, value))

    def size_in_interval(self, value: IntervalHolder):
        return self.__build(value, lambda: ArraySizeIntervalQueryRepresentation(self.__field_name, value))

    def in_interval(self, value: IntervalHolder):
        return self.__build(value, lambda: IntervalQueryRepresentation(self.__field_name, value))

    def has_id(self, value):
        return self.__build(value, lambda: IdQueryRepresentation(value, self.__field_name))

    def equals_regex(self, value: str):
        return self.__build(value, lambda: RegexQueryRepresentation(self.__field_name, value))


class FieldNameSetter:

    def __init__(self, condition_builder_function):
        self.function = condition_builder_function

    def field(self, field_name: str) -> ConditionBuilder:
        return self.function(field_name)


class QueryBuilder:

    def __init__(self):
        self.__and_conditions = []

    def __is_conditions_not_present(self):
        return not len(self.__and_conditions)

    def __check_consistent(self):
        if self.__is_conditions_not_present():
            raise EmptyQuery()

    def compile(self) -> Query:
        self.__check_consistent()

        compiled = {
            Constant.AND: [condition.represent() for condition in self.__and_conditions]
        }

        info(f"Compiled query: {compiled}")

        return Query(compiled)

    def and_condition(self):
        return FieldNameSetter(lambda field_name: ConditionBuilder(self.__and_conditions, self, field_name))


def product_id_query(product_id: ObjectId) -> Query:
    return QueryBuilder().and_condition().field("stocks.product._id").equals(product_id).compile()
