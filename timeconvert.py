import math
import os
import random
import re
import sys


def timeConversion(s):
    # Write your code here
    times = re.search(r"(?P<hh>..):(?P<mm>..):(?P<ss>..)(?P<ampm>..)", s)
    hour = times.group('hh')
    hr = ''

    if times.group('ampm') == 'PM':
        if hour == '12':
            hr = '12'
        else:
            hr = str(int(hour) + 12)
    else:
        if hour == '12':
            hr = '00'
        else:
            hr = hour

    return hr + ':' + times.group('mm') + ':' + times.group('ss')

print(timeConversion("7:09:15PM"))
