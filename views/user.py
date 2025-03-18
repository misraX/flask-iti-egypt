from flask import Blueprint, request

from db.db_session import get_session
from models.user import User
from schemas.user import UserSchema
from services import UserService

user_blueprint = Blueprint('user', __name__, url_prefix='/user')


@user_blueprint.route('/', methods=['GET'])
def user_list():
    """
    Get a list of users
    :return: list
    """
    service = UserService()
    return service.get_users()


@user_blueprint.route('/', methods=['POST'])
def create_user():
    """
    Create a new user

    :return: json
    """
    user = User()
    last_name = request.form['last_name']
    first_name = request.form['first_name']
    user.first_name = last_name
    user.last_name = first_name
    with get_session() as session:
        session.add(user)
        session.commit()
    return UserSchema(first_name=first_name, last_name=last_name).model_dump()


@user_blueprint.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    """
    Delete user

    :return: json
    """
    service = UserService()
    service.delete_user(user_id)
    return "", 204


@user_blueprint.route('/<user_id>', methods=['PUT'])
def update_user(user_id: int):
    """
    Update user

    :return: json
    """
    last_name = request.form['last_name']
    first_name = request.form['first_name']
    user_schema = UserSchema(
        first_name=first_name,
        last_name=last_name,
    )
    service = UserService()
    return service.update_user(user_id, user_schema)
