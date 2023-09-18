import uiautomator2 as u2
import time

d = u2.connect()
ele = d(resourceId='com.viewsonic.vlauncher:id/remove_task')
ele.click()
