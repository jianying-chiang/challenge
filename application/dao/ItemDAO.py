import abc
from application.model.ItemModel import Item
from typing import List

class ItemDAO(abc.ABC):
    """A abstract version of data-access-object to handle all DB-related operations for the Item object.
    """
    # Note: Session is left purposely untyped to allow for different implementations

    @abc.abstractmethod
    def add(self, session, item: Item) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_by_id(self, session, item_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def update_by_id(self, session, item_id: int, item: Item) -> None:
        raise NotImplementedError
 
    @abc.abstractmethod
    def get_all(self, session) -> List[Item]:
        raise NotImplementedError

class SQLAlchemyItemDAO(ItemDAO):
    """Implementation of the ItemDAO
    """
    def add(self, session, item: Item) -> Item:
        """Adds item to db

        Session is flushed afterwards to update item_id

        Args:
            session: SQLAlchemy session
            item: Item to be added 
        Returns:
            The added Item
        """
        session.add(item)
        session.flush()
        session.refresh(item)
        return item


    def delete_by_id(self, session, item_id: int) -> None:
        """Deletes item from db

        Args:
            session: SQLAlchemy session
            item_id: id of item to be delete 
        Returns:
            Returns number of affected rows
        """
        rows = session.query(Item).filter_by(item_id=item_id).delete()
        return rows


    def update_by_id(self, session, item_id: int, item: dict) -> None:
        """Updates description value for item with specified item_id 

        Args:
            session: SQLAlchemy session
            item_id: The item's item_id
            item: Updated item values
        Returns:
            Returns number of affected rows
        """
        rows = session.query(Item).filter(Item.item_id == item_id) \
            .update(item)
        return rows

    def get_all(self, session) -> List[Item]:
        """Retrieves all items

        Args:
            session: SQLAlchemy session

        Returns:
            Returns a list of all Items
            Items are returned in descending order by creation date.
        """

        return session.query(Item).order_by(Item.created_at.desc()).all()