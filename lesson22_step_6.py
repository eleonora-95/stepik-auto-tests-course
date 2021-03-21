from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    # Посчитать математическую функцию от x
    y = calc(x)

    # Проскроллить страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")

    # Ввести ответ в текстовое поле
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    # Отметить checkbox "I'm the robot"
    chbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    chbox.click()

    # Выбрать radiobutton "Robots rule!"
    rbutton = browser.find_element_by_css_selector("[for='robotsRule']")
    rbutton.click()

    # Нажать на кнопку Submit
    button = browser.find_element_by_tag_name("button")
    button.click()
    assert True

finally:
    time.sleep(10)
    browser.quit()
