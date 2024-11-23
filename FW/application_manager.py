from Data.settings import Settings
from FW.FW_Base import FWBase
from FW.appium_driver_instance import AppiumDriverInstance
from FW.driver_instance import DriverInstance
from FW.emulator_instance import EmulatorInstance
from FW.fw_mobile_base import FwMobileBase
from FW.mail.main_page import MainPage
from FW.mail.search_page import SearchPage
from FW.start_screen import StartScreen


class ApplicationManager:

    def __init__(self):

        self.driver_instance = DriverInstance()
        self.fw_base = FWBase(self)
        self.fw_mobile_base = FwMobileBase(self)
        self.settings = Settings()
        self.main_page = MainPage(self)
        self.search_page = SearchPage(self)
        self.emulator_instance = EmulatorInstance()
        self.appium_instance = AppiumDriverInstance()
        self.start_screen = StartScreen(self)
