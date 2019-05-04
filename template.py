import jinja2
import os
import function

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def login(self, url):
    template_values = {'url': url}

    template = JINJA_ENVIRONMENT.get_template('login.html')
    self.response.write(template.render(template_values))


def main(self, url, my_user, user, data, tweets):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'user': user,
        'data': data,
        'tweets': tweets,
    }

    template = JINJA_ENVIRONMENT.get_template('main.html')
    self.response.write(template.render(template_values))

def register(self, url, my_user):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
    }

    template = JINJA_ENVIRONMENT.get_template('register.html')
    self.response.write(template.render(template_values))

def edit(self, url, my_user, data):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'data': data,
    }

    template = JINJA_ENVIRONMENT.get_template('editinfo.html')
    self.response.write(template.render(template_values))

def add(self, url, my_user, data, upload_url):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'tweets': data,
        'upload_url': upload_url,
    }

    template = JINJA_ENVIRONMENT.get_template('add-tweet.html')
    self.response.write(template.render(template_values))

def edittweet(self, url, my_user, data, value):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'data': data,
        'value': value,
    }

    template = JINJA_ENVIRONMENT.get_template('edittweet.html')
    self.response.write(template.render(template_values))


def searchtext(self, url, my_user, data, data1, value):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'tweets': data,
        'userinfo': data1,
        'value': value,
    }

    template = JINJA_ENVIRONMENT.get_template('search.html')
    self.response.write(template.render(template_values))

def user(self, url, my_user, data, data1, value):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'tweets': data,
        'userinfo': data1,
        'value': value,
    }

    template = JINJA_ENVIRONMENT.get_template('usersearch.html')
    self.response.write(template.render(template_values))

def profile(self, url, my_user, tweets, userinfo):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'tweets': tweets,
        'userinfo': userinfo,
    }

    template = JINJA_ENVIRONMENT.get_template('profile.html')
    self.response.write(template.render(template_values))

