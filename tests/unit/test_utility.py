import os
from pathlib import Path
from application.util.utility import export, serialize_item
from application.model.ItemModel import Item

def test_item_serializer():
    """Check if Item object can be converted to Dict"""
    item = Item(name="A", description="B")
    serialized_item = serialize_item(item)

    assert serialized_item['item_id'] == item.item_id
    assert serialized_item['name'] == item.name
    assert serialized_item['description'] == item.description
    assert serialized_item['created_at'] == item.created_at.isoformat()

def test_export():
    """Check if items can be exported to a CSV file"""
    items = [
        Item(name="A", description="B"),
        Item(name="C", description="D"),
    ]
    filename = Path(export(items))
    assert filename.is_file()

    # Clean Up
    os.remove(filename)
    