class Optional:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Optional[{self.value}]"

    def get(self):
        if self.value is None:
            raise ValueError("Attempt to get None value")
        return self.value

    def is_present(self):
        return self.value is not None

    def is_empty(self):
        return self.value is None

    def or_raise(self, exception_supplier):
        if self.is_empty():
            raise exception_supplier()
        return self.value

    def or_else(self, other_value):
        if self.is_empty():
            return other_value
        return self.value

    def map(self, func):
        if self.value is None:
            return empty_optional
        return Optional(func(self.value))


empty_optional = Optional(None)
