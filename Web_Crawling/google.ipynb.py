from selenium import webdriver 
executable_path = '/usr/local/bin/chromedriver' 
browser = webdriver.Chrome(executable_path = executable_path) 
browser.get('https://www.google.com')