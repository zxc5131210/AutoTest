import uiautomator2 as u2
import concurrent.futures
import time
import os
# 初始化连接到设备
d = u2.connect()

# d.screenshot("QAQ.png")
screenshot = './QAQ.png'

current_directory = os.getcwd()
for filename in os.listdir(current_directory):
    filepath = os.path.join(current_directory, filename)
    if os.path.isfile(screenshot):
        os.remove(screenshot)
