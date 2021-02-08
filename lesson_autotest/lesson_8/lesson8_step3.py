import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/selects1.html"
    new_link = "http://suninjuly.github.io/selects2.html"
    
    browser = webdriver.Chrome()
    browser.get(new_link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    summ = int(num1.text) + int(num2.text)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(summ))
        
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Печать "Passed", если тест прошел успешно
    print("--- PASSED ---")

    # Печать "Failed" и ошибки, если тест провален
except Exception as ex:
    print("--- FAILED ---")
    print(ex)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
