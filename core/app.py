import sys
from appium import webdriver
from time import sleep
from prop import *
from common import *
from warnings import filterwarnings
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


def start_driver(command_executor=appium_webdriver_host, desired_capabilities=None):
    """
    This will attempt to start the session through webdriver remote, and it will try several times before error out
    :param command_executor: the default webdriver host
    :param desired_capabilities: app desired capabilities. Refer to this link for more context -
    https://appium.io/docs/en/writing-running-appium/caps/
    :return:
    """

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


def parse_locator(value, description=None):
    """Parse page object tuple or string."""
    try:
        global locator_path, locator_type
        if isinstance(value, tuple):
            locator_path, locator_type = value[0], value[1].lower()
            try:
                if description and value[2]:
                    text = str(description) + " " + str(value[2])
                    print("{} {}".format(generate_formatted_timestamp(), text))
            except IndexError:
                pass
        else:
            raise 'Error parsing locator: Please ensure you are passing a valid tuple or string...'
    except Exception as e:
        raise ('Parse Locator Exception...\n{}'.format(e))


def implicitly_wait(driver, timeout=implicitly_wait_time):
    """ set implicit wait time """
    driver.implicitly_wait(timeout)


def find_element(driver, locator):
    """Find a single WebElement"""
    parse_locator(locator, 'Find element')
    return driver.find_element(locator_type, locator_path)


def find_elements(driver, locator):
    """Find a list of WebElements."""
    parse_locator(locator, 'Find elements')
    return driver.find_elements(locator_type, locator_path)


def tap(driver, locator, idx=None):
    """ simulate tap gesture on single or multiple elements"""
    filterwarnings("ignore")
    parse_locator(locator, "Tap")
    if idx:
        tap_obj = getattr(driver, 'find_elements')(locator_type, locator_path)[idx]
    else:
        tap_obj = getattr(driver, 'find_element')(locator_type, locator_path)
    action = TouchAction(driver)
    action.tap(tap_obj, 0, 0).perform()


def input_text(driver, locator, text, idx=None):
    """ Enter text into a text area/field. Optionally pass position (eg. 0, 1, 2). """
    parse_locator(locator, u'Input {} into'.format(text))
    if idx:
        driver.find_elements(locator_type, locator_path)[idx].send_keys(text)
    else:
        driver.find_element(locator_type, locator_path).send_keys(text)


def is_element_present(driver, locator, wait_time=2):
    """Return boolean indicating whether element is present."""
    parse_locator(locator, 'Is element present')
    try:
        driver.implicitly_wait(wait_time)
        driver.find_element(locator_type, locator_path)
        return True
    except WebDriverException:
        print("{} is not present".format(locator_path))
        return False
    finally:
        driver.implicitly_wait(implicitly_wait_time)


def explicit_wait(driver, locator, timeout=explicit_wait_time, interval=0.5):
    """ Explicit wait for an element to be displayed on the page. """
    if is_element_present(driver, locator):
        return
    parse_locator(locator, 'Wait for element is displayed:')
    locator_tuple = (locator_type, locator_path)
    WebDriverWait(driver, timeout, interval).until(EC.visibility_of_element_located(locator_tuple))


def return_text(driver, locator, idx=None):
    """Return text of an element."""
    if idx is None:
        parse_locator(locator, 'Return text of')
        return driver.find_element(locator_type, locator_path).text
    else:
        parse_locator(locator, "Return text at index {} of".format(idx))
        return driver.find_elements(locator_type, locator_path)[idx].text


def back(driver):
    """ Simulate user clicking  back button. """
    driver.back()
    print('{} Pressed browser back button'.format(generate_formatted_timestamp()))


def swipe(driver, positions, duration=1000):
    """Swipe action. X/Y coordinates required for both start and end."""
    start_x, start_y, end_x, end_y = positions
    driver.swipe(start_x, start_y, end_x, end_y, duration)


def long_press_by_coordinates(driver, x, y, duration=10000):
    """Long press by coordinate. Works similar to tap + duration."""
    action = TouchAction(driver)
    action.press(x=x, y=y).wait(duration).move_to(x=x, y=y).release().perform()
