import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# initialising chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html'
driver.get(URL)
time.sleep(1)

# assigning test data
test_data = [['', ''], ['2', '3', '10'], ['', '', 'NaN']]

# gathering the needful inputs, result, and submit button
a = driver.find_element_by_id('a')
b = driver.find_element_by_id('b')
c = driver.find_element_by_id('result')
submit_button = driver.find_element_by_id('submit')


def clearing_and_fulfill(a_value, b_value):
    """Clearing input fields, and filling with test data"""
    a.clear()
    b.clear()
    a.send_keys(a_value)
    time.sleep(0.5)
    b.send_keys(b_value)
    time.sleep(0.5)


def test_tc01_checking_appearance():
    """Helyesen jelenik meg az applikáció betöltéskor:
    a: <üres>
    b: <üres>
    c: <nem látszik>
    """
    assert a.text == test_data[0][0]
    assert b.text == test_data[0][1]
    assert not c.is_displayed()


def test_tc02_valid_calculation():
    """
    Számítás helyes, megfelelő bemenettel
    a: 2
    b: 3
    c: 10
    """
    clearing_and_fulfill(test_data[1][0], test_data[1][1])
    submit_button.click()
    time.sleep(0.5)
    assert c.text == test_data[1][2]


def test_tc03_invalid_values():
    """
    Üres kitöltés:
    a: <üres>
    b: <üres>
    c: NaN
    """
    clearing_and_fulfill(test_data[2][0], test_data[2][1])
    submit_button.click()
    time.sleep(0.5)
    assert c.text == test_data[2][2]
