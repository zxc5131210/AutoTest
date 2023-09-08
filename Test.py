'''This is a demo test for gesture automation.'''
import uiautomator2 as u2
import subprocess

d = u2.connect('172.21.13.123')

d(scrollable=True).scroll.toEnd()
