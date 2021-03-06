# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Imports
import os
import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('index.html')
    	self.response.out.write(template.render())
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.write('Hello, World2!')


class aboutPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('about.html')
    	self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/about.html', aboutPage)
], debug=True)



