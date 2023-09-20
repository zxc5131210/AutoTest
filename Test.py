import time
import uiautomator2 as u2

# 连接到设备
d = u2.connect()

d(resourceId='com.viewsonic.sidetoolbar:id/select').click()
