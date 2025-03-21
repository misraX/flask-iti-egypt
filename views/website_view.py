from flask import Blueprint, render_template

from forms.contact_form import ContactForm

website_blueprint = Blueprint('website', __name__, template_folder='templates')


@website_blueprint.route('/')
def app_route_index():
    return render_template('website/index.html')


@website_blueprint.route('/about')
def hello():
    return render_template('website/about.html')


@website_blueprint.route('/testimonial')
def testimonial():
    return render_template('website/testimonial.html')


@website_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        return render_template('website/contact-success.html', contact_form=contact_form)
    return render_template('website/contact.html', contact_form=contact_form)
