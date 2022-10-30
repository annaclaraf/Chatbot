from chatterbot import ChatBot
from difflib import SequenceMatcher

CONFIANCA_MINIMA = 0.60

def comparar_mensagens(mensagem_digitada, mensagem_candidata):
    confianca = 0.0

    digitada = mensagem_digitada.text
    candidata = mensagem_candidata.text
    if digitada and candidata:
        confianca = SequenceMatcher(None, 
            digitada,
            candidata)
        confianca = round(confianca.ratio(), 2)

    return confianca

def main(): 
    bot = ChatBot('Robô de atendimento Aribot', 
        read_only=True,
        statement_comparison_function=comparar_mensagens,     
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch"
            }
        ]
    )

    return bot 

def executar_bot(bot):
    while True:
        mensagem = input('Como posso ajudar? \n')
        resposta = bot.get_response(mensagem.lower())

        print('confianca', resposta.confidence)

        if resposta.confidence >= CONFIANCA_MINIMA:
            print(resposta.text + "\n")
        else:
            print('Não sei responder essa pergunta :( \n')
                
if __name__ == "__main__":
    bot = main()

    executar_bot(bot)
