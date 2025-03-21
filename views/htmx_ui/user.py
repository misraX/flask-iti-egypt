from flask import Blueprint, render_template

from forms.user_form import UserForm
from schemas.request.user import UserRequestSchema  # noqa
from services.user_service import UserService  # noqa

htmx_ui_user_blueprint = Blueprint('admin', __name__, url_prefix='/admin/user')


@htmx_ui_user_blueprint.route('/', methods=['GET'])
def user_list():
    """
    Context aware views

    Render Template with user list as template context.

    Template context is a resolution of UserService().get_users()

    :return: html template
    """
    users = UserService().get_users()
    user_form = UserForm()
    return render_template(
        "htmx_templates/user_list.html",
        users=users,
        user_form=user_form
    )


@htmx_ui_user_blueprint.route('/', methods=['POST'])
def create_user():
    user_service = UserService()
    user_form = UserForm()
    user_service.create_user(
        UserRequestSchema(
            first_name=user_form.first_name.data,
            last_name=user_form.last_name.data,
            email=user_form.email.data,
            country=user_form.country.data,
        ),
    )
    return render_template(
        "htmx_templates/partial/user_list_table.html",
        users=UserService().get_users()
    )


@htmx_ui_user_blueprint.route('/<user_id>/', methods=['DELETE'])
def delete_user(user_id):
    user_service = UserService()
    user_service.delete_user(user_id)
    return render_template("htmx_templates/partial/user_list_table.html", users=UserService().get_users())
