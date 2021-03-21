from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    # Посчитать математическую функцию от x
    y = calc(x)

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
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
