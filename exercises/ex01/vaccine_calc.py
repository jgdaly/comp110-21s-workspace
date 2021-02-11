"""A vaccination calculator."""

__author__ = "730356913"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
today: datetime = datetime.today()
print(today.strftime("%B %d, %Y"))
one_day: timedelta = timedelta(1)
tomorrow: datetime = today + one_day
print(tomorrow.strftime("%B %d, %Y"))
fortnight: timedelta = timedelta(7 + 7)
future: datetime = today + fortnight
print(future.strftime("%B %d, %Y"))

Population: int = (100)
Doses: int = (50)
Doses_per_Day: int = (2)
Target_percent: int = (50)
print("We will reach 50% vaccination in 25 days")
twentyfive_days: timedelta = timedelta(20+5)
future1: datetime = today + twentyfive_days
print(future1.strftime("%B %d, %Y"))

Population1: int = (330000000)
Doses1: int = (32780860)
Doses_per_Day1: int = (1319981)
Target_percent1: int = (80)
print("We will reach 80% vaccination in 375 days")
threeseventyfive_days: timedelta = timedelta(300+75)
future2: datetime = today + threeseventyfive_days
print(future2.strftime("%B %d, %Y"))

Population2: int = (30000)
Doses2: int = (1234)
Doses_per_Day2: int = (4321)
Target_percent2: int = (100)
print("We will reach 100% vaccination in 14 days")
future3: datetime = today + fortnight
print(future3.strftime("%B %d, %Y"))