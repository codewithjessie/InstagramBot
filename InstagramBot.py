from selenium import webdriver
from time import sleep
import random


class InstaBot:

    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def login(self):
        self.browser.get('https://www.instagram.com/')
        sleep(1)

        # login with username and password
        self.browser.find_element_by_xpath('//input[@name=\"username\"]').send_keys(username)
        self.browser.find_element_by_xpath('//input[@name=\"password\"]').send_keys(password)
        self.browser.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(3)

        # save password? - not now
        #self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        #sleep(3)

        # turn on notifications? - not now
        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    # scrolls feed and likes posts
    def scroll_and_like(self):
        # TEST CODE: scrolling
        i = 0
        while i < 20:
            # print(i)
            start = 1000 * i
            end = 1000 * (i + 1)
            self.browser.execute_script(f"window.scrollTo({start},{end})")
            sleep(1)
            i += 1

    # randomly likes posts on explore page
    def browse_explore(self):
        self.browser.get('https://www.instagram.com/explore/')
        sleep(3)

        # identifies post on explore page
        post = self.browser.find_element_by_class_name("_9AhH0")
        post.click()

        # views 12 posts and randomly like
        #note: 12 is the maximum on web browser 
        i = 0
        while i < 12:
            # randomly like 80% of posts
            n = random.random()
            if n < .8:
                sleep(2)
                like_path = self.browser.find_element_by_xpath('\
                /html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div')
                like_path.click()
                sleep(1)
            # next post
            self.browser.find_element_by_xpath("//a[contains(text(), 'Next')]").click()
            sleep(2)
            i += 1


# ENTER username and password for the account you are logging into
username = input("Username: ")
password = input("Password: ")


# launching Instagram Bot
instaBot = InstaBot(username, password)
instaBot.login()
# instaSession.scroll_and_like()
instaBot.browse_explore()
