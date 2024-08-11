from back_end.selenium_functions import iniciar_automacao
from back_end.iniciar_driver_function import iniciar_driver
from time import sleep

execution_id = 1
usuario = str(input('Digite o usuário da conta que deseja acessar: ')).strip()
senha = str(input('Digite a senha dessa conta: ')).strip()
pagina_alvo = str(input('Digite o @ da página que deseja curtir: ')).strip()
comentario = str(input(
    'Digite um comentário (se não deseja comentar, deixe este campo vasio): ')).strip()

driver, wait = iniciar_driver()

while True:
    iniciar_automacao(driver, wait, usuario, senha, pagina_alvo, comentario, execution_id)
    execution_id += 1
    sleep(86400)
