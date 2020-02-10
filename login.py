from selenium import webdriver

class login():
    #TODO read from file creds from file
    BASE_URL='https://www.djcity.com'

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(self.BASE_URL)

        title = driver.title

        print ("title: {}".format(title))


thing = login()
thing.test()
