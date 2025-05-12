Feature: Validação de login

Scenario: Login com sucesso
    Given que eu estou na página de login
    Quando eu preencho o campo de username com usuario válido
    And o campo de senha com senha válida
    And clico no botão de login
    Então eu devo ser redirecionado para a página inicial
    And deve aparecer o username no usuário logado

Scenario: Login com falha
    Given que eu estou na página de login
    When eu preencho o campo de username com usuario válido
    And o campo de senha inválida
    And clico no botão de login
    Then eu devo ver uma mensagem de erro informando que as credenciais estão incorretas
    