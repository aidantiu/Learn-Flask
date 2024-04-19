'''IMPORTANT'''

# Declaring css
1. create static folder with css folder: style.css
<!-- https://www.quora.com/How-do-you-add-CSS-to-Flask -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}"> 

2. Looping through flash() messages 
{% with messages = get_flashed_messages() %}
{% if messages %}
<ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}
{% endwith %}

# ''' Summarizations '''
## Chapter 1: SETUP and HELLO WORLD
- Setup venv
- __name__ 
- importing app and Circular imports 
- decorators 
- view functions
- routes
- export and running flask (manual)
- run flask with .flaskenv (automatic)

## Chapter 2: TEMPLATES
- Using HTML Jinja
- mock object
- render_template()
- Template inheritance

## Chapter 3: Web Forms
- Flask-wtf setup
- configs (for csrf attacks)
- FlaskForms (StringField, PasswordField, BooleanField, SubmitField)
- form actions, methods (get, post)
- flash()