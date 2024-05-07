
# Adding a `User` to the database
```python
# Creating a User instance with username and email
u = User(username="John", email="example@gmail.com")

# Adding the User instance to the database session
db.session.add(u)

# Committing the changes to the database
db.session.commit()
```

# Querying Users
```python
# Querying Users
query = sa.select(User)
users = db.session.scalars(query).all()

print(users)

u = db.session.get(User, 1)
print(u)

```

# Adding a `Post` to the database
```python
# Retrieving a User from the database
u = db.session.get(User, 1)

# Creating a new Post instance with body and author, timestamp has default
p = Post(body='my first post!', author=u)

# Adding the Post instance and committing to database session
db.session.add(p)
db.session.commit()
```

# Querying a Post
```python
# get all posts written by a user
u = db.session.get(User, 1)

# retrieve posts by u (SQL SELECT)
query = u.posts.select()
posts = db.session.scalars(query).all()
print(posts)
# [<Post my first post!>]

# same, but with a user that has no posts
u = db.session.get(User, 2)
u
<User susan>
query = u.posts.select()
posts = db.session.scalars(query).all()
posts
# []

# print post author and body for all posts
query = sa.select(Post)
posts = db.session.scalars(query)
for p in posts:
    print(p.id, p.author.username, p.body)

# 1 john my first post!

# get all users in reverse alphabetical order
query = sa.select(User).order_by(User.username.desc())
db.session.scalars(query).all()
# [<User susan>, <User john>]

# get all users that have usernames starting with "s"
query = sa.select(User).where(User.username.like('s%'))
db.session.scalars(query).all()
# [<User susan>]
```

# Automating Python Shell to Play with Flask DB
```python
# Add this line into microblog.py
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}
```

So you can work with database entities without having to import them:
```shell
(venv) $ flask shell
>>> db
<SQLAlchemy sqlite:////home/miguel/microblog/app.db>
>>> User
<class 'app.models.User'>
>>> Post
<class 'app.models.Post'>
```
