import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import StaleElementReferenceException

from FW.FW_Base import FWBase


class FwMobileBase(FWBase):

    def get_driver(self):
        if self.manager.appium_instance.driver is None:
            self.manager.appium_instance.get_appium_driver()
        return self.manager.appium_instance.driver

    def find_element(self, by, value):
        return self.get_driver().find_element(by, value)

    def click_by_xpath(self, locator):
        element = self.find_element(by=AppiumBy.XPATH, value=locator)
        element.click()

    def appium_driver_sleep(self, time):
        self.get_driver().implicitly_wait(time)

    def appium_driver_switch_to(self, context):
        self.get_driver().switch_to.context(context)

    def swipe(self, x_start: int, y_start: int, x_stop: int, y_stop: int, swipe_time=100):
        return self.get_driver().swipe(x_start, y_start, x_stop, y_stop, swipe_time)

    def click_by_class(self, locator):
        return self.find_element(by=AppiumBy.CLASS_NAME, value=locator).click()

    def scroll_to_element(self, by, value, down=True, search_before_scroll=False, step=1):
        if down:
            direction = f"new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd({step}))"
        else:
            direction = f"new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning({step}))"
        for count in range(30):
            try:
                if search_before_scroll:
                    try:
                        # Ищем элемент перед тем как скролить
                        el = self.find_element(by, value, 2)
                        if el:
                            return el
                    except:
                        pass
                # Скролим вниз
                self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, direction, 2)
                # Если скрол не дошёл до конца - ищем элемент на страницу
                el = self.find_element(by, value, 2)
                if el:
                    return el
            except:
                try:
                    # Ищем элемент на странице
                    el = self.find_element(by, value, 2)
                    if el:
                        return el
                except:
                    pass
            return self

    def scroll_by_direction(self, down=True, step=1, count=1):
        for _ in range(count):
            if down:
                direction = f"new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd({step}))"
            else:
                direction = f"new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning({step}))"
            try:
                # Скролим по напровлению
                self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, direction, 0)
            except:
                pass
        return self

    def scroll_to_elements(self, value, by=AppiumBy.ID, down=True, step=1):
        if down:
            direction = f"new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd({step}))"
        else:
            direction = f"new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning({step}))"
        for count in range(30):
            try:
                try:
                    els = self.find_elements(by, value, 0)
                    if len(els) > 0:
                        return els
                except:
                    self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, direction, 0)
                    els = self.find_elements(by, value, 0)
                    if len(els) > 0:
                        return els
            except:
                try:
                    els = self.find_elements(by, value, 0)
                    if len(els) > 0:
                        return els
                except:
                    pass
        return self

    def send_keys_by_xpath(self, locator, text):
        # Нажимаем на поле ввода
        self.click_by_xpath(locator)
        return self.find_element(AppiumBy.XPATH, locator).send_keys(text)

    def send_keys_with_android(self, locator, text, by=AppiumBy.ID):
        el = self.find_element(by, locator)
        el.click()
        for char in text:
            if char.isupper():
                self.get_driver().press_keycode(self.manager.group_data.android_keys['shift'])
            char = char.lower()
            self.get_driver().press_keycode(self.manager.group_data.android_keys[char])
        return

    def send_keys_by_id(self, locator, text):
        el = self.find_element(AppiumBy.ID, locator)
        el.click()
        return el.send_keys(text)

    def hide_keyboard(self):
        self.get_driver().hide_keyboard()

    def click_keyboard_enter(self):
        self.get_driver().press_keycode(66)

    def clear_and_send_keys_by_xpath(self, locator, text):
        self.clear_text(locator)
        self.get_driver().find_element(locator).send_keys(text)

    def get_tag_text(self, locator, by=AppiumBy.ID):
        for i in range(3):
            try:
                return self.find_element(by=by, value=locator).text
            except StaleElementReferenceException:
                time.sleep(0.5)
        raise StaleElementReferenceException

    def get_tag_attribute(self, locator, attribute, by=AppiumBy.ID):
        el = self.find_element(by=by, value=locator)
        return el.get_attribute(attribute)

    def get_tags_text(self, locator):
        text = []
        for el in self.find_elements(by=AppiumBy.ID, value=locator):
            text.append(el.text)
        return text

    def clear_text(self, locator):
        self.get_driver().find_element(locator).clear()

    def sleep_mob(self, time):
        self.get_driver().implicitly_wait(time)

    def driver_switch_to(self, context):
        self.get_driver().switch_to.context(context)

    def find_elements(self, by, value, wait=None):
        if wait is None:
            wait = self.manager.settings.time_element_Wait
        self.sleep_mob(wait)
        return self.get_driver().find_elements(by, value)

    def clear_and_send_keys_by_id(self, locator, text):
        for i in range(3):
            try:
                android_element = self.find_element(by=AppiumBy.ID, value=locator)
                android_element.click()
                android_element.clear()
                android_element.send_keys(text)
                return android_element
            except StaleElementReferenceException:
                time.sleep(0.5)
        raise StaleElementReferenceException

    def click_by_id(self, locator, wait=None):
        for i in range(3):
            try:
                android_element = self.find_element(by=AppiumBy.ID, value=locator, wait=wait)
                android_element.click()
                return android_element
            except StaleElementReferenceException:
                time.sleep(0.5)
        raise StaleElementReferenceException

    def mobile_check_toast_message(self):
        try:
            self.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.Toast')
            return True
        except:
            return False

    def mobile_check_element(self, by, value, wait=None):
        if wait is None:
            wait = self.manager.settings.time_element_Wait
        try:
            self.find_element(by=by, value=value, wait=wait)
            return True
        except:
            return False

    def mobile_double_click(self, x, y):
        return self.get_driver().execute_script('mobile: doubleClickGesture', {'x': x, 'y': y})

    def mobile_long_click(self, x, y, duration=1000):
        return self.get_driver().execute_script('mobile: longClickGesture', {'x': x, 'y': y, 'duration': duration})

    def wait_change_activity(self, new_activity: str):
        for i in range(3):
            current_activity = self.get_driver().current_activity
            if new_activity != current_activity:
                time.sleep(2)
            else:
                return self
        raise Exception(f'Не удалось дождаться смены Activity!')

    def wait_disappear_activity(self, activity: str):
        for i in range(3):
            current_activity = self.get_driver().current_activity
            if activity == current_activity:
                # Ожидаем смену Activity
                time.sleep(3)
            else:
                # Ожидаем полную загрузку нового Activity
                time.sleep(5)
                return self
        raise Exception(f'Не удалось дождаться смены Activity!')