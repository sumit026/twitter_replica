from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import logging
import template
import function
from twitter import Twitter
from myuser import MyUser
from google.appengine.ext import blobstore
from uploadhandler import UploadHandler


class Add(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = function.userKey()
        query = Twitter.query()
        data = query.fetch()
        upload_url= blobstore.create_upload_url('/uploadhandler')
        if function.userLoggedIn():
            if my_user is None or my_user == '':
                if not function.userExist():
                    function.newUser(function.currentUser())

                template.register(self, function.logoutUrl(self), my_user)
            else:
                if not function.userExist():
                    function.newUser(function.currentUser())

                template.add(self, function.logoutUrl(self), my_user, data, upload_url)
        else:
            template.login(self, function.loginUrl(self))

    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')
        
        if action == 'Delete':
            my_user = function.userKey()
            twitter_id = self.request.get('twitter_id')
            twitter_key = ndb.Key(Twitter, twitter_id)
            if twitter_key in my_user.tweets:
                my_user.tweets.remove(twitter_key)
                my_user.put()
                ndb.Key(Twitter, twitter_id).delete()
                self.redirect('/')
                
            
            
