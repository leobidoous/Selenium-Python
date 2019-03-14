from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("../driver/chromedriver")

driver.maximize_window()
driver.get("https://www.google.com.br")

driver.set_page_load_timeout(20)
driver.find_element_by_name("q").send_keys("PUC Campus V")
driver.find_element_by_name("btnK").submit()
driver.find_element_by_link_text("Como chegar").click()
driver.find_element_by_class_name("tactile-searchbox-input").send_keys("\x08\x08\x08\x08\x08\x08\x08\x08\x08PUC 3")
driver.find_element_by_class_name("searchbox-searchbutton").click()

sleep(15)
driver.quit()