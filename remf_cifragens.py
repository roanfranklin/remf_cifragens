#!/usr/bin/python3
# pip3 install pyfiglet
# pip3 install colorama

import os, sys, binascii, re
import pyfiglet
import subprocess
import colorama
from colorama import Fore, Style

def enumero(valor):
    try:
         float(valor)
    except ValueError:
         return False
    return True

def cesar(chave, mensagem):
    if not enumero(chave):
        ajuda()

    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_deslocado = alfabeto[chave:] + alfabeto[:chave]
    tabela = str.maketrans(alfabeto, alfabeto_deslocado)
    mensagem1 = mensagem.translate(tabela)

    alfabeto1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto1_deslocado = alfabeto1[chave:] + alfabeto1[:chave]
    tabela1 = str.maketrans(alfabeto1, alfabeto1_deslocado)

    return mensagem1.translate(tabela1)

def txt2hex(mensagem):
    # Converte um texto para Hex
    encoded = binascii.hexlify(bytes(mensagem, "utf-8"))
    encoded = str(encoded).strip("b")
    encoded = encoded.strip("'")
    return encoded

def hex2txt(mensagem):
    # Converte Hex para texto(ASCII)
    decoded = binascii.unhexlify(bytes(mensagem, "utf-8"))
    decoded = str(decoded).strip("b")
    decoded = decoded.strip("'")
    return decoded


def sh(cmd, input=""):
    rst = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=input.encode("utf-8"))
    assert rst.returncode == 0, rst.stderr.decode("utf-8")
    return rst.stdout.decode("utf-8")

def txt2hex_xxd(mensagem):
    output = sh('echo ' + mensagem + ' | xxd -ps -c 200 | tr -d "\n"')
    return output

def hex2txt_xxd(mensagem): 
    output = sh('echo ' + mensagem + ' | xxd -r -p')
    return output

def miletpolar(mensagem):
    replaces = {'m':'p',
                'i':'o',
                'l':'l',
                'e':'a',
                't':'r',
                'M':'P',
                'I':'O',
                'L':'L',
                'E':'A',
                'T':'R',
                'p':'m',
                'o':'i',
                'l':'l',
                'a':'e',
                'r':'t',
                'P':'M',
                'O':'I',
                'L':'L',
                'A':'E',
                'R':'T'
                }
    regex = re.sub("|".join(replaces.keys()), lambda match: replaces[match.string[match.start():match.end()]], mensagem)
    return regex

def tenispolar(mensagem):
    replaces = {'t':'p',
                'e':'o',
                'n':'l', 
                'i':'a', 
                's':'r',
                'T':'P',
                'E':'O',
                'N':'L',
                'I':'A',
                'S':'R',
                'p':'t',
                'o':'e',
                'l':'n',
                'a':'i',
                'r':'s',
                'P':'T',
                'O':'E',
                'L':'N',
                'A':'I',
                'R':'S'
                }
    regex = re.sub("|".join(replaces.keys()), lambda match: replaces[match.string[match.start():match.end()]], mensagem)
    return regex

def zenitpolar(mensagem):
    replaces = {'z':'p',
                'e':'o',
                'n':'l',
                'i':'a',
                't':'r',
                'Z':'P',
                'E':'O',
                'N':'L',
                'I':'A',
                'T':'R',
                'p':'z',
                'o':'e',
                'l':'n',
                'a':'i',
                'r':'t',
                'P':'Z',
                'O':'E',
                'L':'N',
                'A':'I',
                'R':'T'
                }
    regex = re.sub("|".join(replaces.keys()), lambda match: replaces[match.string[match.start():match.end()]], mensagem)
    return regex

def perm(s, s1 = ''):
    mensagem = ''
    if len(s) == 0:
        print(s1)
    else:
        for i in range(len(s)):
            perm(s[:i]+s[(i+1):],s1+s[i])

    return 0

def binario_texto(s, encoding='UTF-8'):
    n = int('0b'+s, 2)
    txt = binascii.unhexlify('%x' % n)
    return txt

def texto_binario(a):
    a_bytes = bytes(a, "ascii")
    return ' '.join(["{0:b}".format(x) for x in a_bytes])

def logo():
    os.system("clear")
    ascii_banner = pyfiglet.figlet_format("REMF - Cifragens")
    name_app = 'Cifragens'
    print(Style.BRIGHT+Fore.BLUE+ascii_banner)
    print(Fore.YELLOW+' [ '+Fore.WHITE+'REMF.COM.BR'+Fore.YELLOW+' - '+Fore.WHITE+name_app+Fore.YELLOW+' ]'+Style.RESET_ALL)

def ajuda():
    logo()
    print(' '+Fore.CYAN)
    print(' Use:', sys.argv[0], '-cc [ ROT = numero positivo/negativo ] "Frase a ser cifrada com cifra de cesar usando um ROT específico."')
    print('     ', sys.argv[0], '-cc "Frase a ser cifrada com cifra de cesar usando todos ROT 1 à 26."')
    print('     ', sys.argv[0], '-t2h "Frase a ser coverditida de texto em hexadecinal."')
    print('     ', sys.argv[0], '-xt2h "Frase a ser coverditida de texto em hexadecinal."')
    print('     ', sys.argv[0], '-h2t "Frase a ser coverditida de hexadecinal em texto."')
    print('     ', sys.argv[0], '-xh2t "Frase a ser coverditida de hexadecinal em texto."')
    print('     ', sys.argv[0], '-mp "Cifrar o texto usando substituição MILET POLAR."')
    print('     ', sys.argv[0], '-tp "Cifrar o texto usando substituição TENIS POLAR."')
    print('     ', sys.argv[0], '-zp "Cifrar o texto usando substituição ZENIT POLAR."')
    print('     ', sys.argv[0], '-b2t "Binario para texto."')
    print('     ', sys.argv[0], '-t2b "Texto para binario."')
    print('     ', sys.argv[0], '-ana "ANAGRAMA"')
    print(Style.RESET_ALL+' ')
    quit()

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-cc':
            if len(sys.argv) == 3:
                mensagem = str(sys.argv[2])
                contador = 1
                while ( contador < 27 ):
                    cifrada = cesar(contador, mensagem)
                    print(contador,' ', cifrada)
                    contador = contador + 1
                quit()
            elif len(sys.argv) == 4:
                chave = int(sys.argv[2])
                mensagem = str(sys.argv[3])
                cifrada = cesar(chave, mensagem)
            else:
                ajuda()
        elif sys.argv[1] == '-t2h':
            if len(sys.argv) == 3:
                mensagem = str(sys.argv[2])
                cifrada = txt2hex(mensagem)
            else:
                ajuda()
        elif sys.argv[1] == '-xt2h':
            if len(sys.argv) == 3:
                mensagem = str(sys.argv[2])
                cifrada = txt2hex_xxd(mensagem)
            else:
                ajuda()
        elif sys.argv[1] == '-h2t':
            if len(sys.argv) == 3:
                mensagem = str(sys.argv[2])
                cifrada = hex2txt(mensagem)
            else:
                ajuda()
        elif sys.argv[1] == '-xh2t':
            if len(sys.argv) == 3:
                mensagem = str(sys.argv[2])
                cifrada = hex2txt_xxd(mensagem)
            else:
                ajuda()
        elif sys.argv[1] == '-mp':
            if len(sys.argv) == 3:
                mensagem = str(sys.argv[2])
                cifrada = miletpolar(mensagem);
            else:
                ajuda()
        elif sys.argv[1] == '-tp':
            if len(sys.argv) == 3:
                mensagem = str(sys.argv[2])
                cifrada = tenispolar(mensagem);
            else:
                ajuda()
        elif sys.argv[1] == '-zp':
            if len(sys.argv) == 3:
                mensagem = str(sys.argv[2])
                cifrada = zenitpolar(mensagem);
            else:
                ajuda()
        elif sys.argv[1] == '-b2t':
            if len(sys.argv) == 3:
                mensagem = str(sys.argv[2])
                cifrada = binario_texto(mensagem);
            else:
                ajuda()
        elif sys.argv[1] == '-t2b':
            if len(sys.argv) == 3:
                mensagem = str(sys.argv[2])
                cifrada = texto_binario(mensagem);
            else:
                ajuda()

        elif sys.argv[1] == '-ana':
            if len(sys.argv) == 3:
                perm(str(sys.argv[2]))
                quit()
            else:
                ajuda()
        else:
            ajuda()
    else:
        ajuda()

    print(cifrada)

if __name__ == "__main__":
    main()

