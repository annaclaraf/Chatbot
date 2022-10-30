from chatterbot import ChatBot
from chatterbot.comparisons import levenshtein_distance
from chatterbot.response_selection import get_first_response

def main(): 
    bot = ChatBot('Robô de atendimento Aribot', logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": levenshtein_distance,
            "response_selection_method": get_first_response
        }
    ])
    
    while True:
        entrada = input('Como posso ajudar? \n')
        resposta = bot.get_response(entrada)
        
        if resposta.confidence > 0.6:
            print(resposta.text)
        else:
            print('Não sei responder essa pergunta :( ')
                
if __name__ == "__main__":
    main()
