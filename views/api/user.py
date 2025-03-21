from flask import Blueprint, request

from schemas.request.user import UserRequestSchema
from services.user_service import UserService

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
    service = UserService()
    user_request_schema = UserRequestSchema(
        last_name=request.json['last_name'],
        first_name=request.json['first_name'],
    )
    return service.create_user(user_request_schema)


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
    user_schema = UserRequestSchema(
        first_name=request.json['first_name'],
        last_name=request.json['last_name'],
    )
    service = UserService()
    return service.update_user(user_id, user_schema)
