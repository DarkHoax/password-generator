import string
from random import choice

def Gerador():
    senha = ''
    with open('senhas.txt', 'w+') as arq:
        try: #Checa erros
            n = int(input('Tamanho da senha: '))
            if n < 6: #Se menor que 6 vai dar erro pois a senha é fraca
                n = int(input('Senha com menos de 6 chars é fraca... Digite novamente: '))
                value = string.ascii_letters + string.digits + string.punctuation
                senha += choice(value)

            else: #Caso não haja erros a senha vai ser gerada
                for i in range(n): #nº de iterações entre os N
                    value = string.ascii_letters + string.digits + string.punctuation
                    senha += choice(value)

        except ValueError: #Caso tu escrevas uma letra, vai dar erro
            print('Caractere errado. TENTE DE NOVO')
            n = int(input('Tamanho da senha: '))
            for i in range(n): #nº de iterações entre os N
                value = string.ascii_letters + string.digits + string.punctuation
                senha += choice(value)
        arq.write(str(senha)+'\n')

    return n, arq


def Main(n, arq):

    senhas = ''
    l = ''
    with open('senhas.txt', 'r') as arq:
        l = arq.readlines()
        for i in range(len(l)):
            senhas += str(l).replace("['","").replace("']", "")
    print(f'Senha: {senhas}')

    return senhas

n, arq = Gerador()
senhas = Main(n, arq)
