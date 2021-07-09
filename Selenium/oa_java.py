from selenium import webdriver
import time
# user = input("Enter username: ")
# passw = input("Enter password: ")
user = "OA110266202"
passw = "salomon"
driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://myacademy.oracle.com/lmt/xlr8login.login?site=oa')





driver.find_element_by_id('inputUsername').send_keys(user)
driver.find_element_by_id('inputPassword').send_keys(passw)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login-page"]/div[2]/form/div/ul[3]/li/input').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/xlr8_stylesheet/div[4]/div[3]/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/a').click()   #java course
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/main/section[3]/div/div/section/div[2]/div[3]/div/div[2]/h4/a').click()      #learning path
time.sleep(2)

sections = [5, 6, 7, 8, 9, 11, 12, 13, 14, 15]
section_len = [2, 1, 4, 4, 3, 3, 2, 2, 2, 2]
#section 0
for j in range(10):
    for i in range(section_len[j]):
        element = driver.find_element_by_xpath(
            f'/html/body/xlr8_stylesheet/div[4]/div[3]/div[2]/div/div/div[{sections[j]}]/div[2]/div/div[{i + 1}]/div[2]/a')

        driver.execute_script('arguments[0].click();', element)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="col_left"]/div[2]/p/a').click()
        time.sleep(2)
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.close()
        time.sleep(2)
        new_window = driver.window_handles[0]
        driver.switch_to.window(new_window)
        driver.find_element_by_xpath('//*[@id="userCourseLPSContent"]/div/div/div[2]/a').click()