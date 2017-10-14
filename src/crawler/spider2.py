from selenium import webdriver
import csv, operator
#import numpy as np
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

chromepath = "../../selenium/webdriver/chrome/chromedriver.exe"


driver = webdriver.Chrome(chromepath)
driver.get("https://www.sofascore.com/es/levante-espanyol/ogbsZgb")
driver.find_element_by_xpath("//li[@class='nav__item hidden-mobile']").click()
header = driver.find_element_by_xpath("//table[@class='table table--statistics js-sorter-body sort-by-rating']//thead")
header = header.text.replace('\n', ',')[4:]
player_names = driver.find_elements_by_xpath("//table[@class='table table--statistics js-sorter-body sort-by-rating']//td[@class='u-tL ff-medium player-stat-player-name']")
players = driver.find_elements_by_xpath("//table[@class='table table--statistics js-sorter-body sort-by-rating']//tr")

p_names = driver.find_elements_by_xpath("//table[@class='table table--statistics js-sorter-body sort-by-rating']//tr[@class='u-tL ff-medium player-stat-player-name']") item-row item-row--fancy

df = pd.DataFrame
with open('stats.csv', 'w') as output_file:
    wr = csv.writer(output_file, delimiter=',', lineterminator='\n')
    wr.writerow(header.split(','))
    first = True
    for player_name, player in zip(player_names, players):
        data = list()
        if not first:
            data.insert(0, player_name.text)
            for element in player.text.split(' ')[-9:]:
                data.append(element)
            wr.writerow(data)
        else:
            first = False

data = pd.read_csv('stats.csv', encoding='cp1250')
print("FIRST ROW: ", data.iloc[0])
# for column in data.columns:
#     if '(' in column or ')' in column:
#         print("COOL")