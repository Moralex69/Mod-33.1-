# Тесты группы "Авторизация. Позитивные тесты" - вход в ЛК

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.setting import *
import time


def test_auth_by_phone(web_browser):
    """ Тест-кейс AT-001: авторизация по номеру телефона """

    page = AuthPage(web_browser)

    # Переходим на таб Мобильный телефон
    page.swich_tab(page.tab_phone)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(valid_phone)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)


    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Явное ожидание загрузки элемента div.home-container - внешний контейнер в ЛК
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.home-container'))
    )

    print(web_browser.current_url)
    print(f'h2.user-name[title="{valid_username}"]')
    # Проверка
    assert link_lk in web_browser.current_url, f"AT-001 failed: Текущая ссылка {web_browser.current_url} не содержит account_b2"
    assert web_browser.find_element(By.CSS_SELECTOR, f'h2.user-name[title="{valid_username}"]'), f"AT-001 failed: На странице нет элемента {valid_username}"


def test_auth_by_email(web_browser):
    """ Тест-кейс AT-002: авторизация по емейлу """

    page = AuthPage(web_browser)

    # Переходим на таб Почта
    page.swich_tab(page.tab_email)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(valid_email)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Явное ожидание загрузки элемента div.home-container - внешний контейнер в ЛК
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.home-container'))
    )

    print(web_browser.current_url)
    print(f'h2.user-name[title="{valid_username}"]')
    # Проверка
    assert link_lk in web_browser.current_url, f"AT-002 failed: Текущая ссылка {web_browser.current_url} не содержит account_b2"
    assert web_browser.find_element(By.CSS_SELECTOR, f'h2.user-name[title="{valid_username}"]'), f"AT-002 failed: На странице нет элемента {valid_username}"


@pytest.mark.skip("При регистрации не был получен логин, позитивный тест невозможен")
def test_auth_by_login(web_browser):
    """ Тест-кейс AT-003: авторизация по логину """

    page = AuthPage(web_browser)

    # Переходим на таб Логин
    page.swich_tab(page.tab_login)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(valid_login)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Явное ожидание загрузки элемента div.home-container - внешний контейнер в ЛК
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.home-container'))
    )

    print(web_browser.current_url)
    print(f'h2.user-name[title="{valid_username}"]')
    # Проверка
    assert link_lk in web_browser.current_url, f"AT-003 failed: Текущая ссылка {web_browser.current_url} не содержит account_b2"
    assert web_browser.find_element(By.CSS_SELECTOR, f'h2.user-name[title="{valid_username}"]'), f"AT-003 failed: На странице нет элемента {valid_username}"


@pytest.mark.skip("Без подключения услуги нет лицевого счета, позитивный тест невозможен")
def test_auth_by_ls(web_browser):
    """ Тест-кейс AT-004: авторизация по лицевому счету """

    page = AuthPage(web_browser)

    # Переходим на таб Лицевой счет
    page.swich_tab(page.tab_ls)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(valid_ls)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Явное ожидание загрузки элемента div.home-container - внешний контейнер в ЛК
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.home-container'))
    )

    print(web_browser.current_url)
    print(f'h2.user-name[title="{valid_username}"]')
    # Проверка
    assert link_lk in web_browser.current_url, f"AT-004 failed: Текущая ссылка {web_browser.current_url} не содержит account_b2"
    assert web_browser.find_element(By.CSS_SELECTOR, f'h2.user-name[title="{valid_username}"]'), f"AT-004 failed: На странице нет элемента {valid_username}"


@pytest.mark.parametrize(("username, username_title"),
                            [
                                (valid_email, u"Почта"),
                                #(valid_login, u"Логин"),
                                #(valid_ls, u"Лицевой счёт"),
                                (valid_phone, u"Телефон")
                            ],
                            ids= [
                                'By email',
                                #'By login',
                                #"By LS",
                                "By phone"]
                         )
def test_auth_in_any_tab(username, username_title, web_browser):
    """ Тест-кейс AT-005: авторизация по любому username без смены таба """

    page = AuthPage(web_browser)

    # Если проверяем ввод телефона, переходим предварительно на таб Почта, т.к. таб Телефон открыт по умолчанию
    if username_title == "Телефон":
        page.swich_tab(page.tab_email)

    # Вводим логин/пароль
    page.enter_username(username)
    page.enter_pass(valid_password)

    print(username_title)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Явное ожидание загрузки элемента div.home-container - внешний контейнер в ЛК
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.home-container'))
    )

    print(web_browser.current_url)
    print(f'h2.user-name[title="{valid_username}"]')
    # Проверка
    assert link_lk in web_browser.current_url, f"AT-005 failed: Текущая ссылка {web_browser.current_url} не содержит account_b2"
    assert web_browser.find_element(By.CSS_SELECTOR, f'h2.user-name[title="{valid_username}"]'), f"AT-005 failed: На странице нет элемента {valid_username}"