import time
import json
import os
import sys
from selenium import webdriver

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
print("script_directory: {}".format(script_directory))

f = open("links_s.txt", "r")
links = f.readlines()


def save_url_as_pdf(url):
    settings = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
    prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}

    profile = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),
               'savefile.default_directory': script_directory}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_experimental_option('prefs', profile)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.execute_script('window.print();')
    time.sleep(5)
    # driver.quit()


for url_i in links:
    save_url_as_pdf(url=url_i)
    print("URL {} saved".format(url_i))
    time.sleep(5)
