from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    sum = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)
    Select(browser.find_element_by_tag_name('select')).select_by_visible_text(str(sum))
    browser.find_element_by_css_selector('button.btn').click()
    time.sleep(5)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
