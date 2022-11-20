# Aribot 

Robô de atendimento que tira dúvidas sobre programação.

## Como executar

```bash
# Clone o repositório
$ git clone https://github.com/annaclaraf/Chatbot.git

# Entre na pasta do projeto
$ cd Chatbot

# Instale as dependências
$ pip3 install -r requirements.txt

# Execute o treinamento
$ python3 treinamento.py

# Execute o serviço web
$ python3 servico_web.py

# Entre na pasta do servidor
$ cd web

# Instale as dependências
$ npm i

# Execute a aplicação 
npm run start 
```

Por fim, o robô estará disponível para acesso no seu navegador em: http://localhost:3000/

## Para executar os testes

```bash
# Execute os testes de saudação
$ python3 -m tests.test_saudacoes

# Execute os testes das perguntas
$ python3 -m tests.test_infos
```
---

Feito com 💗 by [Anna Clara](https://github.com/annaclaraf)