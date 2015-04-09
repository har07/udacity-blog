import re

USER_RE = re.compile('^[a-zA-Z0-9_-]{3,20}$')
PASS_RE = re.compile('^.{3,20}$')
EMAIL_RE = re.compile('^[\S]+@[\S]+\.[\S]+$')

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

def valid_month(month):
    if month:
        shortMonths = dict([(m[:3].lower(),m) for m in months])
        shortMonth = month[:3].lower()
        if shortMonth in shortMonths :
            return shortMonths[shortMonth]

    return None

def valid_day(day):
     if day and day.isdigit():
          day_int = int(day)
          if day_int >= 1 and day_int <= 31:
               return day_int
     return None

def valid_year(year):
     if year and year.isdigit():
          year_int = int(year)
          if year_int >= 1900 and year_int <= 2020:
               return year_int
     return None

def valid_username(name):
    match = USER_RE.match(name)
    is_valid = True
    validation_msg = ''
    if not match:
        validation_msg = "That's not a valid username."
        is_valid = False
    return is_valid, validation_msg


def valid_password(passw):
    match = PASS_RE.match(passw)
    is_valid = True
    validation_msg = ''
    if not match:
        validation_msg = "That wasn't a valid password."
        is_valid = False
    return is_valid, validation_msg

def valid_password_verification(passw1, passw2):
    is_valid = passw1 == passw2
    validation_msg = ''
    if not is_valid:
        validation_msg = "Your passwords didn't match."
    return is_valid, validation_msg

def valid_email(email):
    is_valid = True
    validation_msg = ''
    if email != '' and not EMAIL_RE.match(email):
        validation_msg = "That's not a valid email."
        is_valid = False
    return is_valid, validation_msg
