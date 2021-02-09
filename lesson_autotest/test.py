import time
import math
import pytest
from selenium import webdriver

answer = str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser


@pytest.mark.parametrize('number', [236895])
def test_search_ufo_text(browser, number):
    link = f"https://stepik.org/lesson/236895/step/1/"
    browser.get(link)
    input1 = browser.find_element_by_css_selector("textarea")
    input1.click()
    input1.send_keys(answer)
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    result = browser.find_element_by_css_selector(".smart-hints__hint")
    assert result.text == "Correct!", "Looking for traces of  UFO"
    time.sleep(1)
