import uiautomator2 as u2


d = u2.connect()
d.keyevent("home")
d(resourceId='com.viewsonic.sidetoolbar:id/arrow').click()
d(resourceId='com.viewsonic.sidetoolbar:id/btnAllTools').click()
d.xpath('//*[@text="Spotlight"]').click()
d().pinch_in(percent=10, steps=10)
d(resourceId='com.viewsonic.sidetoolbar:id/settings_btn').click()
d(resourceId='com.viewsonic.sidetoolbar:id/seekbar_alpha').swipe("left")
d().swipe('left')
d().swipe('up')
d().swipe('right')
d().swipe('down')
