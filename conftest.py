from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")

    parser.addoption('--language', action='store', default='en',
                     help="Choose language: '--language=en' or '--language=ru'")


# это добавит возможность писать параметры в коммандной строке:
# pytest -s -v --browser_name=firefox --language=ru


# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
# parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
# Можно задать значение параметра по умолчанию,
# чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:

# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def browser(request):
    browser_name = request.config.getoption(
        "browser_name")  # получаем параметр командной строки browser_name
    user_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        print("\nstart Сhrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", user_language)
        print("\nstart Firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    # time.sleep(2)
    browser.quit()

# pytest -s -v --browser_name=chrome test_parser.py
# pytest -s -v --browser_name=firefox test_parser.py

# pip freeze > requirements.txt   Эта команда сохранит все версии пакетов в специальный файл requirements.txt.
# pip install -r requirements.txt  В свежем окружении все пакеты установлены одной командой!
