from ninja import Schema


class EnglishNumberOut(Schema):
    status: str
    num_to_english: str


class Error(Schema):
    status: str
    num_to_english: str
