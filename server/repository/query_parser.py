def get_dict_from_tuple(target):
    key, value = target
    return {key: value}


def parse_query_items(items) -> list:
    return list(get_dict_from_tuple(query_filter) for query_filter in items if query_filter[1] is not None)
