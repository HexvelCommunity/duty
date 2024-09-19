class Field:
    def __init__(self, field_type):
        self.field_type = field_type


class IntField(Field):
    def __init__(self):
        super().__init__(int)


class StrField(Field):
    def __init__(self):
        super().__init__(str)
