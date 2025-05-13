from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class SeleniumHelpers:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def send_keys_to_element(self, *locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def wait_for_element(self, *locator, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def is_element_present(self, *locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def wait_for_element_to_be_clickable(self, locator, by=By.CSS_SELECTOR):
        """
        Aguarda até que o elemento esteja clicável.
        :param locator: Localizador do elemento.
        :param by: Tipo de localizador.
        :return: O elemento clicável.
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(f"Elemento com locator '{locator}' não ficou clicável após {self.timeout} segundos.")

    def scroll_to_element(self, locator, by=By.CSS_SELECTOR):
        """
        Rola a página até que o elemento esteja visível.
        :param locator: Localizador do elemento.
        :param by: Tipo de localizador.
        """
        element = self.wait_for_element(locator, by)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def hover_over_element(self, locator, by=By.CSS_SELECTOR):
        """
        Move o mouse sobre um elemento.
        :param locator: Localizador do elemento.
        :param by: Tipo de localizador.
        """
        element = self.wait_for_element(locator, by)
        ActionChains(self.driver).move_to_element(element).perform()

    def press_key(self, key):
        """
        Pressiona uma tecla no teclado.
        :param key: Tecla a ser pressionada (ex.: Keys.ENTER, Keys.TAB).
        """
        ActionChains(self.driver).send_keys(key).perform()

    def wait_for_text_in_element(self, locator, text, by=By.CSS_SELECTOR):
        """
        Aguarda até que um texto específico esteja presente em um elemento.
        :param locator: Localizador do elemento.
        :param text: Texto esperado.
        :param by: Tipo de localizador.
        :return: O elemento contendo o texto.
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.text_to_be_present_in_element((by, locator), text)
            )
        except TimeoutException:
            raise TimeoutException(f"Texto '{text}' não encontrado no elemento com locator '{locator}' após {self.timeout} segundos.")

    def take_screenshot(self, file_path):
        """
        Tira um screenshot da página atual.
        :param file_path: Caminho onde o screenshot será salvo.
        """
        self.driver.save_screenshot(file_path)