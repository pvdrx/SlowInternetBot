from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

PROMISED_DOWN = 250
PROMISED_UP = 250
CHROME_DRIVER_PATH = "C:\development\chromedriver.exe"
TWITTER_EMAIL = "jdbd@protonmail.com"
TWITTER_PASSWORD = "Melo159de"
s = Service(CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(6)
        speed_site = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                        'div[1]/a/span[4]')
        speed_site.click()
        sleep(120)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                       'div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/'
                                                       'span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                     'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/'
                                                     'span').text

        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        sleep(10)
        site = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                  'div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        site.click()
        sleep(10)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                   'div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                         'div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next_button.click()

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/'
                                                      'div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/'
                                                      'div[1]/input')
        password.send_keys(TWITTER_PASSWORD)

        sleep(3)

        login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                   'div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        login.click()
        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                           'div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/'
                                                           'div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/'
                                                           'div/div/div/div')
        tweet = f"Hey Mais Fibra, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}" \
                f"down/{PROMISED_UP}up?"

        tweet_compose.send_keys(tweet)
        sleep(3)
        tweet_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                         'div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]'
                                                         '/div/div/div[2]/div[3]')
        tweet_button.click()
        sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(s)
bot.get_internet_speed()
bot.tweet_at_provider()
