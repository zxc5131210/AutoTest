import uiautomator2 as u2
import subprocess

# 连接到设备
d = u2.connect()

d.screenshot("qqq")
# element_bounds = d.info
# center_x = (element_bounds["displayWidth"]) // 2
# x_bounds = element_bounds["displayWidth"]
# bottom = element_bounds["displayHeight"]
# width = element_bounds["displayWidth"]
#
# d(resourceId="com.viewsonic.sidetoolbar:id/flOpenBar").click()
# d(resourceId="com.viewsonic.sidetoolbar:id/vPenColor").click()
# count = 0
# while True:
#     for i in range(1, 9):
#         d.xpath(
#             f"//*[@resource-id='com.viewsonic.sidetoolbar:id/colorPickerRadioGroup']/android.widget.RadioButton[{i}]"
#         ).click()
#         line = 0
#         line2 = 0
#         linex = 0
#         linex2 = center_x
#         offset = 10
#         if d(resourceId="com.viewsonic.sidetoolbar:id/vPenColor").exists:
#             for _ in range(200):
#                 y_start = line
#                 line += offset
#                 d.drag(center_x, y_start, 0, y_start, duration=0.05)
#                 y_start += offset
#                 d.drag(center_x, y_start, 0, y_start, duration=0.05)
#                 y_start += offset
#                 d.drag(center_x, y_start, 0, y_start, duration=0.05)
#                 count += 1
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/redo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/redo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 print(count)
#             for _ in range(200):
#                 y_start = line2
#                 line2 += 10
#                 d.drag(center_x, y_start, width, y_start, duration=0.05)
#                 y_start = offset
#                 d.drag(center_x, y_start, width, y_start, duration=0.05)
#                 y_start = offset
#                 d.drag(center_x, y_start, width, y_start, duration=0.05)
#                 count += 1
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/redo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/redo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 print(count)
#
#             for _ in range(400):
#                 x_start = linex
#                 linex += offset
#                 d.drag(x_start, 0, x_start, bottom, duration=0.05)
#                 x_start += offset
#                 d.drag(x_start, 0, x_start, bottom, duration=0.05)
#                 x_start += offset
#                 d.drag(x_start, 0, x_start, bottom, duration=0.05)
#                 count += 1
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/redo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/redo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#                 print(count)
#         else:
#             print("final:", count)


# line = 0
# for i in range(100):
#     y_start = line
#     line += 20
#     d.drag(center_x, y_start, 0, y_start, duration=0.05)
#     y_start += 20
#     d.drag(center_x, y_start, 0, y_start, duration=0.05)
#     y_start += 20
#     d.drag(center_x, y_start, 0, y_start, duration=0.05)
#     d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#     d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#     d(resourceId="com.viewsonic.sidetoolbar:id/redo").click()
#     d(resourceId="com.viewsonic.sidetoolbar:id/redo").click()
#     d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#     d(resourceId="com.viewsonic.sidetoolbar:id/undo").click()
#     count += 1
#     print(count)
