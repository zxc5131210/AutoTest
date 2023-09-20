import time
import uiautomator2 as u2

# 连接到设备
d = u2.connect()
element_bounds = d.info
center_x = (element_bounds['displayWidth']) // 2
center_y = (element_bounds['displayHeight']) // 2
print(center_x, center_y)
for i in range(100):
    y_start = i
    d.swipe(fx=0, fy=y_start, tx=center_x, ty=y_start)
