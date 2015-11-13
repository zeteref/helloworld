import webapp2

import praw
import pyquery

import imp
import os.path
import inspect

#from google.appengine.tools.devappserver2.python import sandbox
#sandbox._WHITE_LIST_C_MODULES += ['_ssl', '_socket']
#real_os_src_path = os.path.realpath(inspect.getsourcefile(os))
#psocket = os.path.join(os.path.dirname(real_os_src_path), 'socket.py')
#imp.load_source('socket', psocket)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class Test(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('test')

        r = praw.Reddit(user_agent='my cool app')
        submissions = r.get_subreddit('opensource').get_hot(limit=5)
        self.response.write('\n'.join([str(x) for x in submissions]))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/test', Test)
], debug=True)

