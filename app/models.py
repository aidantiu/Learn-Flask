# Description: This file defines the User class and the relationship between the User and Post tables.

# Import the required modules
from datetime import datetime, timezone

# Import the typing module
from typing import Optional

# Import the SQLAlchemy modules
import sqlalchemy as sa

# Import the SQLAlchemy ORM module
import sqlalchemy.orm as so

# Import the SQLAlchemy base class
from app import db

# Define the User class
class User(db.Model):

    # Define the columns of the User table
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # Define the relationship between the User and Post tables
    posts: so.WriteOnlyMapped['Post'] = so.relationship(
        back_populates='author')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    # Define the relationship between the User and Post tables
    def __repr__(self):
        return '<User {}>'.format(self.username)


# Define the Post class
class Post(db.Model):
    # Define the columns of the Post table
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),
                                               index=True)
    
    # Define the relationship between the Post and User tables
    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)