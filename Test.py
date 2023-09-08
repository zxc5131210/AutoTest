'''This is a demo test for gesture automation.'''
import uiautomator2 as u2
import subprocess

# d = u2.connect('172.21.10.20:5555')

# elements = d(resourceId="com.viewsonic.sidetoolbar:id/arrow")
# elements.click()

command = f'adb shell rm /sdcard/Wallpaper_TestPhoto.jpg'
subprocess.run(command, shell=True, capture_output=True,
               text=True, check=False)
