import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('c:/windows/system32/chromedriver.exe')
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():

   # Вводим email
   pytest.driver.find_element('id','email').send_keys('vasya@mail.com')

   # Вводим пароль
   pytest.driver.find_element('id','pass').send_keys('12345')

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element('css selector','button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   # ждем загрузки
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
   assert pytest.driver.find_element('tag name','h1').text == "PetFriends"

   # ждем загрузки
   pytest.driver.implicitly_wait(50)

   images = pytest.driver.find_element('css selector','.card-deck .card-img-top')
   names = pytest.driver.find_elements('css selector','.card-deck .card-title')
   descriptions = pytest.driver.find_elements('css selector','.card-deck .card-text')


   for i in range(len(names)):
   assert images.get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0