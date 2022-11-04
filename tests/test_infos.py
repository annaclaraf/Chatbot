import sys
sys.path.append("..")
from bot import *
import unittest

class TestInformacoes(unittest.TestCase):
    def setUp(self):
        self.bot = main()

    def test_01_o_que_faz(self):
        perguntas = [
            "O que é um programador?", 
            "O que é um desenvolvedor?", 
            "O que faz um programador?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.bot.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O programador ou desenvolvedor é o profissional que cria, desenvolve e mantém diferentes tipos de softwares em sistemas", 
                resposta.text
            )

    def test_02_como_aprender(self):
        perguntas = [
            "O que devo estudar para aprender programação?", 
            "Como aprender programação?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.bot.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Você deve focar o seu tempo em aprender a chamada lógica de programação",
                resposta.text
            )
    
    def test_03_diferenca_backend_frontend(self):
        perguntas = [
            "Qual a diferença entre backend e frontend?", 
            "O que é backend e frontend?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.bot.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O front-end pode ser considerado como a parte visual de um site, aquilo que o usuário consegue ver e interagir",
                resposta.text
            )

    def test_04_orientacao_objetos(self):
        perguntas = [
            "O que é orientação a objetos?", 
            "O que é programação orientada a objetos?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.bot.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A programação orientada a objetos é um paradigma da programação que tem como objetivo utilizar “objetos” na construção de um software",
                resposta.text
            )

    def test_05_melhor_linguagem(self):
        perguntas = [
            "Qual a melhor linguagem de programação?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.bot.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Não existe uma resposta definitiva para essa pergunta, porque a resposta depende de vários fatores.",
                resposta.text
            )

    def test_06_diferenca_javascript_typescript(self):
        perguntas = [
            "Qual a diferença entre javascript e typescript?", 
            "O que é javascript e typescript?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.bot.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "São duas linguagens de programação diferentes, porém uma é o superconjunto de outra",
                resposta.text
            )

    def test_07_mercado_trabalho(self):
        perguntas = [
            "Como está o mercado de trabalho para a programação atualmente?", 
            "Como está o mercado para a área de programação?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.bot.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O setor de tecnologia é um dos menos atingidos pelas crises econômicas, o que torna a carreira de programador uma das mais estáveis e promissoras do mercado",
                resposta.text
            )


if __name__ == "__main__":
    load = unittest.TestLoader()
    tests = unittest.TestSuite()

    tests.addTest(load.loadTestsFromTestCase(TestInformacoes))

    exec = unittest.TextTestRunner()
    exec.run(tests)