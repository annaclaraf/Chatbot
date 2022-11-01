from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance

CONFIANCA_MINIMA = 0.60

def main(): 
    bot = ChatBot('Robô de atendimento Aribot', 
        read_only=True,
        logic_adapters=[
            {
                "statement_comparison_function": LevenshteinDistance,     
                "import_path": "chatterbot.logic.BestMatch"
            }
        ]
    )

    return bot 

def executar_bot(bot):
    while True:
        mensagem = input('Como posso ajudar? \n')
        resposta = bot.get_response(mensagem.lower())

        if resposta.confidence >= CONFIANCA_MINIMA:
            print(resposta.text + "\n")
        else:
            print('Não sei responder essa pergunta :( \n')
                
if __name__ == "__main__":
    bot = main()

    executar_bot(bot)
