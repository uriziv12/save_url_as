import time
from selenium import webdriver

f = open("links_s.txt", "r")
links = f.readlines()


def extract_file_name_from_url(url):
    return url.split("=")[-1].strip() + ".html"


def save_url_as_html(url, filename):
    driver = webdriver.Chrome()
    driver.get(url)
    html_content = driver.page_source
    html_file = open(filename, "wt", encoding="utf-8")
    html_file.write(html_content)
    html_file.close()


for url_i in links:
    filename_i = extract_file_name_from_url(url=url_i)
    save_url_as_html(url=url_i, filename=filename_i)
    print("URL {} saved at {}".format(url_i, filename_i))
    time.sleep(5)
