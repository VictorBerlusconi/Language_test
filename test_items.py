from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_add_to_cart_button(browser):  # opens the link and checks button existence
    browser.get(link)
    # time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button) > 0, "Button wasn't found!"  # check that button is found so array is not empty
