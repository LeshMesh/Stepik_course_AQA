from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/math.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_checked = browser.find_element_by_css_selector("button.btn").get_attribute("disabled")
    print("disabled is: ", people_checked)
    time.sleep(11)
    people_checked2 = browser.find_element_by_css_selector("button.btn").get_attribute("disabled")
    print("disabled is: ", people_checked2)
    # assert people_checked is not None, "People radio is not selected by default"


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
