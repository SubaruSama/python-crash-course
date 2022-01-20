'''
Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
'''

def make_shirt(size: str, text_message: str) -> None:
    '''make_shirt: Função que escreve na tela a sumarização do tamanho e da mensagem escrita

    :param size: tamanho da camisa (P, M, G)
    :type size: str
    :param text_message: o que será escrito
    :type text_message: str
    '''
    print(f'Tamanho da camisa é {size} com a mensagem \'{text_message}\'')

make_shirt(text_message='Python is great!', size='M')