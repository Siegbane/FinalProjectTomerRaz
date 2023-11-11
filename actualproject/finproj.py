from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from stuffforcouse.selenium_base import selenium_base


class finproj:
    base = selenium_base()
    driver = base.selenium_init("https://www.booking.com/")

    search = driver.find_element(By.CLASS_NAME, "eb46370fe1")
    button = driver.find_element(By.CLASS_NAME, "e4adce92df")



    search.click()
    search.send_keys("toronto")
    button.click()





    def find_highest_score(scores):
        if not scores:
            return "No scores provided"

        highest_score = scores[0]

        for score in scores:
            if score > highest_score:
                highest_score = scores

        return highest_score

    base.selenium_end(driver)