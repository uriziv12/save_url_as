import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui

f = open("links_s.txt", "r")
links = f.readlines()


def extract_file_name_from_url(url):
    return url.split("=")[-1].strip()


def save_url_as_mhtml(url, filename):
    driver = webdriver.Chrome()
    driver.get(url)

    # wait until body is loaded
    WebDriverWait(driver, 60).until(visibility_of_element_located((By.TAG_NAME, 'body')))
    time.sleep(1)

    # open 'Save as...' to save html and assets
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    if filename != '':
        pyautogui.typewrite(filename)

    # Sequence to save as mhtml
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('up')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(3)


for url_i in links:
    filename_i = extract_file_name_from_url(url=url_i)
    save_url_as_mhtml(url=url_i, filename=filename_i)
    print("URL {} saved at {}".format(url_i, filename_i))
    time.sleep(5)
