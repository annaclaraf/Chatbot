from bot import *
from flask import Flask

VERSAO = "1.0"

bot = main()
servico_bot = Flask(__name__)

@servico_bot.route("/resposta/<mensagem>", methods=["GET"])
def get_resposta(mensagem):
    resposta = bot.get_response(mensagem)

    return resposta.text

if __name__ == "__main__":
    servico_bot.run()