from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    new_link = "http://suninjuly.github.io/registration2.html"
    
    browser = webdriver.Chrome()
    browser.get(new_link)

    # Ваш код, который заполняет все поля
    input1 = browser.find_element_by_css_selector('.first_block >.form-group.first_class>input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('.first_block >.form-group.second_class>input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.first_block >.form-group.third_class>input')
    input3.send_keys("test@test.ru")
    input4 = browser.find_element_by_css_selector('.second_block >.form-group.first_class>input')
    input4.send_keys("+000000000")
    input5 = browser.find_element_by_css_selector('.second_block >.form-group.second_class>input')
    input5.send_keys("USSR")
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    
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
    
