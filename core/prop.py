from pathlib import Path

appium_webdriver_host = "http://localhost:4723/wd/hub"
webdriver_start_retry = 5
implicitly_wait_time = 6
explicit_wait_time = 5


def get_current_working_directory():
    parent_folder_path = Path(__file__).resolve().parent
    project_path = parent_folder_path.parent
    android_apk_path = "/apk/stock-simulator.apk"
    android_absolute_path = str(project_path) + android_apk_path
    return android_absolute_path


android_app = [

    {
        "app": get_current_working_directory(),
        "deviceName": "pixel_2",
        "platformName": "Android",
        "automationName": "uiautomator2",
        "platformVersion": "11.0",
        "new-command-timeout": 120,
        "command-timeout": 120
    }

]
