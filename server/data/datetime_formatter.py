from datetime import datetime

datetime_format = '%d/%m/%Y %H:%M:%S'


def get_datetime_from_any(value):
    return get_datetime(str(value))


def get_datetime(timestamp: str) -> datetime:
    return datetime.strptime(timestamp, datetime_format)


def get_string(timestamp: datetime):
    return timestamp.strftime(datetime_format)
