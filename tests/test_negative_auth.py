# Тесты группы "Авторизация. Негативные тесты" - вход в ЛК
# Проверка авторизации с пустым телефоном/емейлом/логином/ЛС
# Проверка авторизации с правильным телефоном/емейлом/логином/ЛС и пустым паролем
# Ввод некорректного номера телефона
# Ввод некорректного емейла
# Вход с верным телефоном/емейлом/логином/ЛС и неверным паролем
# Вход с неверным телефоном/емейлом/логином/ЛС и верным паролем


import pytest
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.setting import *
import time


@pytest.mark.parametrize("phone", ['', ' '], ids= ["Empty phone", "Space phone"])
def test_auth_by_empty_phone(phone, web_browser):
    """ Тест-кейс AT-006: попытка авторизации с пустым номером телефона """

    page = AuthPage(web_browser)

    # Переходим на таб Мобильный телефон
    page.swich_tab(page.tab_phone)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(phone)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    assert link_lk not in web_browser.current_url, f"AT-006 failed: Выполнен вход в ЛК"
    # Появляется надпись "Введите номер телефона"
    assert web_browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error").text == 'Введите номер телефона', "AT-006 failed: нет предупреждения о пустом номере телефона"


@pytest.mark.parametrize("email", ['', ' '], ids=["Empty email", "Space email"])
def test_auth_by_empty_email(email, web_browser):
    """ Тест-кейс AT-011: попытка авторизации с пустым адресом электронной почты """

    page = AuthPage(web_browser)

    # Переходим на таб Почта
    page.swich_tab(page.tab_email)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(email)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Введите адрес, указанный при регистрации"
    assert web_browser.find_element(By.CSS_SELECTOR,
                                    "span.rt-input-container__meta.rt-input-container__meta--error").text == 'Введите адрес, указанный при регистрации', f"AT-011 failed: нет предупреждения о пустом емейле"


@pytest.mark.parametrize("login", ['', ' '], ids= ["Empty login", "Space login"])
def test_auth_by_empty_login(login, web_browser):
    """ Тест-кейс AT-016: попытка авторизации с пустым логином """

    page = AuthPage(web_browser)

    # Переходим на таб Логин
    page.swich_tab(page.tab_login)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(login)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Введите логин, указанный при регистрации"
    assert web_browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error").text == 'Введите логин, указанный при регистрации', f"AT-016 failed: нет предупреждения о пустом логине"


@pytest.mark.parametrize("ls", ['', ' '], ids= ["Empty ls", "Space ls"])
def test_auth_by_empty_ls(ls, web_browser):
    """ Тест-кейс AT-018: попытка авторизации с пустым ЛС """

    page = AuthPage(web_browser)

    # Переходим на таб Логин
    page.swich_tab(page.tab_ls)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(ls)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Введите номер вашего лицевого счета"
    assert web_browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error").text == 'Введите номер вашего лицевого счета', f"AT-018 failed: нет предупреждения о пустом ЛС"


@pytest.mark.parametrize("username, passwd, test_num", [
                            (valid_phone, '', 'AT-007'),
                            (valid_phone, ' ', 'AT-007'),
                            (valid_email, '', 'AT-012'),
                            (valid_email, ' ', 'AT-012'),
                            (valid_login, '', 'AT-017'),
                            (valid_login, ' ', 'AT-017'),
                            (valid_ls, '', 'AT-019'),
                            (valid_ls, ' ', 'AT-019')
                        ], ids= [
                            "Phone: Empty password",
                            "Phone: Space password",
                            "Email: Empty password",
                            "Email: Space password",
                            "Login: Empty password",
                            "Login: Space password",
                            "LS: Empty password",
                            "LS: Space password"
                        ])
@pytest.mark.xfail(reason="Нереализовано")
def test_auth_by_username_and_empty_password(username, passwd, test_num, web_browser):
    """ Тест-кейс AT-007/AT-012/AT-017/AT-019: попытка авторизации с пустым паролем """

    page = AuthPage(web_browser)

    # Вводим логин/пароль
    page.enter_username(username)
    page.enter_pass(passwd)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Введите пароль"
    assert web_browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error").text == 'Введите пароль', f"{test_num} failed: Нет вывода сообщения 'Введите пароль'"


@pytest.mark.parametrize("username, test_num", [
                                ('+7(999)9999999', "AT-008"),
                                ("romashka2003@gmail.com", "AT-014")
                            ], ids= [
                                "Wrong phone number",
                                "Wrong email"
                            ]
                         )
def test_auth_by_wrong_phone(username, test_num, web_browser):
    """ Тест-кейс AT-008/AT-014: попытка авторизации неверным username и верным паролем"""

    page = AuthPage(web_browser)

    # Вводим логин/пароль
    page.enter_username(username)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        print("Captcha!!!")
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Неверный логин или пароль"
    assert web_browser.find_element(By.ID, "form-error-message").text == 'Неверный логин или пароль', f"{test_num} failed: Нет надписи 'Неверный логин или пароль'"


@pytest.mark.parametrize("username, passwd, test_num", [
                            (valid_phone, 'hjvfirf2003', 'AT-009'),
                            (valid_email, 'hjvfirf2003', 'AT-013'),
                        ], ids= [
                            "Phone: Wrong password",
                            "Email: Wrong password",
                        ])
def test_auth_by_wrong_password(username, passwd, test_num, web_browser):
    """ Тест-кейс AT-009 и AT-013: попытка авторизации верным username и неверным паролем"""

    page = AuthPage(web_browser)

    # Вводим логин/пароль
    page.enter_username(username)
    page.enter_pass(passwd)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        print("Captcha!!!")
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Неверный логин или пароль"
    assert web_browser.find_element(By.ID, "form-error-message").text == 'Неверный логин или пароль', f"{test_num} failed: Нет надписи 'Неверный логин или пароль'"


@pytest.mark.parametrize("phone", ['+7(977)561260'], ids= ["Not correct numb"])
def test_auth_by_bad_format_phone(phone, web_browser):
    """ Тест-кейс AT-010: попытка авторизации по номеру телефона в неверном формате"""

    page = AuthPage(web_browser)

    # Переходим на таб Мобильный телефон
    page.swich_tab(page.tab_phone)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(phone)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Введите номер телефона"
    assert web_browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error").text == 'Неверный формат телефона', f"AT-010 failed: Нет надписи 'Неверный логин или пароль'"


@pytest.mark.parametrize("email", ['romashkacool2003@gmail'], ids= ["Not correct email"])
def test_auth_by_bad_format_email(email, web_browser):
    """ Тест-кейс AT-015: попытка авторизации по емейлу в неверном формате"""

    page = AuthPage(web_browser)

    # Переходим на таб Почта
    page.swich_tab(page.tab_email)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(email)
    page.enter_pass(valid_password)

    # Проверка перехода на таб "Логин"
    assert web_browser.find_element(By.CSS_SELECTOR, "div.rt-tab.rt-tab--small.rt-tab--active").text == 'Логин', f"AT-015 failed: не перешли на таб 'Логин'"

    # python -m pytest -v --driver Chrome --driver-path C:\chromedriver_win32/chromedriver.exe tests/test_negative_auth.py
