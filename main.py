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
import validations
import tools
from rot13 import Rot13
import main_templating

form = """
<form method="post">
    What is your birthday?
    <br>
    <label> Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label> Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label> Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

form_rot13 = """
<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">{0}</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""

class MainHandler(webapp2.RequestHandler):

    def write_form(self, error="", month="", day="", year=""):
        params = {"error" : error,
                  "month" : tools.escape_html(month),
                  "day" : tools.escape_html(day),
                  "year" : tools.escape_html(year)}
        self.response.write(form % params)

    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()

    def post(self):
        month = self.request.get('month')
        day = self.request.get('day')
        year = self.request.get('year')
        is_valid_month = validations.valid_month(month)
        is_valid_day = validations.valid_day(day)
        is_valid_year = validations.valid_year(year)
        if not(is_valid_month and is_valid_day and is_valid_year) :
            # self.response.write(form)
            message = "That doesn't look valid to me, friend."
            self.write_form(message, month, day, year)
        else:
            self.redirect("/thanks?source=date")


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        source = self.request.get("source")
        self.response.write("Thanks! That's a totally valid %s!" % source)

class Rot13Handler(webapp2.RequestHandler):
    def write_form(self, text=""):
        text = tools.escape_html(text)
        self.response.write(form_rot13.format(text))

    def get(self):
        self.write_form()

    def post(self):
        plain = self.request.get("text")
        #convert string from unicode to normal string:
        plain = str(plain)
        encryptor = Rot13()
        encrypted = encryptor.encrypt(plain)
        self.write_form(encrypted)

class SignupHandler(main_templating.Handler):
    def get(self):
        self.render("signup.html", data={})

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        is_valid_username, username_msg = validations.valid_username(username)
        is_valid_password, password_msg = validations.valid_password(password)
        is_valid_verification, verify_msg = validations.valid_password_verification(password, verify)
        is_valid_email, email_msg = validations.valid_email(email)

        if is_valid_username and is_valid_password and is_valid_verification and is_valid_email:
            self.redirect('/thanks?data')
        else:
            data = {'username': username,
                    'email': email,
                    'username_msg': username_msg,
                    'password_msg': password_msg,
                    'email_msg': email_msg}
            if is_valid_password:
                data['verify_msg'] = verify_msg
            self.render("signup.html", data=data)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
    , ('/thanks', ThanksHandler)
    , ('/unit2/rot13', Rot13Handler)
    , ('/unit2/signup', SignupHandler)
], debug=True)
