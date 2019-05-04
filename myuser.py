from google.appengine.ext import ndb
from twitter import Twitter


class MyUser(ndb.Model):
    tweets = ndb.KeyProperty(kind=Twitter, repeated=True)
    username = ndb.StringProperty()
    following = ndb.StringProperty(repeated=True)
