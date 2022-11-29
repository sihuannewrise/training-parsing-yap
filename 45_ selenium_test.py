from time import sleep

from selenium import webdriver
# Импортируем классы для Chrome. Если у вас другой браузер - измените импорт.
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Если у вас установлен другой браузер - импортируйте нужный драйвер.
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import IEDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.opera import OperaDriverManager

DJANGO_URL = 'http://51.250.32.149/'
USERNAME = 'test_parser_user'
PASSWORD = 'testpassword'
PAUSE_DURATION_SECONDS = 1

if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(DJANGO_URL)
    driver.maximize_window()
    sleep(PAUSE_DURATION_SECONDS)

    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(USERNAME)
    sleep(PAUSE_DURATION_SECONDS)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(PASSWORD)
    sleep(PAUSE_DURATION_SECONDS)

    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()
    sleep(PAUSE_DURATION_SECONDS)

    driver.save_screenshot('screenshot.png')
    sleep(PAUSE_DURATION_SECONDS)

    first_post = driver.find_element(By.CLASS_NAME, 'card-text')
    print(first_post.text)
    driver.quit()
