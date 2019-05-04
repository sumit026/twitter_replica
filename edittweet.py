from google.appengine.ext import ndb
import webapp2
import logging
import template
import function
from twitter import Twitter
from myuser import MyUser
from userinfo import UserInfo
from datetime import datetime

class EditTweet(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = function.userKey()
        query = Twitter.query()
        data = query.fetch()
        value = self.request.get('value')
        
        if function.userLoggedIn():
            if my_user is None or my_user == '':
                if not function.userExist():
                    function.newUser(function.currentUser())

                template.register(self, function.logoutUrl(self), my_user)
            else:
                if not function.userExist():
                    function.newUser(function.currentUser())

                template.edittweet(self, function.logoutUrl(self), my_user, data, value) 

        else:
            template.login(self, function.loginUrl(self))
            
    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')
        
        if action == 'Update':
            my_user = function.userKey()
            username = self.request.get('username')
            content = self.request.get('content')
            tags = self.request.get('tags')

            if content is not None or content != '':
                twitter_id = content
                twitter_key = ndb.Key(Twitter, twitter_id)
                tweets = twitter_key.get()
                my_user = function.userKey()

                new_data = Twitter(id=twitter_id, username=username, content=content, tags=tags, user_id=my_user.key.id())
                new_data.put()

                my_user.tweets.append(twitter_key)
                my_user.put()
                
                self.redirect('/')

        elif action == 'Cancel':
            self.redirect('/')
