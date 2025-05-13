Feature: Funcionalidades do Header
 
  Como usuário do site
  Quero utilizar o header para login, logout e busca
  Para que eu possa navegar e interagir com a aplicação de forma eficiente
 
  Scenario: Login com sucesso pelo header
    Given que o usuário está na home
    When ele fizer login com o usuário "usuario123" e senha "senha123"
    Then o nome do usuário "USUARIO123" deve ser exibido no header
 '''
  Scenario: Logout com sucesso
    Given que o usuário está na home
    When ele fizer login com o usuário "usuario123" e senha "senha123"
    And ele fizer logout
    Then nenhum usuário deve estar logado
 
  Scenario: Buscar produto usando o campo de busca do header
    Given que o usuário está na home
    When ele buscar por "laptop" no campo de busca
    Then o navegador deve exibir resultados relacionados a "laptop"

    '''