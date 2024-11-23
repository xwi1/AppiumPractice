import os
import subprocess

from Test.test_base import TestBase


class MobileBase(TestBase):

    def setup_class(self):
        #self.APP.emulator_instance.start_emulator()
        pass

    def setup_method(self):
        self.APP.appium_instance.get_appium_driver()

    def teardown_method(self):
        self.APP.emulator_instance.clear_cache()
        self.APP.appium_instance.stop_driver()