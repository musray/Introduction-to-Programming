# -*- coding: utf-8 -*-

import urllib, os, jinja2, webapp2
from urlparse import urlparse

from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'html_templates')
jinja_env = jinja2.Environment(
        loader = jinja2.FileSystemLoader(template_dir),
        autoescape = True)

def comment_validate(msg):
    if len(msg) > 3:
        return True
    else:
        return False

def comment_key(page_name):
    """Generate a ndb.Key object to store and query the user comment."""
    return ndb.Key('Comment', page_name)

class CommentEntity(ndb.Model):
    """A main model for representing an individual comment entity."""
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **kw):
        t = jinja_env.get_template(template) 

        # user comment in a specific artical page
        page_name = kw.get('page_name')

        # [start comment query]
        comment_query = CommentEntity.query(ancestor = comment_key(page_name)).order(-CommentEntity.date)
        comments = comment_query.fetch(10)
        # [end query]

        return t.render(comments = comments, **kw)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class CommentPoster(webapp2.RequestHandler):
    """This is handler to put a entity to the DataStore.
       Each blog entry has a own DataStore Entity.
       All Entities are set to be the descendent of 'Comment'(the ancestor)."""
    def post(self):
        page_name = self.request.get('page_name')
        comment = CommentEntity(parent=comment_key(page_name))
        user_input = self.request.get('content')
        if comment_validate(user_input):
            comment.content = user_input
        else:
            comment.content = "Input invalid. Please make sure your input is longer than 3 charactors." 
        comment.put()

        url_param = urllib.urlencode({'page_name': page_name})
        self.redirect('/%s?' % page_name + url_param + '#comment_form') 

class MainPage(Handler):
    def get(self):
        self.render('index.html', page_name = 'index')

class Content(Handler):
    def get(self):
        self.render('toc.html', page_name = 'toc')

# Handler for INTRO TO WEB DEVELOPMENT page
class WebDev(Handler):
    def get(self):
        self.render('web-development.html', page_name = 'web-development')


class HtmlNote(Handler):
    def get(self):
        self.render('html-note.html', page_name = 'html-note')

class CssNote(Handler):
    def get(self):
        self.render('css-note.html', page_name = 'css-note')

class VimTip(Handler):
    def get(self):
        self.render('vim-tip.html', page_name = 'vim-tip')

class PythonNote(Handler):
    def get(self):
        self.render('python-note.html', page_name = 'python-note')

class Lesson4(Handler):
    def get(self):
        self.render('lesson-4.html', page_name = 'lesson-4')

class Reserved(Handler):
    def get(self):
        self.render('reserved.html', page_name = 'reserved-page')
