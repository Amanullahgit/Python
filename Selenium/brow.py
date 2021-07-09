from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_experimental_option('detach', True)

for i in range(10):
    web = webdriver.Chrome('C:/chromedriver.exe',options=option)
    web.get('https://www.youtube.com/watch?v=vVCYVNxW4ic&list=UU04DF2BkixPPGKszkGx3WQw&index=1')

