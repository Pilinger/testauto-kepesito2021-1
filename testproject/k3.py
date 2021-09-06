import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# initialising chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html'
driver.get(URL)
time.sleep(1)

# assigning test data
test_data = ['abcd1234', 'teszt233@', 'abcd']
expected_results = ['', 'Only a-z and 0-9 characters allewed.', 'Title should be at least 8 characters; you entered 4.']


def clear_and_fill_input(data):
    title = driver.find_element_by_id('title')
    title.clear()
    time.sleep(0.5)
    title.send_keys(data)
    time.sleep(0.5)


def get_error_message():
    return driver.find_element_by_xpath('//span[contains(@class, "error")]')


def test_tc01_valid_data():
    """
    Helyes kitöltés esete:
    title: abcd1234
    Nincs validációs hibazüzenet
    """
    clear_and_fill_input(test_data[0])
    error_message = get_error_message()
    time.sleep(0.5)
    assert error_message.text == expected_results[0]


def test_tc02_illegal_data():
    """
    Illegális karakterek esete:
    title: teszt233@
    Only a-z and 0-9 characters allewed.
    """
    clear_and_fill_input(test_data[1])
    error_message = get_error_message()
    time.sleep(0.5)
    # failed test due to test_data ends with '.', though error message does not have '.' at the end
    # illegal test data and error message contains end word 'allewed', its written 'allowed' correctly
    assert error_message.text == expected_results[1]


def test_tc03_short_string():
    """
    Tul rövid bemenet esete:
    title: abcd
    Title should be at least 8 characters; you entered 4.
    """
    clear_and_fill_input(test_data[2])
    error_message = get_error_message()
    time.sleep(0.5)
    assert error_message.text == expected_results[2]
