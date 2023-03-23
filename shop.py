# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# MyAccount=driver.find_element_by_partial_link_text("My Account").click()
# LoginEmail=driver.find_element_by_id("username")
# LoginEmail.send_keys("Veseliy_brat@mail.ru")
# LoginPassword=driver.find_element_by_id("password")
# LoginPassword.send_keys("1QWerty1993!")
# LoginBtn=driver.find_element_by_xpath("//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
# Shop=driver.find_element_by_partial_link_text("Shop").click()
# Html5Forms=driver.find_element_by_xpath("//*[@id='content']/ul/li[3]/a[1]/img").click()
# Html5FormsChek = driver.find_element_by_css_selector(".product_title.entry-title")
# Html5Chek = Html5FormsChek.text
# assert Html5Chek =="HTML5 Forms"
# print("заголовок книги = HTML5 Forms")
import time

##########################################################################

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# MyAccount=driver.find_element_by_partial_link_text("My Account").click()
# LoginEmail=driver.find_element_by_id("username")
# LoginEmail.send_keys("Veseliy_brat@mail.ru")
# LoginPassword=driver.find_element_by_id("password")
# LoginPassword.send_keys("1QWerty1993!")
# LoginBtn=driver.find_element_by_xpath("//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
# Shop=driver.find_element_by_partial_link_text("Shop").click()
# HTMLCategory=driver.find_element_by_xpath("//*[@id='woocommerce_product_categories-2']/ul/li[2]/a").click()
# Check3=driver.find_element_by_xpath("//*[@id='woocommerce_product_categories-2']/ul/li[2]/span")
# Check4= Check3.text
# assert Check4 =="(2)"
# print("3 товара в категории")

##########################################################################

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# MyAccount=driver.find_element_by_partial_link_text("My Account").click()
# LoginEmail=driver.find_element_by_id("username")
# LoginEmail.send_keys("Veseliy_brat@mail.ru")
# LoginPassword=driver.find_element_by_id("password")
# LoginPassword.send_keys("1QWerty1993!")
# LoginBtn=driver.find_element_by_xpath("//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
# Shop=driver.find_element_by_partial_link_text("Shop").click()
# Select1 = driver.find_element_by_class_name("orderby")
# SelectDefault = Select1.get_attribute("value")
# if SelectDefault == 'menu_order':
#     print("По умолчанию default sorting")
# else:
#     print("Another...")
# SortElement = driver.find_element_by_class_name("orderby")
# Sort1 =Select(SortElement)
# Sort1.select_by_value("price-desc")
# Select2 = driver.find_element_by_class_name("orderby")
# SelectDefault1 = Select2.get_attribute("value")
# if SelectDefault1 == 'price-desc':
#     print("в селекторе выбран вариант сортировки по цене от большей к меньшей")
# else:
#     print("Another...")

##########################################################################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# MyAccount=driver.find_element_by_partial_link_text("My Account").click()
# LoginEmail=driver.find_element_by_id("username")
# LoginEmail.send_keys("Veseliy_brat@mail.ru")
# LoginPassword=driver.find_element_by_id("password")
# LoginPassword.send_keys("1QWerty1993!")
# LoginBtn=driver.find_element_by_xpath("//*[@id='customer_login']/div[1]/form/p[3]/input[3]").click()
# Shop=driver.find_element_by_partial_link_text("Shop").click()
# AndroidQSG=driver.find_element_by_partial_link_text("Android Quick Start Guide").click()
# OldPrice=driver.find_element_by_css_selector("div>p>del>span")
# OldPrice2=OldPrice.text
# assert OldPrice2 == "₹600.00"
# print("OK")
# NewPrice=driver.find_element_by_css_selector("div>.price>ins")
# NewPrice2=NewPrice.text
# assert NewPrice2 == "₹450.00"
# print("OK")
# Book =WebDriverWait(driver,5).until(
#     EC.element_to_be_clickable((By.XPATH,"//*[@id='product-169']/div[1]/a/img")))
# Book.click()
# Close =WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR,".pp_close")))
# Close.click()

##########################################################################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# Shop=driver.find_element_by_partial_link_text("Shop").click()
# MasteringJS=driver.find_element_by_partial_link_text("Mastering JavaScript").click()
# AddBasket=driver.find_element_by_css_selector(".single_add_to_cart_button.button.alt").click()
# Basket=driver.find_element_by_css_selector(".cartcontents")
# Basket_chek = Basket.text
# assert Basket_chek== "1 Item"
# Price=driver.find_element_by_css_selector(".amount")
# Basket_chek2 = Price.text
# assert Basket_chek2=="₹350.00"
# Basket3=driver.find_element_by_css_selector(".wpmenucart-contents").click()
# SubTotal= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/table/tbody/tr[1]/td"),
#                                  "₹350.00"))
# Total= WebDriverWait(driver, 5).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr>td>strong>span"),
#                                  "₹357.00"))

##########################################################################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# Shop=driver.find_element_by_partial_link_text("Shop").click()
# driver.execute_script("window.scrollBy(0, 800);")
# MasteringJS=driver.find_element_by_partial_link_text("Mastering JavaScript").click()
# AddBasket=driver.find_element_by_css_selector(".single_add_to_cart_button.button.alt").click()
# time.sleep(5)
# Basket3=driver.find_element_by_css_selector(".wpmenucart-contents").click()
# DeleteBook=driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[1]/a").click()
# Undo=driver.find_element_by_partial_link_text("Undo?").click()
# Quantity = driver.find_element_by_css_selector(".input-text.qty.text").clear()
# Quantity1 = driver.find_element_by_css_selector(".input-text.qty.text")
# Quantity1.send_keys("3")
# UpdateBasket=driver.find_element_by_name("update_cart").click()
# Quantity2 = driver.find_element_by_css_selector(".input-text.qty.text")
# Quantity_check=Quantity2.get_attribute("value")
# assert Quantity_check=="3"
# time.sleep(4)
# ApplyCoupon=driver.find_element_by_name("apply_coupon").click()
# PeaCouponCode=driver.find_element_by_css_selector(".woocommerce-error")
# PeaCouponCode1=PeaCouponCode.text
# assert PeaCouponCode1=="Please enter a coupon code."

##########################################################################
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")
Shop=driver.find_element_by_partial_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 800);")
MasteringJS=driver.find_element_by_partial_link_text("Mastering JavaScript").click()
AddBasket=driver.find_element_by_css_selector(".single_add_to_cart_button.button.alt").click()
time.sleep(5)
Basket3=driver.find_element_by_css_selector(".wpmenucart-contents").click()
ProceedToCheckout =WebDriverWait(driver,5).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR,".checkout-button.button.alt.wc-forward")))
ProceedToCheckout.click()
FirstName=WebDriverWait(driver,5).until(
     EC.element_to_be_clickable((By.ID,"billing_first_name")))
FirstName.send_keys("Vladimir")
LastName=driver.find_element_by_id("billing_last_name")
LastName.send_keys("Veselov")
Email=driver.find_element_by_id("billing_email")
Email.send_keys("qwerty1@mail.ru")
Phone=driver.find_element_by_id("billing_phone")
Phone.send_keys("12345678901")
#Country1=driver.find_element_by_id()
time.sleep(4)
Country=driver.find_element_by_id("select2-chosen-1").click()
Country1=driver.find_element_by_id("s2id_autogen1_search")
Country1.send_keys("Russia")
time.sleep(4)
Country3=driver.find_element_by_id("select2-results-1").click()
Adress=driver.find_element_by_id("billing_address_1")
Adress.send_keys("assadasdasd")
Adress2=driver.find_element_by_id("billing_address_2")
Adress2.send_keys("asdasd123")
Town=driver.find_element_by_id("billing_city")
Town.send_keys("Kaliningrad")
State=driver.find_element_by_id("billing_state")
State.send_keys("asdasd")
PostCode=driver.find_element_by_id("billing_postcode")
PostCode.send_keys("123123")
time.sleep(5)
CheckPay=driver.find_element_by_id("payment_method_cheque").click()
driver.execute_script("window.scrollBy(0, 800);")
PlaceOrder=driver.find_element_by_id("place_order").click()
EC1= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
                                 "Thank you. Your order has been received."))
EC2= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.XPATH, "//*[@id='page-35']/div/div[1]/table[1]/tfoot/tr[3]/td"),
                                 "Check Payments"))

