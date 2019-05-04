from google.appengine.ext import ndb
import webapp2
import logging
import template
import function
from twitter import Twitter
from userinfo import UserInfo
from myuser import MyUser


class Profile(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = function.userKey()

        query = Twitter.query()
        tweets = query.fetch()

        query1 = UserInfo.query()
        userinfo = query1.fetch()
        
        if function.userLoggedIn():
            if my_user is None or my_user == '':
                if not function.userExist():
                    function.newUser(function.currentUser())

                template.register(self, function.logoutUrl(self), my_user)
            else:
                if not function.userExist():
                    function.newUser(function.currentUser())

                template.profile(self, function.logoutUrl(self), my_user, tweets, userinfo)
            
        else:
            template.login(self, function.loginUrl(self))

