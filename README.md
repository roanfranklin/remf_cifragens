# remf_cifragens

Script em python para cifragens:
   - Cifra de Cesar
   - Texto para Hexadecimal
   - Hexadecimal para Texto
   - Milet Polar
   - Tenis Polar
   - Zenit Polar

# Ajuda

    Use: ./remf_cifragens.py -cc [ ROT = numero positivo/negativo ] "Frase a ser cifrada com cifra de cesar usando um ROT específico."
         ./remf_cifragens.py -cc "Frase a ser cifrada com cifra de cesar usando todos ROT 1 à 26."
         ./remf_cifragens.py -t2h "Frase a ser coverditida de texto em hexadecinal."
         ./remf_cifragens.py -xt2h "Frase a ser coverditida de texto em hexadecinal."
         ./remf_cifragens.py -h2t "Frase a ser coverditida de hexadecinal em texto."
         ./remf_cifragens.py -xh2t "Frase a ser coverditida de hexadecinal em texto."
         ./remf_cifragens.py -mp "Cifrar o texto usando substituição MILET POLAR."
         ./remf_cifragens.py -tp "Cifrar o texto usando substituição TENIS POLAR."
         ./remf_cifragens.py -zp "Cifrar o texto usando substituição ZENIT POLAR."
         ./remf_cifragens.py -ana "ANAGRAMA"

OBS.: A conversão de Texto para Hexadecimal e de Hexadecimal para Texto, tem 2 (duas) entradas para cada. Motivo é que uma [ -t2h | -h2t ] usa o modulo binascii diretamente no python, e a outra [ -xt2h | -xh2t ] usa a ferramenta/aplicação xxd.

# Roan Franklin
http://www.remf.com.br/
