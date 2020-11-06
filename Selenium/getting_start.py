from selenium import webdriver

web = webdriver.Chrome('C:/chromedriver.exe')

web.get('https://github.com/login')

username = 'your_username'
password = 'your_password'

userfield = web.find_element_by_id('login_field')
userfield.send_keys(username)

passfield = web.find_element_by_id('password')
passfield.send_keys(password)

signinbtn = web.find_element_by_name('commit')
signinbtn.click()

