import io
from itertools import count
from requests import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from PIL import Image

# TO DO LIST
# 1: Make the page scroll down to get more images to download

COUNT = 0

def return_first_image(driver):
    time.sleep(1)
    llist1 = []
    for x in driver.find_elements(By.TAG_NAME, 'a'):
        if "/pin/" in x.get_attribute("href"):
            llist1.append(x.get_attribute("href"))
    llist2 = []
    for i in llist1:
        if i not in llist2:
            llist2.append(i)
    return llist2

def get_image_link(driver):
    var1 = driver.find_elements(By.TAG_NAME, 'img')
    arr = []
    for x in var1:
        arr.append(x.get_attribute("src"))
    return arr[0]

def save_image(downloadPath, url, fileName):
    imageContent = requests.get(url).content
    imageFile = io.BytesIO(imageContent)
    image = Image.open(imageFile)
    filePath = downloadPath + fileName
    with open(filePath, "wb") as f:
        image.save(f, "JPEG")

def search_image(driver):
    for x in return_first_image(driver):
        time.sleep(10)
        driver.get(x)
        time.sleep(5)
        try:
            save_image("", get_image_link(driver), increment() + "Image.jpg")
            print("-> Success Image Downloaded")
        except:
            print("-> Error Downloading Image")
    print("-> Finished Downloading Images")

def increment():
    global COUNT
    COUNT = COUNT+1
    count2 = str(COUNT)
    return count2

def __main__():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://www.pinterest.co.uk/search/pins/?q=programming%20posters&rs=typed&term_meta[]=programming%7Ctyped&term_meta[]=posters%7Ctyped')
    search_image(driver)
    time.sleep(500)

__main__()