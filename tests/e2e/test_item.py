import os
from pathlib import Path

def test_add_and_delete_item(client, items):
    """Check if adding/deleting an item is successful. Additionally, check expected failures"""
    item_id = len(items) + 1

    # Add Invalid Items
    response = client.post(f'/v1/item')
    assert response.status_code == 400

    response = client.post(f'/v1/item', json={"random": "asdf"})
    assert response.status_code == 400

    response = client.post(f'/v1/item', json={"name": 1234})
    assert response.status_code == 400

    # Add Item
    response = client.post(f'/v1/item', json={"name": "asdf", "description": "qwer"})
    assert response.status_code == 201

    # Delete Item
    response = client.delete(f'/v1/item/{item_id}')
    assert response.status_code == 200

    # Re-delete Item
    response = client.delete(f'/v1/item/{item_id}')
    assert response.status_code == 404

    # Invalid Item ID
    response = client.delete(f'/v1/item/asdf')
    assert response.status_code == 400

    # Non-existent Item ID
    response = client.delete(f'/v1/item/100')
    assert response.status_code == 404

def test_update_item(client, items):
    """Check if an item is updated successfully"""

    # Update Item
    response = client.put(f'/v1/item/1', json={"name": "asdf", "description": "qwer"})
    assert response.status_code == 200

    response = client.put(f'/v1/item/1', json={"name": "qwer"})
    assert response.status_code == 200

    # Update with None/invalid JSONs
    response = client.put(f'/v1/item/1')
    assert response.status_code == 400

    response = client.put(f'/v1/item/1', json={"random": "asdf"})
    assert response.status_code == 400

    response = client.put(f'/v1/item/1', json={"name": 1234})
    assert response.status_code == 400

    # Invalid Item ID
    response = client.put(f'/v1/item/asdf', json={"name": "qwer"})
    assert response.status_code == 400

    # Non-existent Item ID
    response = client.put(f'/v1/item/100', json={"name": "qwer"})
    assert response.status_code == 404

def test_get_list_of_items(client, items):
    """Check if list of items retrieved is successful"""
    response = client.get(f'/v1/item')

    assert response.status_code == 200
    assert len(response.json['items']) == len(items)

def test_export(client, items):
    """Check if the export is successful"""
    response = client.get(f'/v1/item/csv')
    message = response.json['message'].split()
    count = int(message[2])
    filename = Path(message[-1])

    assert response.status_code == 201
    assert count == len(items)
    assert filename.is_file()

    # Clean Up
    os.remove(filename)