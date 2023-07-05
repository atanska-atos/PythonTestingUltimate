import unittest
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
import sys


class BigPage(unittest.TestCase):

    IDNAME1 = "et_pb_contact_name_0"

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://ultimateqa.com/complicated-page")
        self.driver.implicitly_wait(3)

    def testButtons(self):
        button_list = self.driver.find_elements_by_class_name("et_pb_button_module_wrapper")
        self.assertEqual(12, len(button_list))

    def testLinks(self):
        twitter_links = self.driver.find_elements_by_class_name("et-social-twitter")
        facebook_links = self.driver.find_elements_by_class_name("et-social-facebook")
        self.assertEqual(len(twitter_links), len(facebook_links))

    def testTextBoxName(self):
        namebox = self.driver.find_element_by_id(self.IDNAME1)
        name = input("type your name: ")
        namebox.send_keys(name)
        self.driver.implicitly_wait(3)
        name_value = namebox.get_attribute("value")
        self.assertEqual(name, name_value)

    def testTextBoxEmail(self):
        emailbox = self.driver.find_element_by_id("et_pb_contact_email_0")
        email = input("type your email address: ")
        emailbox.send_keys(email)
        self.driver.implicitly_wait(3)
        email_value = emailbox.get_attribute("value")
        self.assertRegex(email_value, "[@*.com]")

    def testMessage(self):
        message = self.driver.find_element_by_id("et_pb_contact_message_0")
        message_value = input("type message: ")
        message.send_keys(message_value)
        self.assertNotRegex(message.get_attribute("value"), r'[ąęćśżźół]')

    def testSubmit(self):
        expression = self.driver.find_element_by_class_name("et_pb_contact_captcha_question").text
        result = eval(expression)
        self.driver.find_element_by_xpath("//*[@id=\"et_pb_contact_form_0\"]/div[2]/form/div/div/p/input").send_keys(
            result)
        self.driver.find_element_by_xpath("//*[@id=\"et_pb_contact_form_0\"]/div[2]/form/div/button").click()

    def submit(self):
        print("do it")
        self.driver.find_element_by_name("et_builder_submit_button")
        self.driver.implicitly_wait(3)
        self.driver.back()
        self.driver.implicitly_wait(3)

    def testLogin(self):
        login_box = self.driver.find_element_by_id("user_login_64a5221b1d747")
        login_value = input("type your login: ")
        login_box.send_keys(login_value)
        login = login_box.get_attribute("value")
        self.assertTrue(login)

        password_box = self.driver.find_element_by_id("user_pass_64a5221b1d747")
        password_value = input("type your password: ")
        password_box.send_keys(password_value)
        password = password_box.get_attribute("value")
        self.assertTrue(password)

        self.submit()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        BigPage.IDNAME1 = sys.argv.pop()
        BigPage.IDNAME2 = sys.argv.pop()
        BigPage.IDNAME3 = sys.argv.pop()
        BigPage.IDEMAIL1 = sys.argv.pop()
        BigPage.IDEMAIL2 = sys.argv.pop()
        BigPage.IDEMAIL3 = sys.argv.pop()
        BigPage.IDMESS1 = sys.argv.pop()
        BigPage.IDMESS2 = sys.argv.pop()
        BigPage.IDMESS3 = sys.argv.pop()
        BigPage.IDLOGIN1 = sys.argv.pop()
        BigPage.IDLOGIN2 = sys.argv.pop()
    unittest.main()

