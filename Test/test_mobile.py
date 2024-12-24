import time

from Test.mobile_base import MobileBase


class TestMobile(MobileBase):

    def test_run(self):
        time.sleep(3)
        start_screen = self.APP.start_screen.skip_tutorial()
        schedule_screen = self.APP.schedule_screen.click_input_search()
        
        