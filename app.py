from back_end.selenium_functions import iniciar_automacao


usuario = str(input('Digite o usuário da conta que deseja acessar: ')).strip()
senha = str(input('Digite a senha dessa conta: ')).strip()
pagina_alvo = str(input('Digite o @ da página que deseja curtir: ')).strip()


iniciar_automacao(usuario, senha, pagina_alvo)