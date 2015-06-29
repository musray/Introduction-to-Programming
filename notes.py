import webapp2
import cgi
from handlers import *

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/toc', Content),
    ('/web-development', WebDev),
    ('/html-note', HtmlNote),
    ('/css-note', CssNote),
    ('/vim-tip', VimTip),
    ('/python-note', PythonNote),
    ('/lesson-4', Lesson4),
    ('/reserved', Reserved),
    ('/comment', CommentPoster),
], debug=True)
