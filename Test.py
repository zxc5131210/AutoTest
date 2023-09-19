import uiautomator2 as u2
import time

d = u2.connect()
# d.xpath('//*[@resource-id="com.viewsonic.sidetoolbar:id/container"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]').swipe('right')
ele = d.xpath(
    '//*[@resource-id="com.viewsonic.sidetoolbar:id/container"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]')
print(ele.info)
