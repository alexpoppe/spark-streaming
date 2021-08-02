from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

# set the directories
CODE_DIR = os.getcwd()
WORK_DIR = CODE_DIR.replace("/code", "")

# get the driver to run chrome
driver = webdriver.Chrome(executable_path=WORK_DIR+"/driver/chromedriver")
driver.get("https://www.instagram.com")

# click on "Accept cookies"
elem = driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]')
elem.click()

# log in with the account that I made for this project
username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))

username.clear()
password.clear()
username.send_keys("epitaproject")
password.send_keys("alex1709")

time.sleep(2)

# log in and click on "not now"
log_in = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()

# Go through the hashtags and get the amount of posts per hashtag
hashtags = ["photography", "food", "love"]
while True:
    n_posts = []

    for hashtag in hashtags:
        # go to the page of the hashtag
        page = driver.get("https://www.instagram.com/explore/tags/" + hashtag)

        # get the number of posts
        number = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div/div[2]/span/span')
        n_posts.append(number.text)  

    # write the numbers to a file
    with open(WORK_DIR+'/data/hashtags.txt', 'w') as f:
        for name, number in list(zip(hashtags, n_posts)):
            f.write(str(name) + ': ' + str(number) + '\n')
            print(str(name) + ': ' + str(number) + '\n')

    # wait for 5 seconds
    time.sleep(5)
