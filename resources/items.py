from flask import jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db.items_db import ItemDatabase
from schemas import ItemSchema, GetItemSchema,RequiredIdSchema ,OptionalGetSchema, MessageSchema, PostItemSchema
from flask_jwt_extended import jwt_required

blp = Blueprint('items', __name__, description = "Operations on items")

@blp.route("/items")
class Items(MethodView):
    
    def __init__(self):
        self.db = ItemDatabase()

    @jwt_required()
    @blp.response(200, GetItemSchema(many = True))
    @blp.arguments(OptionalGetSchema, location='query')
    def get(self, args):
        id = args.get('id')
        if id is None:
            return jsonify(self.db.get_items()), 200
        item = self.db.get_item(id)
        if item is None:
            abort(404, message="Item doesn't exist")
        return jsonify(item), 200
            
    @jwt_required()
    @blp.response(201, MessageSchema)
    @blp.arguments(PostItemSchema)
    def post(self, data):
        self.db.add_item(data)
        return jsonify({"message":"Inserted Successfully..."}), 200

    @jwt_required()
    @blp.response(200, MessageSchema)
    @blp.arguments(RequiredIdSchema, location = 'query')
    @blp.arguments(ItemSchema)
    def put(self, args, data):
        id = args.get('id')
        present = self.db.get_item(id)
        if not present:
            abort(404, message="Item doesn't exist")        
        else:
            self.db.put_item(id,data)
            return {"message": "Item Updated"}, 200
    
    @jwt_required()
    @blp.response(200, MessageSchema)
    @blp.arguments(RequiredIdSchema, location = 'query')
    def delete(self, id):
        id = id.get('id')
        present = self.db.get_item(id)
        if present is None:
            abort(404, message="Item doesn't exist")        
        else:
            self.db.del_item(id)
            return {"message":"Deleted successfully.."}, 200