from google.appengine.ext import ndb


class Twitter(ndb.Model):
    user_id = ndb.StringProperty()
    username = ndb.StringProperty()
    tags = ndb.StringProperty()
    content = ndb.StringProperty()
    tweet_date = ndb.DateTimeProperty(auto_now=True)
    picture_name = ndb.StringProperty()
    picture_blob = ndb.BlobKeyProperty()
    picture_url = ndb.StringProperty()
                   

