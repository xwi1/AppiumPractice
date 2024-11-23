import time

from Test.mobile_base import MobileBase


class TestMobile(MobileBase):

    def test_run(self):
        time.sleep(30)
        self.APP.start_screen.click_button_skip()
        self.APP.start_screen.click_button_change_week()
        print()