from pydantic import UUID4, ValidationError
import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_sucess():
    product = ProductIn.model_validate(product_data())

    assert product.name == "Iphone 14 pro Max"

def test_schemas_return_raise():
    data = {'name': 'Iphone 14 pro Max', 'quantity': 5, 'price': 8.000}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 14 pro Max", "quantity": 5, "price": 8.0},
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }