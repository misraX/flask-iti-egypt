import uuid

from flask import Flask

from views.webiste_view import website_blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = uuid.uuid4().hex
app.config['PORT'] = 9080


def main() -> Flask:
    app.register_blueprint(
        website_blueprint
    )
    return app

if __name__ == "__main__":
    main().run(debug=True, port=9080)
