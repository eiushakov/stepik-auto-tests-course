import time
import math
import pytest


@pytest.mark.parametrize('number', [236895, 236896,  236897, 236898, 236899, 236903, 236904, 236905])
def test_search_ufo_text(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1/"
    browser.get(link)
    input1 = browser.find_element_by_css_selector("textarea")
    input1.click()
    answer = str(math.log(int(time.time())))
    input1.send_keys(answer)
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    result = browser.find_element_by_css_selector(".smart-hints__hint")
    assert result.text == "Correct!", f"Part of traces UFO is '{result.text}'"



