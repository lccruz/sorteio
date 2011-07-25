# -*- coding: utf8 -*-

import sys
import random
import os

class Sorteio:
    def __init__(self, lista):
        self.lista = lista

    def sortear(self):
        if len(self.lista):
            sorteado = random.choice(self.lista)
            self.lista.remove(sorteado)
            return sorteado
        else:
            return ""


if __name__ == "__main__":
    try:
        nome_arquivo = sys.argv[1]
    except IndexError:
        print "Informe o arquivo com os participantes!\nsorteio.py <arquivo>"
        sys.exit()

    try:
        arquivo = open(nome_arquivo, "r")
    except Exception:
        print "O arquivo %s não existe ou não pode ser aberto!" % nome_arquivo
        sys.exit()

    lista = arquivo.readlines()

    s = Sorteio(lista)

    while len(s.lista):
        sorteado = s.sortear()
        if sorteado:
            os.system('cls' if os.name=='nt' else 'clear')
            print "\nO escolhido é: %s\n" % sorteado
            raw_input("Aperte ENTER para sortear novamente...")
    else:
        print "Não há mais participantes!"
