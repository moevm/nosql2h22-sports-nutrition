from server.common.monad import Optional


def first(elements: list) -> Optional:
    return Optional(elements).filter(lambda data: len(data) > 0).map(lambda data: data[0])
