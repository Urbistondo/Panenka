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
# navigate to the application home page
'''
driver.get("https://www.sofascore.com/es/torneo/futbol/spain/primera-division/8")
# matches = driver.find_elements_by_class_name("result")

round= driver.find_element_by_xpath("//label[@class='js-tournament-page-events-select-round radio-switch__item']")
round.click()
matches = driver.find_elements_by_xpath("//div[@class='js-event-list-tournament-events']//a")
cont= 0
for match in reversed(matches):
    cont = cont +1
    print()
    print(match.text)
    print()
    match.click()
    links=driver.find_elements_by_xpath("//a[@class='h-interactive js-event-link']")
 #   links=driver.find_elements_by_xpath("//a[@title='Abrir este partido en una nueva pestaña']")
    for link in links:
        print("LINKS")
        print(link.text)
        print()
        link.click()
    if cont==10:
        break


# //*[@id="tournament-fixture"]/tbody/tr[2]/td[5]/a

'''

def leer(final_df):
    header= driver.find_element_by_xpath("//table[@class='table table--statistics js-sorter-body sort-by-rating']//thead")
    print(header.text)
    vals= driver.find_elements_by_xpath("//table[@class='table table--statistics js-sorter-body sort-by-rating']//tbody")
    print("TYPE OF VALS: ", type(vals))
    final_df = pd.DataFrame(vals)
    return final_df

    ''' for val in vals:
        final_df= pd.DataFrame(val)
#            final_df= val.text
#        final_df = pd.merge(final_df, val.)
        print(val.text)
'''

driver.get("https://www.sofascore.com/es/levante-espanyol/ogbsZgb")
driver.find_element_by_xpath("//li[@class='nav__item hidden-mobile']").click()
#for estadistica in estadisticas:
#    estadistica.click()
#   break






final_df = pd.DataFrame
with open('estadisticas.csv', mode='w') as output_file:
    ##SUMARIO
    final_df = leer(final_df)
    secciones= driver.find_elements_by_xpath("//li[@class='nav__item ']//a")
    for seccion in secciones:
        seccion.click()
        final_df = pd.merge(final_df, leer(final_df))

    final_df.to_csv(output_file)

'''
##ATAQUE
ataques= driver.find_elements_by_xpath("//a[@class='js-squad-stats-groups-nav-tab player-stat-group-attack']")
for ataque in ataques:
    ataque.click()
    break
leer("ataque")
##DEFENSA
defensas= driver.find_elements_by_xpath("//a[@class='js-squad-stats-groups-nav-tab player-stat-group-defence']")
for defensa in defensas:
    defensa.click()
    break
leer("defensa")
##PASES
pases= driver.find_elements_by_xpath("//a[@class='js-squad-stats-groups-nav-tab player-stat-group-passing']")
for pase in pases:
    pase.click()
    break
leer("passing")
##DUELOS
duelos= driver.find_elements_by_xpath("//a[@class='js-squad-stats-groups-nav-tab player-stat-group-attack']")
for duelo in duelos:
    duelo.click()
    break
leer("duelos")
##PORTERO
porteros= driver.find_elements_by_xpath("//a[@class='js-squad-stats-groups-nav-tab player-stat-group-attack']")
for portero in porteros:
    portero.click()
    break
leer("portero")


'''


