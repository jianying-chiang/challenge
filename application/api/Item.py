from flask import current_app as app, jsonify, request
from application import Session
from application.api import item_service
from application.service.ItemService import ItemDoesNotExistException

@app.route("/v1/item", methods=['POST'])
def add_item():
    item_data = request.json

    # check if JSON format is correct
    if item_data is None or 'name' not in item_data or type(item_data['name']) != str or ('description' in item_data and type(item_data['description']) != str):
        return jsonify({'message': 'A JSON is required for adding. It must contain item name and optionally a description. Both need to be valid string values.'}), 400
    
    session = Session()
    try:
        item_id = item_service.add_item(session=session, item=item_data)
        session.commit()
        return jsonify({'message': 'Item with ID {} was created'.format(item_id)}), 201
    except:
        session.rollback()
        return jsonify({'message': 'Something went wrong'}), 500
    finally:
        session.close()

@app.route("/v1/item/<item_id>", methods=['PUT'])
def update_item(item_id):
    # check if item_id type is correct
    if item_id is None or not str.isdigit(item_id):
        return jsonify({'message': 'A valid item ID integer is required for updating'}), 400
    item_data = request.json

    # check if JSON format is correct
    if item_data is None or ('name' not in item_data and 'description' not in item_data) or ('description' in item_data and type(item_data['description']) != str) or ('name' in item_data and type(item_data['name']) != str):
        return jsonify({'message': 'A JSON is required for updating. It must contain name or description, and need to be valid string values.'}), 400

    session = Session()
    try:
        item_service.update_item(session=session, item_id=item_id, item=item_data)
        session.commit()
        return jsonify({'message': "Item {} updated successfully".format(item_id)}), 200
    except ItemDoesNotExistException:
        session.rollback()
        return jsonify({'message': 'Item does not exists, therefore it cannot be updated'}), 404
    except:
        session.rollback()
        return jsonify({'message': 'Something went wrong'}), 500
    finally:
        session.close()

@app.route("/v1/item/<item_id>", methods=['DELETE'])
def delete_item(item_id):
    # check if item_id type is correct
    if item_id is None or not str.isdigit(item_id):
        return jsonify({'message': 'A valid item ID integer is required for deleting'}), 400

    session = Session()
    try:
        item_service.delete_item(session=session, item_id=item_id)
        session.commit()
        return jsonify({'message': "Item {} deleted successfully".format(item_id)}), 200
    except ItemDoesNotExistException:
        session.rollback()
        return jsonify({'message': 'Item does not exists, therefore it cannot be deleted'}), 404
    except:
        session.rollback()
        return jsonify({'message': 'Something went wrong'}), 500
    finally:
        session.close()

@app.route("/v1/item", methods=['GET'])
def get_list_of_items():
    session = Session()
    items = item_service.get_item_list(session=session)
    return jsonify({'items': items}), 200

@app.route("/v1/item/csv", methods=['GET'])
def export():
    session = Session()
    message = item_service.export_to_csv(session=session)
    return jsonify({'message': message}), 201