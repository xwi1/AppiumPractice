import os
import subprocess

from Data.settings import Settings


class EmulatorInstance:

    def __init__(self):
        self.settings = Settings

    def start_emulator(self):
        subprocess.Popen(['emulator', '@Pixel_6'])
        os.system('adb wait-for-device')
        subprocess.run('adb shell service call alarm 3 s16 Europe/Moscow')

    def stop_emulator(self):
        os.system('adb devices')
        subprocess.call(['adb', '-s', 'emulator-5554', 'emu', 'kill'])

    def clear_cache(self):
        os.system(('adb shell pm com.ngieu.scheduleapp'))