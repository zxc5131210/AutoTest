import uiautomator2 as u2
import time

d = u2.connect()

# ele = d.xpath('//*[@resource-id="com.viewsonic.sidetoolbar:id/hour_wheelview"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]')
# print(ele.text)

target_text = '10'
target_scrollbar = 'com.viewsonic.sidetoolbar:id/hour_wheelview'
ele = '//*[@resource-id="com.viewsonic.sidetoolbar:id/hour_wheelview"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]'
# 循环滑动并查找文本
for _ in range(60):
    if d.xpath(ele).text == target_text:
        # 找到文本后执行操作，例如点击元素
        break  # 找到后跳出循环
    else:
        # 如果未找到文本，继续滑动
        d(resourceId=target_scrollbar).swipe('up')

# 如果循环结束仍未找到文本，可以添加适当的处理
51
