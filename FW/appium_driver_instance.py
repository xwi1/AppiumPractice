import os.path
from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options

from Data.settings import Settings


class AppiumDriverInstance:

    mobile_stand = 'Xiaomi M2191K9AG'

    def __init__(self):
        self.settings = Settings

    driver = None

    def get_appium_driver(self):
        if self.driver is None:
            options = UiAutomator2Options()
            options.platform_name = self.settings.mobile_stand[self.mobile_stand]['platformName']
            options.device_name = self.settings.mobile_stand[self.mobile_stand]['deviceName']
            options.app_package = self.settings.mobile_stand[self.mobile_stand]['appPackage']
            options.app_activity = self.settings.mobile_stand[self.mobile_stand]['appActivity']
            options.app = os.path.join(Path(__file__).parent.parent, 'Data', 'Ngieu.apk')
            options.auto_grant_permissions = True
            options.ignore_hidden_api_policy_error = True
            options.language = self.settings.mobile_stand[self.mobile_stand]['language']
            options.locale = self.settings.mobile_stand[self.mobile_stand]['locale']

            self.driver = webdriver.Remote(self.settings.mobile_stand['appium_server'], options=options)
        return self.driver

    def stop_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None


