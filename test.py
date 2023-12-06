import uiautomator2 as u2

d = u2.connect()
# element_bounds = d.info
# while True:
#     d(resourceId="com.viewsonic.sidetoolbar:id/flOpenBar").click()
#     d(resourceId="com.viewsonic.sidetoolbar:id/imgBtnAllTools").click()
#     d.xpath("//*[@text='Marker']").click()
#     center_x = (element_bounds["displayWidth"]) // 2
#     for i in range(400):
#         y_start = i
#         d.swipe(fx=0, fy=y_start, tx=center_x, ty=y_start, duration=0.05)
#     d(resourceId="com.viewsonic.sidetoolbar:id/close").click()
ele = d(resourceId="com.viewsonic.vlauncher:id/label")
list = []
for i in ele:
    list.append(i.get_text())
print(list)
