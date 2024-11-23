from FW.fw_mobile_base import FwMobileBase

class Locator:
    input_search = '//android.widget.EditText'


class ScheduleScreen(FwMobileBase):

    def click_input_search(self):
        self.click_by_xpath(Locator.input_search)
        return self