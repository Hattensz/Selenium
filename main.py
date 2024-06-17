from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")

email.send_keys("email@mail.com")
password.send_keys("123456", Keys.ENTER)

try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "codigo"))
    )

finally:
    table = pd.read_csv("produtos.csv")
    
    for row in table.index:
        code = driver.find_element(By.ID, "codigo")
        code.send_keys(table["codigo"][row])

        brand = driver.find_element(By.ID, "marca")
        brand.send_keys(table["marca"][row])

        type = driver.find_element(By.ID, "tipo")
        type.send_keys(table["tipo"][row])

        category = driver.find_element(By.ID, "categoria")
        category.send_keys(str(table["categoria"][row]))

        priceuni = driver.find_element(By.ID, "preco_unitario")
        priceuni.send_keys(str(table["preco_unitario"][row]))

        price = driver.find_element(By.ID, "custo")
        price.send_keys(str(table["custo"][row]))

        obsdata = table["obs"][row]
        if not pd.isna(obsdata):
            obs = driver.find_element(By.ID, "obs")
            obs.send_keys(obsdata)

        price.send_keys(Keys.ENTER)

    time.sleep(60)
    driver.quit()