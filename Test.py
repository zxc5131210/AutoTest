import uiautomator2 as u2
import concurrent.futures
import time
import os
# 初始化连接到设备
d = u2.connect()

d.screen_off()
