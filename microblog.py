import sqlalchemy as sa
import sqlalchemy.orm as orm
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'orm': orm, 'db': db, 'User': User, 'Post': Post}