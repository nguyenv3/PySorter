from schematics.models import Model
from schematics.types import IntType
from schematics.types.compound import ListType


class NumberPOSTRequest(Model):
    numbers = ListType(IntType, required=True)