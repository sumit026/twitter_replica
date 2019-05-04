from google.appengine.ext import ndb
import webapp2
import logging
import template
import function
from twitter import Twitter
from userinfo import UserInfo
from register import Register
from myuser import MyUser
from edit import Edit
from add import Add
from edittweet import EditTweet
from search import Search
from user import User
from follow import Follow
from profile import Profile
from uploadhandler import UploadHandler


class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = function.userKey()
        
        query = UserInfo.query()
        data = query.fetch()

        query1 = Twitter.query().order(-Twitter.tweet_date)
        tweets = query1.fetch()
        user = function.currentUser()
        
        if function.userLoggedIn():
            if my_user is None or my_user == '':
                if not function.userExist():
                    function.newUser(function.currentUser())

                template.register(self, function.logoutUrl(self), my_user)
            else:
                if not function.userExist():
                    function.newUser(function.currentUser())

                template.main(self, function.logoutUrl(self), my_user, user, data, tweets)
            

        else:
            template.login(self, function.loginUrl(self))



app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
        ('/register', Register),
        ('/edit', Edit),
        ('/add', Add),
        ('/edittweet', EditTweet),
        ('/search', Search),
        ('/user', User),
        ('/follow', Follow),
        ('/profile', Profile),
        ('/uploadhandler', UploadHandler),
    ], debug=True)
