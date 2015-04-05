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
            self.redirect("/thanks")


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks! That's a totally valid date!")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
    , ('/thanks', ThanksHandler)
], debug=True)
