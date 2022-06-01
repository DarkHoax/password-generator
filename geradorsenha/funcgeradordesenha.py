import string
from random import choice

def Gerador():
    senha = ''

    try:
        n = int(input('Tamanho da senha: '))
    except n < 5:
        print('Senha com menos de 5 caracteres é considerada fraca...',
        'TENTE DE NOVO.')
    except ValueError:
        print('Caractere errado. TENTE DE NOVO')

    for i in range(n): #nº de iterações entre os N
        value = string.ascii_letters + string.digits + string.punctuation
        senha += choice(value)

    return senha

def Main(senha):
    print(f'Senha: {senha}')
    return senha

senha = Gerador()
Main(senha)
