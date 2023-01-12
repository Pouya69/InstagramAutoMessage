from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome('./chromedriver.exe')


def start_messaging():
    message_area = driver.find_element_by_css_selector("textarea")
    for i in range(200):
        message_area.send_keys(f"YOUR MESSAGE")
        message_area.send_keys(Keys.ENTER)
    message_area.send_keys(Keys.ENTER)


if __name__ == '__main__':
    username = "YOUR USERNAME"
    password = "YOUR PASSWORD"
    driver.get("https://www.instagram.com")
    sleep(3)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
    input("Go to the chat room and press Enter to continue")
    start_messaging()
