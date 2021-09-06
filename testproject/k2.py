import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# initialising chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html '
driver.get(URL)
time.sleep(1)

# assighing test data
all_colors = driver.find_element_by_id('allcolors').text.replace('"', '').split(', ')
possilbe_result = ['Correct!', 'Incorrect!']
blank_text = '[     ]' + ' == ' + '[     ]'

# assigning buttons, test color, random color
start_button = driver.find_element_by_id('start')
stop_button = driver.find_element_by_id('stop')
random_color_name = driver.find_element_by_id('randomColorName')
random_color = driver.find_element_by_id('randomColor')
test_color_name = driver.find_element_by_id('testColorName')
test_color = driver.find_element_by_id('testColor')


def get_result():
    return driver.find_element_by_id('result').text


def test_tc01_checking_appearance():
    """
    Helyesen jelenik meg az applikáció betöltéskor:
    Alapból egy random kiválasztott szín jelenik meg az == bal oldalanán.
    A jobb oldalon csak a [ ] szimbólum látszik. <szín neve> [ ] == [ ]
    """
    assert random_color_name.text in all_colors
    appeared_values = random_color_name.text + random_color.text + ' == ' + test_color.text
    assert appeared_values == random_color_name.text + blank_text


def test_tc02_checking_start_and_stop():
    """
    El lehet indítani a játékot a start gommbal.
    Ha elindult a játék akkor a stop gombbal le lehet állítani.
    """
    assert start_button.is_enabled()
    start_button.click()
    time.sleep(3)
    assert stop_button.is_enabled()
    stop_button.click()
    time.sleep(0.5)


def test_tc03_checking_result():
    """
    Eltaláltam, vagy nem találtam el.

    Ha leállítom a játékot két helyes működés van,
    ha akkor állítom épp le amikor a bal és a jobb oldal ugyan azt a színt tartalmazza,
    akkor a Correct! felirat jelenik meg.
    Ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az Incorrect! felirat kell megjelenjen.
    """
    start_button.click()
    time.sleep(4)
    stop_button.click()
    time.sleep(0.5)
    result_color_name = driver.find_element_by_id('testColorName')
    result = get_result()
    if random_color_name.text == result_color_name.text:
        assert result() == possilbe_result[0]
    else:
        assert result == possilbe_result[1]
