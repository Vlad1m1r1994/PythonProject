import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 750);")
Selenium_Ruby=driver.find_element_by_partial_link_text('Selenium Ruby').click()
driver.execute_script("window.scrollBy(0, 750);")
time.sleep(3)
Reviews=driver.find_element_by_xpath("//*[@id='product-160']/div[3]/ul/li[2]/a").click()
Star5=driver.find_element_by_class_name('star-5').click()
ReviewField=driver.find_element_by_id('comment')
ReviewField.send_keys("Nice book!")
NameField=driver.find_element_by_id("author")
NameField.send_keys("Vladimir")
EmailField=driver.find_element_by_id("email")
EmailField.send_keys("sadasdd@mail.ru")
SubmitBtn=driver.find_element_by_id("submit")
SubmitBtn.click()
#SubmitBtn2=SubmitBtn.get_attribute("Value")
#Url="https://practice.automationtesting.in/wp-comments-post.php"
PageError = driver.find_element_by_id("error-page")
if SubmitBtn != PageError:
    print("есть такой комментарий")
else:
    print("нет такого комментария")

#driver.quit()