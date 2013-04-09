# coding: utf-8

db = DAL('sqlite://storage.sqlite')
response.generic_patterns = ['*'] if request.is_local else []
from gluon.tools import Auth, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key())
auth.define_tables()

Post = db.define_table("post",
        Field("message", "text", requires=IS_NOT_EMPTY(), notnull=True),
        auth.signature
    )

Post.is_active.readable = False
Post.is_active.writable = False
