
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# MyAccount=driver.find_element_by_partial_link_text("My Account").click()
# RegisterEmail=driver.find_element_by_id("reg_email")
# RegisterEmail.send_keys("Veseliy_brat@mail.ru")
# RegisterPassword=driver.find_element_by_id("reg_password")
# RegisterPassword.send_keys("1QWerty1993!")
# RegisterBtn = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((By.NAME, "register")))
# RegisterBtn1=driver.find_element_by_name("register").click()

##########################################################################

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")
MyAccount=driver.find_element_by_partial_link_text("My Account").click()
LoginEmail=driver.find_element_by_id("username")
LoginEmail.send_keys("Veseliy_brat@mail.ru")
LoginPassword=driver.find_element_by_id("password")
LoginPassword.send_keys("1QWerty1993!")
LoginBtn=driver.find_element_by_xpath("//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
LogOut=driver.find_element_by_partial_link_text("Logout")
LogOutCheck = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                    (By.PARTIAL_LINK_TEXT, "Logout")))