from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app import db

class User(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: orm.Mapped[str] = orm.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: orm.Mapped[Optional[str]] = orm.mapped_column(sa.String(256))

    # One-to-Many Relationship
    posts: orm.WriteOnlyMapped['Post'] = orm.relationship(
        back_populates='author')

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    body: orm.Mapped[str] = orm.mapped_column(sa.String(140))
    timestamp: orm.Mapped[datetime] = orm.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))

    # Foreign Key Relationship
    user_id: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey(User.id),
                                               index=True)

    # Many-to-One Relationship
    author: orm.Mapped[User] = orm.relationship(back_populates='posts')

    def __repr__(self):
        return f'<Post {self.body}>'
