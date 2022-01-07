from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from application import Base
"""
This is the Item Model that will be created in the DB. It contains:
- item_id (int): Auto-generated ID. It is used as a primary key
- name (str): The name of the item
- description (str): The description of the item
- created_at (datetime): The creation date of the item
"""
class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.created_at = datetime.utcnow()