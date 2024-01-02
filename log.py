import logging

logging.basicConfig(level=logging.DEBUG,filename='app.log',filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')#setar o nivel

try:
    email = input('Digite seu email')
    senha = int(input('Digite sua senha bancária'))
    if senha == 1234:
        logging.info(f'{email} entrou em sua conta bancária')
except ValueError as erro:
    print('Favor Digitar apenas números')
    logging.warning(erro)
