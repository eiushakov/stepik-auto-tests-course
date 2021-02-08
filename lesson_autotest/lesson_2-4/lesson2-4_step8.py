import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    option = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), str(100)))
    button = browser.find_element_by_id("book")
    button.click()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("input")
    input1.send_keys(y)
        
    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
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
    
