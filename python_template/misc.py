# codding: utf-8
"""
A few tiny things that doesn't really deserve a file of their own.
"""


#####################################
# *args and **kwargs
def sum(*args):
    sum = 0
    for elt in args:
        sum += elt
    print("Sum: {}".format(sum))

def exam(**kwargs):
    for key, value in kwargs.items():
        print("Student: {} - Grade: {}".format(key, value))

sum(1, 2, 7)
x = [1, 2, 7, 5]
sum(*x)

listing = dict()
listing["Bob"] = 14
listing["Alice"] = 17
exam(**listing)
#####################################