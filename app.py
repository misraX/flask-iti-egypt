import uuid

from flask import Flask, render_template

from forms.contact_form import ContactForm

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
app = Flask(__name__)

app.config['SECRET_KEY'] = uuid.uuid4().hex
app.config['PORT'] = 9080


@app.route('/')
def app_route_index():
    return render_template('index.html')


@app.route('/about')
def hello():
    return render_template('about.html')


@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        return render_template('contact-success.html', contact_form=contact_form)
    return render_template('contact.html', contact_form=contact_form)


if __name__ == "__main__":
    app.run(debug=True, port=9080)
