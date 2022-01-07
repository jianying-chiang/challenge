import csv
from datetime import datetime
from pathlib import Path
from typing import List

from application.model.ItemModel import Item

def serialize_item(item: Item) -> dict:
    """Serializes an item

    Args:
        item (Item): The item to serialize

    Returns:
        Dict [String: Any]: The item object serialized
    """

    return {
        "item_id": item.item_id,
        "name": item.name,
        "description": item.description,
        "created_at": item.created_at.isoformat()
    }

def export(items: List[Item]) -> str:
    """Exports all existing items to a local CSV file

    Args:
        items (List[Item]): List of items for export
    Returns:
        filename (str): Filename of CSV file
    Raises:
        Exception: An exception when writing to csv
    """
    filename = 'items_{}.csv'.format(datetime.now().strftime("%Y_%m_%d_%H-%M-%S"))
    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for item in items:
                writer.writerow([item.item_id, item.name, item.description, item.created_at])
    except Exception as e:
        print('Exception: ', filename)
        raise e
        
    return Path(filename).absolute()