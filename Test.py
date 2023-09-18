import uiautomator2 as u2
import time

d = u2.connect()

ele = d(textContains="Manager")
if ele.exists:
    element.swipe("left")
    print('123')
