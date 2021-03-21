from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для первой переменной
    elem1 = browser.find_element_by_id("num1")
    v1 = elem1.text

    # Считать значение для второй переменной
    elem2 = browser.find_element_by_id("num2")
    v2 = elem2.text

    # Посчитать сумму заданных чисел
    sum = str(int(v1) + int(v2))

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum)

    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
