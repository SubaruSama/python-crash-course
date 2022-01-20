'''
Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
'''

def make_shirt(size: str = 'G', text_message: str = 'I love Python') -> None:
    '''make_shirt: Função que escreve na tela a sumarização do tamanho e da mensagem escrita

    :param size: tamanho da camisa (P, M, G)
    :type size: str
    :param text_message: o que será escrito
    :type text_message: str
    '''
    print(f'Tamanho da camisa é {size} com a mensagem \'{text_message}\'')

make_shirt(size='P', text_message='This is a test string')