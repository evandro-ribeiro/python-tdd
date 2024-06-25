from typing import List

import pytest
from tests.factories import product_data
from fastapi import HTTPException, status

async def test_controller_create_should_return_sucess(client, products_url):
    response = await client.post(products_url, json=product_data())

    assert response.status_code == status.HTTP_201_CREATED

async def test_controller_get_should_return_sucess(client, products_url, product_inserted):
    response = await client.get(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_200_OK

async def test_controller_get_should_return_not_found(client, products_url):
    response = await client.get(f"{products_url}d7e64c43-ce9f-4de5-8819-55ce713289ce")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Not Found'}

@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_should_return_sucess(client, products_url):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1

async def test_controller_patch_should_return_sucess(client, products_url, product_inserted):
    response = await client.patch(f"{products_url}{product_inserted.id}", json={"quantity": 40})

    assert response.status_code == status.HTTP_200_OK

async def test_controller_delete_should_return_no_content(client, products_url, product_inserted):
    response = await client.patch(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT

async def test_controller_delete_should_return_not_found(client, products_url):
    response = await client.delete(f"{products_url}d7e64c43-ce9f-4de5-8819-55ce713289ce")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Not Found'}