#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest
from selenium import webdriver
from pages.setting import drv_path
import uuid


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1400, 1000)

    test_num = str(uuid.uuid4())
    print(f"\nTest number: {test_num}\n")

    # Return browser instance to test case:
    yield browser

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'yellow';")

            # Make screen-shot for local debug:
            browser.save_screenshot(f'screenshots/{test_num}.png')
            print(f"\nScreenshot with error: {test_num}.png\n")

        except:
            pass # just ignore any errors here

    browser.quit()