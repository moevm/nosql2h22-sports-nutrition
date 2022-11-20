from dataclasses import dataclass


@dataclass
class DtoConstant:
    MAX_STRING_SIZE: int = 30
    MIN_STRING_SIZE: int = 1
    PHONE_REGEX: str = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
    EMAIL_REGEX: str = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
