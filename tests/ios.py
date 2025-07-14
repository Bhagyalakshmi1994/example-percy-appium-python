import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.ios import XCUITestOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from percy import percy_screenshot



USER_NAME = "bhagyalakshmik_qERVnx"
ACCESS_KEY = "ULzcw8GxxPgCfwTDWok6"


def run_session(capability):
    options = XCUITestOptions().load_capabilities(capability)
    driver = webdriver.Remote("https://hub-cloud.browserstack.com/wd/hub", options=options)
    text_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Button"))
    )
    text_button.click()
    text_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
    )
    #text_input.send_keys("hello@browserstack.com" + "\n")
    text_input.send_keys("BrowserStack again" + "\n")
    time.sleep(1)
    driver.hide_keyboard()
    percy_screenshot(driver, 'screenshot 1')
    driver.quit()


if __name__ == '__main__':
    ios_capability = {
        "deviceName": "iPhone 14",
        "os_version": "16",
        "app":  'bs://c6d80720f4964e9e02ac98f935b417d2a43321a9',
        "appium:percyOptions": {
            # enabled is default True. This can be used to disable visual testing for certain capabilities
            "enabled": True
        },
        'bstack:options' : {
            "projectName" : "My Project",
            "buildName" : "test percy_screnshot",
            "sessionName" : "BStack first_test",

            # Set your access credentials
            "userName" : USER_NAME,
            "accessKey" : ACCESS_KEY
        },
        "platformName": "ios",
    }

    capabilities_list = [ios_capability]
    list(map(run_session, capabilities_list))


 