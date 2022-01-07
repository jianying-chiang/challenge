from typing import List
from sqlalchemy.orm.session import Session
from application.dao.ItemDAO import ItemDAO
from application.model.ItemModel import Item
from application.util.utility import serialize_item, export


class ItemDoesNotExistException(Exception):
    """A Exception if an item by id does not exist
    """
    pass

class ItemService(object):
    """A service for all operations on user items.

    Attributes:
        item_dao (ItemDAO)
    """

    def __init__(self,
                 item_dao: ItemDAO):
        """Inits ItemService with an DAO"""
        self.item_dao = item_dao
    
    def add_item(self, session: Session, item: dict) -> int:
        """Add new item

            Args:
                session: SQLAlchemy session
                item: The new item object
            Returns:
                Item ID
        """
        item_to_add = Item(item['name'], item['description'])
        added_item = self.item_dao.add(session, item_to_add)
        return added_item.item_id
    
    def update_item(self, session: Session, item_id: str, item: dict) -> None:
        """Update an item by its ID

            Args:
                session: SQLAlchemy session
                item_id: Item ID
                item: Updated item values
            Raises:
                ItemDoesNotExistException: if no rows are changed, this exception is raised
        """
        rows_affected = self.item_dao.update_by_id(session, int(item_id), item)
        if rows_affected == 0:
            raise ItemDoesNotExistException

    def delete_item(self, session: Session, item_id: str) -> None:
        """Delete an item by its ID

            Args:
                session: SQLAlchemy session
                item_id: Item ID
            Raises:
                ItemDoesNotExistException: if no rows are changed, this exception is raised
        """
        rows_affected = self.item_dao.delete_by_id(session, int(item_id))
        if rows_affected == 0:
            raise ItemDoesNotExistException
    
    def get_item_list(self, session: Session) -> List[Item]:
        """Get list of all items

            Args:
                session: SQLAlchemy session
            Returns:
                List of all items
        """
        items = self.item_dao.get_all(session)
        for i in range(len(items)):
            items[i] = serialize_item(items[i])

        return items
    
    def export_to_csv(self, session: Session) -> str:
        """Exports a list of all items as a CSV file

            Args:
                session: SQLAlchemy session
            Returns:
                Request message
        """
        items = self.item_dao.get_all(session)
        filename = export(items)

        return "Successfully exported {} items to CSV file: {}".format(len(items), filename)