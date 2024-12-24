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
                'platformVersion': '35',
                'deviceName': 'Pixel_6',
                'appPackage': 'com.ngieu.scheduleapp',
                'appActivity': 'com.example.pu_app.MainActivity',
                'language': 'en',
                'locale': 'US'
            }
    }