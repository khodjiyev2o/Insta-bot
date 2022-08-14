from lib2to3.pgen2 import driver
import os
from pickle import TRUE

from re import S
from sre_constants import SUCCESS 
from selenium import webdriver
import os
import main.constants as const
from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException
import time 
import json
 
 





class Scraping(webdriver.Chrome):
    def __init__(self, driver_path=const.DRIVER_PATH, teardown=False):
        """options = webdriver.ChromeOptions()
        options.add_argument("start-maximized");
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")"""
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        super(Scraping, self).__init__(options=options)
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
            print("Exiting...")



    def land_first_page(self):
        self.get(const.BASE_URL)

    def authentication(self):
        login = self.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        password = self.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        login.send_keys('1517followers')
        password.send_keys('feyk0505')
        ent_btn = self.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
    def later(self):
        WebDriverWait(self,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')))
        later_btn = self.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        WebDriverWait(self,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')))
        not_now = self.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()


    def search(self,input):
        srch_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div/span")
        srch_btn.send_keys(input).submit()
