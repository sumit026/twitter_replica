from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api.images import get_serving_url
from google.appengine.ext import blobstore
import webapp2
import logging
import template
import function
from twitter import Twitter
from myuser import MyUser


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')

        if action == 'Add':            
            my_user = function.userKey()
            username = self.request.get('username')
            content = self.request.get('content')
            tags = self.request.get('tags')
            uploaded_file = self.request.POST.get("file")
            tweets = Twitter()
            if content is not None or content != '':
                twitter_id = content
                twitter_key = ndb.Key(Twitter, twitter_id)
                get_tweets = twitter_key.get()
                tweets.id = content
                tweets.key = twitter_key
                tweets.username = username
                tweets.content = content
                tweets.tags = tags
                tweets.user_id = my_user.key.id()
                if len(self.get_uploads()) > 0:
                    upload = self.get_uploads()[0]
                    blobinfo = blobstore.BlobInfo(upload.key())
                    filename = blobinfo.filename
                    tweets.picture_name = filename
                    tweets.picture_blob = upload.key()
                    tweets.picture_url = get_serving_url(upload.key())

                tweets.put()

                my_user.tweets.append(twitter_key)
                my_user.put()
                    
                self.redirect('/')            
