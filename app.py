import logging
import uuid

from flask import Flask

from views.user import user_blueprint
from views.webiste_view import website_blueprint

logger = logging.getLogger(__file__)

app = Flask(__name__)

app.config['SECRET_KEY'] = uuid.uuid4().hex
app.config['PORT'] = 9080



def main() -> Flask:
    app.register_blueprint(
        website_blueprint
    )
    app.register_blueprint(
        user_blueprint
    )

    # with get_session(app.config['SQLALCHEMY_DATABASE_URI']) as session:
    #     statement = select(User).filter_by(first_name="Maysra")
    #     rows = session.execute(statement).all()
    #     for row in rows:
    #         print(row[0].first_name)
    #         print(row[0].last_name)
    #         print(row[0].id)

    return app

if __name__ == "__main__":
    main().run(debug=True, port=9080)
