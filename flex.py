import time
import getpass
import os

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
 
chromedriver = repr(os.getcwd() + "\\chromedriver").replace("\\\\", "\\")

print(chromedriver)


class Registration(object):

    def __init__(self, login, password, secondpass):
        self.login = login
        self.password = password
        self.secondpass = secondpass

    def loginToAccount(self):
        baseurl = 'https://flexstudent.nu.edu.pk/login'
        options = Options()
        # options.add_argument('--disable-gpu')
        # options.add_argument("--disable-extensions")
        # options.add_experimental_option("detach", True)
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        mydriver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install(), options=options)
        mydriver.get(baseurl)
        actions = ActionChains(mydriver)
                                
        mydriver.find_element_by_id("UserID").send_keys(self.login)
        mydriver.find_element_by_xpath(
            '//*[@id="PIN"]/input').send_keys(self.password)
        mydriver.find_element_by_xpath("//p//input[@type='submit']").click()

        mydriver.find_element_by_id('answer').send_keys(self.secondpass)

        mydriver.find_element_by_xpath("//p//input[@type='submit']").click()

        mydriver.get(
            'https://flexstudent.nu.edu.pk/Student/CourseRegistration?dump=KicqbxFjLEz56%2B%2FX9dNCAw%3D%3D')

        time.sleep(1)

        mydriver.get(
            'https://flexstudent.nu.edu.pk/Student/CourseRegistration?dump=KicqbxFjLEz56%2B%2FX9dNCAw%3D%3D')

        time.sleep(1)
  
        mydriver.find_element_by_link_text(
            'Register, Drop and/or Add Classes').click()

        print('Please click submit and wait 5 seconds while CRNS get populated...')

        time.sleep(5)
        #enter your name of courses below

        mydriver.find_element_by_id("crn_id1").send_keys(crn1)

        mydriver.find_element_by_id("crn_id2").send_keys(crn2)

        mydriver.find_element_by_id("crn_id3").send_keys(crn3)

        mydriver.find_element_by_id("crn_id4").send_keys(crn4)

        mydriver.find_element_by_id("crn_id5").send_keys(crn5)


crn1 = '24415'
crn2 = '22962'
crn3 = '24414'
crn4 = '24744'
crn5 = '22516'

myuser = "19K-1069" # input('Enter GWID: ')
mypass =  getpass.getpass('Enter password: ')
mypass2 = mypass # getpass.getpass('Enter Second Password: ')

myobj = Registration(myuser, mypass, mypass2)
myobj.loginToAccount()
