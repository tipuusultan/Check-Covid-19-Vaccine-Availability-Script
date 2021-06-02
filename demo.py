from selenium import webdriver

driver = webdriver.Chrome('https://webchala.com/chromedriver.exe')
driver.get('https://www.instagram.com')


username = driver.find_element_by_name('username')
username.send_keys("tlyrics.in")

password = driver.find_element_by_name('password')
password.send_keys("FUCKINGpassword")

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login.click()


not_now = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
not_now.click()

not_now2 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
not_now2.click()


driver.get('https://www.instagram.com/p/CO3CG43DY8w/')

like = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
like.click()
