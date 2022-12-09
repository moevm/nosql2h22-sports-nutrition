from bson import ObjectId

from server.common.exceptions import InvalidQueryList
from server.common.monad import Optional


def split_query_string(query: list) -> list:
    if query is None:
        return None

    string = unpack_first(query)
    array = string.split(', ')

    if not len(array):
        raise InvalidQueryList(string)

    return array


def unpack_first(array: list):
    return first(array).or_else(None)


def object_id(array: list):
    return first(array).map(ObjectId).or_else(None)


def first(elements: list) -> Optional:
    return Optional(elements).filter(lambda data: len(data) > 0).map(lambda data: data[0])


def check(argument, predicate, message):
    if not predicate(argument):
        raise ValueError(message)
    return argument
