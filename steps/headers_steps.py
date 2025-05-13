from behave import given, when, then
 
@given('que o usuário está na home')
def step_usuario_na_home(context):
    # O navegador já abre na home no before_scenario, então nada a fazer aqui
    pass
 
@when('ele fizer login com o usuário "{usuario}" e senha "{senha}"')
def step_fazer_login(context, usuario, senha):
    context.header.logar(usuario, senha)
 
@then('o nome do usuário "{nome}" deve ser exibido no header')
def step_verificar_usuario_logado(context, nome):
    nome_exibido = context.header.obter_usuario_logado()
    assert nome_exibido == nome, f"Esperado: {nome}, mas exibido: {nome_exibido}"
 
@when('ele fizer logout')
def step_fazer_logout(context):
    context.header.fazer_logout()
 
@then('nenhum usuário deve estar logado')
def step_verificar_usuario_deslogado(context):
    assert context.header.obter_usuario_logado() is None
 
@when('ele buscar por "{produto}" no campo de busca')
def step_buscar_produto(context, produto):
    context.header.buscar_produto(produto)
 
@then('o navegador deve exibir resultados relacionados a "{produto}"')
def step_verificar_resultado_busca(context, produto):
    assert produto.lower() in context.driver.page_source.lower(), f"O texto '{produto}' não foi encontrado na página."