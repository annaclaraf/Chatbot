from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONFIG_FILES = [
    'config/infos.json',
    'config/saudacoes.json'
]

def iniciar():
    global bot
    global treinador

    bot = ChatBot('Robô de atendimento Aribot')
    treinador = ListTrainer(bot)

def carregar_conversas():
    conversas = []

    for arquivo_configuracao in CONFIG_FILES:
        with open(arquivo_configuracao, "r") as arquivo:
            conversas_configuracao = json.load(arquivo)
            conversas.append(conversas_configuracao["conversas"])

            arquivo.close()

    return conversas

def treinar_robo(conversas):
    global treinador

    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens =  mensagens_resposta["mensagens"]
            resposta =  mensagens_resposta["resposta"]

            for mensagem in mensagens:
                treinador.train([mensagem, resposta])

if __name__ == "__main__":
    iniciar()

    conversas = carregar_conversas()
    if conversas:
        treinar_robo(conversas)