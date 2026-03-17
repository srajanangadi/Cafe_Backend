from flask import jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db.users_db import UserDatabase
from schemas import UserSchema, OptionalGetSchema, MessageSchema, UserPostSchema, RequiredIdSchema
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from blocklist import BLOCKLIST

blp = Blueprint('users', __name__, description = "Operations on users")

@blp.route("/login")
class Login(MethodView):
    def __init__(self):
        self.db = UserDatabase()

    @blp.arguments(UserPostSchema)
    def post(self, data):
        user_id = self.db.verify_user(data)
        if user_id:
            return {"access_token":create_access_token(identity=str(user_id))}
        abort(400, "Username or Password Incorrect")


@blp.route("/logout")
class Logout(MethodView):

    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message":"Successfully Logged Out"}

@blp.route("/user")
class Users(MethodView):
    
    def __init__(self):
        self.db = UserDatabase()

    @blp.response(200, UserSchema)
    @blp.arguments(RequiredIdSchema, location='query')
    def get(self, id):
        id = id.get('id')
        user = self.db.get_user(id)
        if user is None:
            abort(404, message="User doesn't exist")
        return jsonify(user), 200
    
    @blp.response(201, MessageSchema)
    @blp.arguments(UserPostSchema)
    def post(self, data):
        if not self.db.add_user(data):
            abort(409, message= "Sorry, username Already Exist...")
        return jsonify({"message":"Inserted Successfully..."}), 201
    
    @blp.response(200, MessageSchema)
    @blp.arguments(RequiredIdSchema, location = 'query')
    def delete(self, id):
        id = id.get('id')
        if self.db.del_user(id):
            return {"message":"Deleted successfully.."}, 200
        abort(404, message="User doesn't exist")