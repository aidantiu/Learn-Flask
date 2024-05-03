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
    ```python
        from flask_sqlalchemy import SQLAlchemy
        from flask_migrate import Migrate

        db = SQLAlchemy(app)
        migrate = Migrate(app, db)

        from app import routes, models
    ```
- Database Models: Collection of classes
- ORM (Object Relation Mapper) Convert python code into rows of databases
- Create Database Model in app/models.py
    ```python
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
    ```python
        posts: so.WriteOnlyMapped['Post'] = so.relationship(
        back_populates='author')
    ```
- ### Playing wth the Database
- Adding a `User` to the database with User() model class
    - Adding instance to the and committing changes to database session

- Querying Users
    - query = sa.select(User): Selects Model User from Database
    - users = db.session.scalars(query).all(): Executes the database query that returns a result iterator
    - Looping through Queried users using fo rloop
    - Querying a User by id with by db.session.get(User, 1)

- Adding a `Post` to the database
    - Retrieve a user from the database, and creating post via Post() model class, with author = u

- Querying a Post
    - u = db.session.get(User, 1): Select a User (u) to be identified as author for finding user's posts
    - query = u.posts.select(): Select posts made by u (SQL SELECT)
    - query = sa.select(Post): Select post author and body for all posts
    - query = sa.select(User).order_by(User.username.desc()): Select users by descending order
    - query = sa.select(User).where(User.username.like('s%')): Select users that starts with 's'

- Automating Python Shell to Play with Flask DB
    ```python
    # Add this line into microblog.py
    @app.shell_context_processor
    def make_shell_context():
        return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}
    ```

- So you can work with database entities without having to import them:
    ```shell
    (venv) $ flask shell
    >>> db
    <SQLAlchemy sqlite:////home/miguel/microblog/app.db>
    >>> User
    <class 'app.models.User'>
    >>> Post
    <class 'app.models.Post'>
    ```

