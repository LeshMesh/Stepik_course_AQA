from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name('firstname').send_keys('Имя')
    browser.find_element_by_name('lastname').send_keys('Фамилия')
    browser.find_element_by_name('email').send_keys('email')
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_css_selector('button.btn').click()
    time.sleep(5)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
