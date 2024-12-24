from FW.fw_mobile_base import FwMobileBase


class Locator:
    input_search = '//android.widget.EditText'
    igo_string = '//android.view.View[contains(@content-desc, "21 ИгО")]'
    krivonogov_string = '//android.view.View[contains(@content-desc, "Кривоногов С.В.")]'



class ScheduleScreen(FwMobileBase):

    def click_input_search(self):
        search = self.send_keys_by_xpath(Locator.input_search, '21')
        self.click_by_xpath(Locator.igo_string)
        assert self.find_element_by_xpath(Locator.krivonogov_string)