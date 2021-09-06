import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# initialising chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html'
driver.get(URL)
time.sleep(1)

# assigning test data
full_asci_table = '!"#$%&' + "'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

# gathering submit button,
submit_button = driver.find_element_by_id('submit')


def get_ascii():
    """gathering the value of the full ascii table"""
    return driver.find_elements_by_xpath('//div[@class="flex-child"]/p')[2].text


def get_char():
    """gathering char value"""
    return driver.find_element_by_id('chr').text


def get_op():
    """gathering oparation sigh"""
    return driver.find_element_by_id('op').text


def get_number():
    """gathering the number to modify with"""
    return int(driver.find_element_by_id('num').text)


def get_result():
    """gathering the result value"""
    return driver.find_element_by_id('result').text


def get_index(char):
    """gathering the index of a character"""
    return full_asci_table.index(char)


def test_tc01_appears_correctly():
    """
    Helyesen betöltődik az applikáció:
    Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
    !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
    """
    assert get_ascii() == full_asci_table


def test_tc02_valid_operation_values():
    """
    Megjelenik egy érvényes művelet:
    chr megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
    op mező vagy + vagy - karaktert tartlamaz
    num mező egy egész számot tartalamaz
    """
    assert get_char() in full_asci_table
    assert get_op() in '+-'
    assert isinstance(get_number(), int)


def test_t03_checking_calculated_result():
    """
    Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
    A megjelenő chr mezőben lévő karaktert kikeresve a táblában
    Ha a + művelet jelenik meg akkor balra lépve ha a - akkor jobbra lépve
    A num mezőben megjelenő mennyiségű karaktert
    az result mező helyes karaktert fog mutatni
    """
    submit_button.click()
    time.sleep(0.5)
    if get_op() == '+':
        assert get_index(get_char()) + get_number() == get_index(get_result())
    elif get_op() == '-':
        assert get_index(get_char()) - get_number() == get_index(get_result())
