import subprocess
import uiautomator2 as u2
import time

# 初始化连接到设备
d = u2.connect()
print(d.app_current())
