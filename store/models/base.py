from datetime import datetime
from decimal import Decimal
from typing import Any
from uuid import uuid4
from bson import Decimal128
from pydantic import UUID4, BaseModel, Field, model_serializer


class CreateBaseModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())

    @model_serializer
    def set_model(self) -> dict[str, Any]:
        self._dict = dict(self)

        for key, value in self._dict.items():
            if isinstance(value, Decimal):
                self._dict[key] = Decimal128(str(value))

        return self._dict