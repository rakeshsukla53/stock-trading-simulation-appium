import sys
from appium import webdriver
from time import sleep
from prop import *
from common import *
from selenium.common.exceptions import WebDriverException


def start_driver(command_executor=appium_webdriver_host, desired_capabilities=None):
    '''
    This will attempt to start the session through webdriver remote, and it will try several times before error out
    :param command_executor: the default webdriver host
    :param desired_capabilities: app desired capabilities. Refer to this link for more context -
    https://appium.io/docs/en/writing-running-appium/caps/
    :return:
    '''

    for _ in range(webdriver_start_retry):
        try:
            # wait for 3 seconds before attempting to start
            sleep(3)
            driver = webdriver.Remote(command_executor, desired_capabilities)
            print("{} webdriver session id: {}".format(generate_formatted_timestamp(), driver.session_id))
            return driver
        except Exception as e:
            print("{} Error: Instantiating WebDriver. Reason: {}".format(generate_formatted_timestamp(), e))

    raise WebDriverException("{} Failed to instantiate a webdriver instance".format(generate_formatted_timestamp()))


def implicitly_wait(driver, timeout=implicitly_wait_time):
    '''
    set implicit wait time
    '''
    driver.implicitly_wait(timeout)


def on_platforms(platforms):
    '''
    pass multiple platform configurations to be run in a single pass
    '''

    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = type(name, (base_class,), d)
    return decorator
