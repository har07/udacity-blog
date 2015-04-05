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