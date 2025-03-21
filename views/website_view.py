from flask import Blueprint, render_template

from forms.contact_form import ContactForm

website_blueprint = Blueprint('webiste', __name__, template_folder='templates')


@website_blueprint.route('/')
def app_route_index():
    return render_template('index.html')


@website_blueprint.route('/about')
def hello():
    return render_template('about.html')


@website_blueprint.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')


@website_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        return render_template('contact-success.html', contact_form=contact_form)
    return render_template('contact.html', contact_form=contact_form)
