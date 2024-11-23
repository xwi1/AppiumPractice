class Settings:

    browser = {
        'NoSandBox': False,
        'Headless': False
    }

    page = {
        'Link': 'https://mail.ru'
    }

    mobile_stand = {
        'appium_server': 'http://127.0.0.1:4723',
        'Pixel_6':
            {
                'platformName': 'Android',
                'platformVersion': '34',
                'deviceName': 'Pixel_6',
                'appPackage': 'com.ngieu.scheduleapp',
                'appActivity': 'com.example.pu_app.MainActivity',
                'language': 'ru',
                'locale': 'RU'
            },
        'Xiaomi M2191K9AG':
            {
                'platformName': 'Android',
                'platformVersion': '33',
                'deviceName': 'Xiaomi M2191K9AG',
                'appPackage': 'com.ngieu.scheduleapp',
                'appActivity': 'com.example.pu_app.MainActivity',
                'language': 'ru',
                'locale': 'RU'
            }
    }