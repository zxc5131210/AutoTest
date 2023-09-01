'''This is a demo test for gesture automation.'''
from appium import webdriver
import config
from event_generator import EventGen
from appium.webdriver.common.appiumby import AppiumBy

# Step 1 : Create Desired Capabilities
desired_caps = {}
desired_caps['platformName'] = config.platformName
desired_caps['platformVersion'] = config.platformVersion
desired_caps['deviceName'] = config.deviceName

# Step 2 : Create Driver object
driver = webdriver.Remote(
    f'http://{config.host}:{config.port}/wd/hub', desired_caps)

elements = driver.find_elements(
    AppiumBy.ID, "com.viewsonic.wallpaperpicker:id/wallpaper_image")

# 輸出找到的元素數量
print(f"找到了 {len(elements)} 個元素：")

# 列印每個找到的元素的文本
for element in elements:
    print('123', element.text)
