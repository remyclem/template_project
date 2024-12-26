# codding: utf-8
"""
Template for datetime management.
"""
import datetime


if __name__ == "__main__":

    my_date = datetime.datetime(1991, 12, 25, 2, 31, 58, 999)
    my_other_date = datetime.datetime.strptime("20200301_1255", "%Y%m%d_%H%M")
    today = datetime.datetime.now()
    tomorrow = today + datetime.timedelta(days=1)
    print(my_date)
    print(my_other_date)
    print(today)
    print(tomorrow)
    print("today as string:", today.strftime("%Y%m%d_%H%M"))