from Test.mobile_base import MobileBase


class TestMobile(MobileBase):

    def test_run(self):
        self.APP.start_screen.click_button_skip()
        print()