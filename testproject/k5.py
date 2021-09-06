import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# initialising chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html'
driver.get(URL)
time.sleep(1)

# gathering the buttons
init_button = driver.find_element_by_id('Init')
play_button = driver.find_element_by_id('spin')


def get_bingo():
    """gathering the bingo elements"""
    return driver.find_elements_by_xpath('//td')


def get_list():
    """gathering the list elements"""
    return driver.find_elements_by_xpath('//li/input[@type="checkbox"]')


def test_tc01_checking_appearance():
    """
    Az applikáció helyesen megjelenik:
    A bingo tábla 25 darab cellát tartalmaz
    A számlista 75 számot tartalmaz
    """
    assert len(get_bingo()) == 25
    assert len(get_list()) == 75


def test_tc02_play_till_first_bingo():
    """
    Bingo számok ellenőzrzése:
    Addig nyomjuk a play gobot amíg az első bingo felirat meg nem jelenik
    Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről
    tényleg a már kihúzott számok közül kerültek-e ki
    """
    while not driver.find_element_by_xpath('//ul[@id="messages"]/li').is_displayed():
        play_button.click()
        time.sleep(0.5)


def test_tc03_init_new_game():
    """
    Új játékot tudunk indítani
    az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
    új bingo szelvényt kapunk más számokkal.
    """
    init_button.click()
