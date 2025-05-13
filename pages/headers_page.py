from selenium.webdriver.common.by import By
 
class HeaderPage:
    # ==== Constantes (locators) ====
    LOGO = (By.ID, 'Layer_1')
    SEARCH_ICON = (By.CSS_SELECTOR, 'div#searchSection > div > img')
    SEARCH_INPUT = (By.ID, 'autoComplete')
    USER_ICON = (By.ID, 'menuUser')
    LOGIN_POPUP = (By.CSS_SELECTOR, 'div.pop-up.loginPopUp')
    USERNAME_FIELD = (By.NAME, 'username')
    PASSWORD_FIELD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.ID, 'sign_in_btnundefined')
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, 'CREATE NEW ACCOUNT')
    SHOPPING_CART_ICON = (By.ID, 'menuCart')
    LOGOUT_BUTTON = (By.XPATH, "//label[text()='Sign out']")
    USER_NAME_DISPLAY = (By.CSS_SELECTOR, 'label#menuUserLink > span')
 
    def __init__(self, driver, helpers):
        self.driver = driver
        self.helpers = helpers  
 
    # ==== Métodos ====
    def clicar_logo(self):
        self.helpers.click_element(*self.LOGO)
 
    def buscar_produto(self, texto):
        self.helpers.click_element(*self.SEARCH_ICON)
        self.helpers.send_keys_to_element(*self.SEARCH_INPUT, keys=texto)        
 
    def abrir_menu_login(self):
        self.helpers.click_element(*self.USER_ICON)
        self.helpers.wait_for_element(*self.LOGIN_POPUP)
 
    def logar(self, usuario, senha):
        self.abrir_menu_login()
        self.helpers.send_keys_to_element(*self.USERNAME_FIELD, keys=usuario)
        self.helpers.send_keys_to_element(*self.PASSWORD_FIELD, keys=senha)
        self.helpers.click_element(*self.SIGN_IN_BUTTON)
        self.helpers.wait_for_element(*self.USER_NAME_DISPLAY)
 
    def acessar_criacao_conta(self):
        self.abrir_menu_login()
        self.helpers.click_element(*self.CREATE_ACCOUNT_LINK)
 
    def clicar_carrinho(self):
        self.helpers.click_element(*self.SHOPPING_CART_ICON)
 
    def fazer_logout(self):
        self.helpers.click_element(*self.USER_ICON)
        self.helpers.click_element(*self.LOGOUT_BUTTON)
 
    def obter_usuario_logado(self):
        if self.helpers.is_element_present(*self.USER_NAME_DISPLAY):
            return self.helpers.wait_for_element(*self.USER_NAME_DISPLAY).text
        return None