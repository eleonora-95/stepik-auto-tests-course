from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    print(browser.window_handles)
    orig_window = browser.window_handles[0]
    fst_window = browser.window_handles[1]
    snd_window = browser.window_handles[2]
    browser.switch_to.window(snd_window)

    # Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

