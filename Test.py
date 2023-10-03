import uiautomator2 as u2
import subprocess

# 连接到设备
d = u2.connect()
device=d.device_info
device_model = device['model']
print(device_model)
elements=d(resourceId='com.android.documentsui:id/roots_list').child(text=device_model).click()