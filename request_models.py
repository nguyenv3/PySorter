from schematics.models import Model
from schematics.types import IntType, BooleanType, StringType
from schematics.types.compound import ListType


class BaseModel(Model):
    descending = BooleanType(default=False)


class NumberPOSTRequest(BaseModel):
    numbers = ListType(IntType, required=True)


class StringPOSTRequest(BaseModel):
    strings = ListType(StringType, required=True)