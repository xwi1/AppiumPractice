from FW.fw_mobile_base import FwMobileBase

class Locator:
    button_skip = '//android.widget.Button[@content-desc="Пропустить"]'
    change_week = '//android.widget.Button[@content-desc="ВН / НН"]'


class StartScreen(FwMobileBase):

    def click_button_skip(self):
        self.click_by_xpath(Locator.button_skip)
        return self

    def click_button_change_week(self):
        self.click_by_xpath(Locator.change_week)
        return self