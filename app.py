from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condicoes_esperadas
from iniciar_driver_function import iniciar_driver
from formatar_pagina import formatar_endereco_da_pagina
from time import sleep

# Pegando credenciais
usuario = str(input('Digite o usuário da conta que deseja acessar: ')).strip()
senha = str(input('Digite a senha dessa conta: ')).strip()
pagina_alvo = str(input('Digite o @ da página que deseja curtir: ')).strip()

endereco_pagina = formatar_endereco_da_pagina(pagina_alvo)


while True:

    driver, wait = iniciar_driver()
    # Navegar até o site do instagram: https://www.instagram.com/
    driver.get('https://www.instagram.com/')

    # Colocar o usuario
    campo_nome = wait.until(condicoes_esperadas.element_to_be_clickable(
        (By.XPATH, "//input[@aria-label='Telefone, nome de usuário ou email']")))
    campo_nome.send_keys(usuario)

    # Colocar a senha
    campo_senha = wait.until(condicoes_esperadas.element_to_be_clickable(
        (By.XPATH, "//input[@aria-label='Senha']")))
    campo_senha.send_keys(senha)

    # Clicar em entrar
    botao_entrar = wait.until(condicoes_esperadas.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")))
    botao_entrar.click()

    # Navegar até a página desejada
        # Esperar carregar a conta
    botao_iginorar = wait.until(condicoes_esperadas.element_to_be_clickable(
        (By.XPATH, "//div[text()='Agora não']")))
        # Ir até o URL da página desejada
    driver.get(endereco_pagina)

    # Encontrar a última publicação
    postagens = wait.until(condicoes_esperadas.visibility_of_any_elements_located(
        (By.XPATH, "//div[@class='_ac7v xras4av xgc1b0m xat24cr xzboxd6']/div[1]")))
    primeiro_post = postagens[0]
    primeiro_post.click()

    # Verificar se foi curtido, se não: Curtir e comentar, se sim: esperar 24hrs

    botao_curtir_lista = wait.until(condicoes_esperadas.visibility_of_any_elements_located(
        (By.CSS_SELECTOR, "svg[aria-label*='urtir']")))
    botao_atributo = botao_curtir_lista[0].get_attribute('aria-label')
    if botao_atributo == 'Curtir':
        botao_curtir_elemento = wait.until(condicoes_esperadas.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='x1ypdohk']/div")))[0]
        print(botao_curtir_elemento)
        botao_curtir_elemento.click()
        sleep(1)
        botao_curtir_elemento.click()
    driver.close()

    # Esperar 24hrs
    sleep(86400)
