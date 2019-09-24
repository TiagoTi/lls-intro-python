import sys
import logging

logging.basicConfig(level=logging.INFO)

CHECKED=u'\u2713'
NOCHECKED=u'\u2715'
ARROW=u'\u2192'


def print_separador(repeticao=100):
    print(repeticao*'-')

def ler_string():
    print_separador(50)
    try:
        texto_informado = input("Por favor informe um Texto : \n")
    except EOFError as error:
        texto_informado = ''
        logging.error(f'Falha ao ler entrada {ARROW} {error}')
    logging.info(f'Texto informado {ARROW} {texto_informado}')
    
    return texto_informado


def has_alphanumerical(texto):
    if len(texto) > 0:
        response = CHECKED
    else:
        response = NOCHECKED

    print(f"{response}\tPossui alfanumerico")


def has_alphabetical(texto):
    response = CHECKED

    for caracter in texto:
        try:
            int(caracter)
            response = NOCHECKED
            break
        except ValueError:
            pass
    print(f"{response}\tPossui apenas alfabetico")

def has_digit(texto):
    response = CHECKED

    for caracter in texto:
        try:
            int(caracter)
        except ValueError:
            response = NOCHECKED
            break
    print(f"{response}\tPossui apenas digito")

def has_lowercase(texto):
    response = NOCHECKED
    letras = [ letra for letra in texto if letra in texto.lower() ]
    if len(letras)>0:
        response = CHECKED
    print(f"{response}\tPossui letras minusculas")
    

def has_uppercase(texto):
    response = NOCHECKED
    letras = [ letra for letra in texto if letra in texto.upper() ]
    if len(letras)>0:
        response = CHECKED
    print(f"{response}\tPossui letras maiusculas")

if __name__ == '__main__':
    #Passe como argumento de linha de comando, uma string qualquer
    string_lida = ler_string()

    #True - se algum dos caracteres da string for alfanumérico
    has_alphanumerical(string_lida)

    #True - se todos os caracteres da string for alfabético
    has_alphabetical(string_lida)

    #True - se algum dos caracteres da string for dígito
    has_digit(string_lida)

    #True - se algum dos caracteres da string for minúsculo
    has_lowercase(string_lida)

    #True - se algum dos caracteres da string for maiúsculo
    has_uppercase(string_lida)

    print_separador(50)