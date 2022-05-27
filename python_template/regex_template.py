# codding: utf-8
"""
How to use regex in python.
"""
import re


def test_regex(candidate_string):
    # ^: starts with
    # [0-9]: any digit between 0 and 9
    # [0-9]{8}: 8 consecutive digits between 0 and 9
    # $: ends with
    regex = r"^[0-9]{8}_[0-9]{2}h[0-9]{2}$"
    if re.match(regex, candidate_string):
        print("It matches!")
    else:
        print("It doesn't match")


candidate_string = "20220107_12h58"
match_regex = test_regex(candidate_string)

