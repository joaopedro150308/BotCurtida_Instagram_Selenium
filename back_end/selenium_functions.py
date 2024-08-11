from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as condicoes_esperadas
from selenium.webdriver.common.keys import Keys
from back_end.iniciar_driver_function import iniciar_driver
from back_end.uteis import formatar_endereco_da_pagina
from time import sleep


def navegar_ate_o_site(driver):
    driver.get('https://www.instagram.com/')


def logar_instagram(driver, wait, senha, usuario):
    # Colocar o usuario
    campo_nome = wait.until(condicoes_esperadas.element_to_be_clickable(
        (By.XPATH, "//input[@aria-label='Telefone, nome de usuário ou email']")))
    campo_nome.send_keys(usuario)
    sleep(1)

    # Colocar a senha
    campo_senha = wait.until(condicoes_esperadas.element_to_be_clickable(
        (By.XPATH, "//input[@aria-label='Senha']")))
    campo_senha.send_keys(senha)
    sleep(1)

    # Clicar em entrar
    botao_entrar = wait.until(condicoes_esperadas.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")))
    botao_entrar.click()


def navegar_ate_a_pagina_alvo(driver, wait, pagina):
    # Esperar carregar a conta
    div_de_botoes = wait.until(condicoes_esperadas.element_to_be_clickable(
        (By.XPATH, "//div[@class='x1xgvd2v x1o5hw5a xaeubzz x1cy8zhl xvbhtw8 x9f619 x78zum5 xdt5ytf x1gvbg2u x1y1aw1k xn6708d xx6bls6 x1ye3gou']")))
    # Ir até o URL da página desejada
    endereco_pagina = formatar_endereco_da_pagina(pagina)
    driver.get(endereco_pagina)


def acessar_ultimo_post(driver, wait):
    # Encontrar a última publicação
    driver.execute_script('window.scrollTo=(0, 500);')
    sleep(5)
    postagens = wait.until(condicoes_esperadas.visibility_of_any_elements_located(
        (By.XPATH, "//div[@class='_ac7v xras4av xgc1b0m xat24cr xzboxd6']/div[1]")))
    sleep(1)
    primeiro_post = postagens[0]
    sleep(1)
    primeiro_post.click()


def procurar_botao_recarregar(wait):
    # Botao recarregar
    try:
        botao_recarregar = wait.until(condicoes_esperadas.element_to_be_clickable(
            (By.XPATH, "//div[text()='Recarregar página']")))
        sleep(2)
        botao_recarregar.click()
    except TimeoutException:
        print('Botão recarregar não encontrado')


def verificar_e_curtir(wait):
    # Verificar se foi curtido, se não: Curtir e comentar, se sim: esperar 24hrs
    # Curtir
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
        return True


def verificar_curtir_e_comentar(wait, comentario):
    if verificar_e_curtir(wait) is True:
        if comentario != '':
            # svg[aria-label='Comentar']
            # //span//div//div[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k'] - 2 resultados
            # //span[@class='x1rg5ohu']/div/div
            botao_comentario = wait.until(condicoes_esperadas.element_to_be_clickable(
                (By.CSS_SELECTOR, "svg[aria-label='Comentar']")))
            sleep(1)
            botao_comentario.click()
            sleep(2)
            campo_comentario = wait.until(condicoes_esperadas.element_to_be_clickable(
                (By.XPATH, "//textarea[@aria-label='Adicione um comentário...']")))
            campo_comentario.send_keys(comentario)
            sleep(1)
            campo_comentario.send_keys(Keys.ENTER)


def iniciar_automacao(driver, wait, usuario, senha, pagina, comentario, execution_id):
    driver.set_window_size(800, 600)
    if execution_id == 1:
        navegar_ate_o_site(driver)
        logar_instagram(driver, wait, senha, usuario)
    sleep(1)
    navegar_ate_a_pagina_alvo(driver, wait, pagina)
    sleep(3)
    acessar_ultimo_post(driver, wait)
    sleep(5)
    procurar_botao_recarregar(wait)
    verificar_curtir_e_comentar(wait, comentario)
    driver.minimize_window()

    print('Processo finalizado. Iniciando agendamento.')
