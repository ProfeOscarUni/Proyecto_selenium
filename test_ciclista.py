import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import HtmlTestRunner


class TestCiclista(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def test_agregar_ciclista(self):
        self.driver.get(
            "file:///C:/Users/Jorge/Documents/Selenium/Ciclista.html")
        time.sleep(5)

        team_name = "Ineos"
        tipo = "Montanista"
        nombre = "Egan Bernal"
        edad = "27"
        nacionalidad = "Colombiano"
        atributo_especifico = "Alta"

        self.driver.find_element(By.ID, 'team-name').send_keys(team_name)
        self.driver.find_element(By.ID, 'tipo').send_keys(tipo)
        self.driver.find_element(By.ID, 'nombre').send_keys(nombre)
        self.driver.find_element(By.ID, 'edad').send_keys(edad)
        self.driver.find_element(By.ID, 'nacionalidad').send_keys(nacionalidad)
        self.driver.find_element(
            By.ID, 'atributo-especifico').send_keys(atributo_especifico)
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)

        table = self.driver.find_element(By.ID, 'cyclist-table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertEqual(len(
            rows), 2, f"Se esperaba 1 ciclista en la tabla, pero se encontraron {len(rows) - 1}.")
        cells = rows[1].find_elements(By.TAG_NAME, 'td')
        self.assertEqual(cells[0].text, tipo)
        self.assertEqual(cells[1].text, nombre)
        self.assertEqual(cells[2].text, edad)
        self.assertEqual(cells[3].text, nacionalidad)
        self.assertEqual(cells[4].text, atributo_especifico)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reportes'))
