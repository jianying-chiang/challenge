import pytest

from application import Session, create_app
from application.model.ItemModel import Item
from typing import List, Dict

# Constants
items_data = [
    { 
      "description": "standard",
      "name": "Paper"
    }, 
    {
      "description": "red", 
      "name": "Pen"
    }
]


@pytest.fixture(scope='session')
def app():
    """Create and configure a new app instance for each test."""
    app = create_app(test=True)
    app.app_context().push()
    return app


@pytest.fixture(scope='session')
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture(scope='function')
def session():
    return Session()

@pytest.fixture(scope='module')
def module_session():
    return Session()


@pytest.fixture(scope='session')
def session_session():
    return Session()

@pytest.fixture(scope='module')
def items(module_session) -> Dict[str, List[Item]]: 
    """Creates items based on the constants above

    Yields:
        items_data: Dict[str, List[Item]]
    """
    # Set Up
    items = []
    for item in items_data:
        itemObject = Item(name=item['name'], description=item['description'])
        items.append(itemObject)
        
    module_session.add_all(items)
    module_session.commit()
    
    yield items

    # Clean Up
    for item in items:
        module_session.delete(item)
    module_session.commit()
