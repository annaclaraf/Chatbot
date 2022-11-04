import sys
sys.path.append("..")
from bot import *
import unittest

class TestSaudacoes(unittest.TestCase):
    def setUp(self):
        self.bot = main()

    def test_01_oi_ola_tudobem(self):
        saudacoes = ["oi", "olá", "tudo bem?"]

        for saudacao in saudacoes:
            print(f"testando saudação: {saudacao}")

            resposta = self.bot.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Olá, sou a Aribot e tiro dúvidas sobre programação", 
                resposta.text
            )

    def test_02_bomdia_boatarde_boanoite(self):
        saudacoes = ["Bom dia", "Boa tarde", "Boa noite"]

        for saudacao in saudacoes:
            print(f"testando saudação: {saudacao}")

            resposta = self.bot.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                saudacao + ", sou a Aribot e tiro dúvidas sobre programação",
                resposta.text
            )


if __name__ == "__main__":
    load = unittest.TestLoader()
    tests = unittest.TestSuite()

    tests.addTest(load.loadTestsFromTestCase(TestSaudacoes))

    exec = unittest.TextTestRunner()
    exec.run(tests)