from datetime import *

today = date.today()

number_of_days_passed = today.timetuple().tm_yday
print(number_of_days_passed)

beginning_of_year = date(today.year, 1, 1)
print(beginning_of_year)

end_of_year = date(today.year, 12, 31)
print(end_of_year)

num_of_days_in_year = (end_of_year - beginning_of_year).days
print(num_of_days_in_year + 1)

year_progress = number_of_days_passed / (num_of_days_in_year + 1) * 100
print("Time passed since the beginning of the year is: ", round(year_progress, 2))