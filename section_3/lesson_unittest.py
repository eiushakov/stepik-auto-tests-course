from selenium import webdriver
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = filling_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = filling_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


def filling_form(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет все поля
    input1 = browser.find_element_by_css_selector('.first_block >.form-group.first_class>input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('.first_block >.form-group.second_class>input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.first_block >.form-group.third_class>input')
    input3.send_keys("test@test.ru")

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
    browser.quit()
    return welcome_text


if __name__ == "__main__":
    unittest.main()
