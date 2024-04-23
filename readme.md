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

## Chapter 4: 
- Database Migrations
    - pip install flask-migrate
- Flask-Alchemy config
    ```python
    import os
    basedir = os.path.abspath(os.path.dirname(__file__))

    class Config:
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    ```
- Represent database in application
    - ```python
        from flask_sqlalchemy import SQLAlchemy
        from flask_migrate import Migrate

        db = SQLAlchemy(app)
        migrate = Migrate(app, db)

        from app import routes, models
    ```
- Database Models: Collection of classes
- ORM (Object Relation Mapper) Convert python code into rows of databases
- Create Database Model in app/models.py
    - ```python
        class User(db.Model):
            id: so.Mapped[int] = so.mapped_column(primary_key=True)
            username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                        unique=True)
            email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                                    unique=True)
            password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

            def __repr__(self):
                return '<User {}>'.format(self.username)
    ```
- __repr__ method tells how to print or represent an object
- Migration Repository: Container of the scripts that tells how to update a database
    - flask db init
    - First Migration: Compares the database's models in the code compared to actual structure of database
        - flask db migrate -m "users table"
        - Generates a unique code for the scripts to be executed
    - upgrade(): Add | flask db upgrade  
    - downgrade(): Delete | flask db delete  
    - Uses snake case for default table names
- Relationships: One to Many: Many to One: Many to Many
- Indicating relationship to a model to another
    - ```python
        posts: so.WriteOnlyMapped['Post'] = so.relationship(
        back_populates='author')
    ```

