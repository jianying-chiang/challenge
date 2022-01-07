from application.dao.ItemDAO import SQLAlchemyItemDAO
from application.service.ItemService import ItemService

# Initialize DAOs
item_dao = SQLAlchemyItemDAO()

# Create Service Singletons
item_service = ItemService(item_dao=item_dao)