import time

from FW.fw_mobile_base import FwMobileBase

class Locator:
    button_skip = '//android.widget.Button[@content-desc="Пропустить"]'
    skip_tutorial = '//android.widget.EditText'


class StartScreen(FwMobileBase):

    def click_button_skip(self):
        self.click_by_xpath(Locator.button_skip)
        return self

    def skip_tutorial(self):
        self.click_button_skip()
        time.sleep(1)
        for _ in range(13):
            self.click_by_xpath(Locator.skip_tutorial)
        return self.manager.schedule_screen

