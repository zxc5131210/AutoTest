'''This is a demo test for gesture automation.'''
from appium import webdriver
import config
from event_generator import EventGen

# Step 1 : Create Desired Capabilities
desired_caps = {}
desired_caps['platformName'] = config.platformName
desired_caps['platformVersion'] = config.platformVersion
desired_caps['deviceName'] = config.deviceName
desired_caps['udid'] = config.udid

# Step 2 : Create Driver object
driver = webdriver.Remote(
    f'http://{config.host}:{config.port}/wd/hub', desired_caps)

# Step 3 : Create gesture automation flow
event_gen = EventGen()
event_gen.generate_event(json_path='./motion_flow.json', driver=driver)
