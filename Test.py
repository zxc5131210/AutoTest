import uiautomator2 as u2
import subprocess

# 连接到设备
d = u2.connect()

print(d.app_current())
