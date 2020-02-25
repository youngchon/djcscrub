from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import os
import time

class login:
    BASE_URL='https://www.djcity.com'
    SIGN_IN_URL = BASE_URL + '/signin.aspx'

    def __init__(self, driver):
        self.d=driver

        self.set_credentials()
        self.signin()

    def set_credentials(self):
        local_path = os.path.dirname(os.path.realpath('__file__'));
        filename = os.path.join(local_path, "user.info")
        file = open(filename, "r")
        self.user = file.readline()
        self.pw = file.readline()


    def signin(self):
        self.d.get(self.SIGN_IN_URL)
        title = self.d.title
        print ("title: {}".format(title))

        user_input= self.d.find_element_by_css_selector("input[name*=UserName]")
        print user_input
        user_input.clear()

        pass_input= self.d.find_element_by_css_selector("input[type=password]")
        print pass_input
        pass_input.clear()

        submit_button = self.d.find_element_by_css_selector("input[type=submit]")

        actions = ActionChains(self.d)
        actions.send_keys_to_element(user_input, self.user)
        actions.send_keys_to_element(pass_input, self.pw)
        actions.click(submit_button)
        actions.perform()
        time.sleep(10)
