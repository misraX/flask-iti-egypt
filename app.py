import logging
import uuid

from flask import Flask
from pydantic import ValidationError

from views.api.user import user_blueprint
from views.website_view import website_blueprint

logger = logging.getLogger(__file__)

app = Flask(__name__)

app.config['SECRET_KEY'] = uuid.uuid4().hex
app.config['PORT'] = 9080

@user_blueprint.app_errorhandler(ValidationError)
def handle_validation_error(error):
    """
    Global Error handler for user blueprint
    :param error: str(validation error)
    :return: json
    """
    return {"error": str(error)}, 400

def main() -> Flask:
    app.register_blueprint(
        website_blueprint
    )
    app.register_blueprint(
        user_blueprint
    )


    return app

if __name__ == "__main__":
    main().run(debug=True, port=9080)
