#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
from caesar import encrypt

rot_form = """
<form action="/" method="post">
    <label>
        rotate by
        <input type="number" name="rotation" value="0"/>
        <br>
        <textarea input type="text" name="text" style="height: 100px; width: 400px;">{0}</textarea>
        <br>
    </label>
    <input type="submit" value="Submit"/>
</form>
"""

class MainHandler(webapp2.RequestHandler):

    def get(self):
        clean_text = rot_form.format("")
        self.response.out.write(clean_text)
        #response = page_header + rot_form %{"answer": answer} + page_footer
        #self.response.write(response)
        #self.response.out.write(rot_form %{'answer': answer})
#class Rotate(webapp2.RequestHandler):
    #""" Rotates text based on user input
    #"""
    def post(self):
        answer = ''
        rot = self.request.get('rotation')

        user_text = self.request.get('text')

        answer = encrypt(user_text, int(rot))
        self.response.out.write(rot_form.format(answer))
        #response = page_header + "<p>" + answer + "</p>" + page_footer
        #self.response.out.write(rot_form %{"answer": answer})
        #self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
