# -*- coding: utf8 -*-

import unittest
from sorteio import Sorteio


class SorteioTest(unittest.TestCase):
    def setUp(self):
        self.lista = [
            "Nerdson",
            "Beta Bitsy",
            "Lilo",
            "Bozo",
            "Amigoogle"
        ]
        self.sorteio = Sorteio(self.lista[:])

    def test_load(self):
        self.assertEqual(self.lista, self.sorteio.lista)

    def test_sorteia(self):
        sorteado = self.sorteio.sortear()
        self.lista.remove(sorteado)
        self.assertEqual(self.lista, self.sorteio.lista)
        log = open('participantes_sorteados.txt', 'r')
        sorteado_file = log.readline()
        self.assertEqual(sorteado_file, sorteado)


unittest.main()
