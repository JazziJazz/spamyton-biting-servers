# Spamyton Biting Servers

A solução **definitiva** para divulgação de servidores **OpenTibia** em massa. Você está cansado de aproveitadores entrando em seu servidor procurando por vantagens ou cargos em troca de divulgação? Essa aplicação vai ser a solução de seus problemas! 🥳🎉

Utilizando a **{c:red}API{/c}** [Who is PythOnline?](https://github.com/JazziJazz/who-is-pythonline) essa aplicação é capaz de obter informações sobre todos os jogadores **{c:green}online{/c}** em um determinado servidor e enviar **automaticamente** uma mensagem pré-definida para cada um deles. É fantástico! 🚀 🕺💃 ✨

Seu uso é fácil e intuitivo, o código fala por si. Para divulgar seu servidor basta criar uma conta em um dos servidores cobertos pela [WhoisPythOnline](https://github.com/JazziJazz/who-is-pythonline) e entrar através de **qualquer** client, isso significa; **Você pode usar qualquer versão do client** padrão do Tibia ou mesmo utilizar _**OTClient**_, você pode até mesmo especificar o nome do seu próprio client. 🥰

Para executar o _SPAM_ é muito simples, basta iniciar uma instância do {c:blue}_**Spamython**_{/c}. Essa istância possuí apenas {c:red}_**dois**_{/c} parâmetros {c:red}_**obrigatórios**_{/c}, o _primeiro_ é o nome do servidor para que se inicie o a divulgação e o _segundo_ parâmetro é a mensagem a ser enviada.
```PYTHON
message = 'Entra lá no servidor irmão! https://www.baiakdosputons.com/'
my_spam_bot = SpamythonMessage('Baiak Illusions', message)
```

Assim você tem uma instância do servidor que deseja iniciar a divulgação. Um **JSON** é criado na pasta de **logs** contendo dados sobre todos os jogadores do servidor em questão. Por fim basta chamar o método {c:green}_**shooting_messages**_{/c}():

```PYTHON
my_spam_bot.shooting_messages():
```

Aproveite seu tempo enquanto uma sequência de mensagens é enviada para cada jogador online.
**Criador**: _Rodrigo S**#**7737_

_Com ❤️ Rodrigo Siliunas_, _**Jazz**_. 

## Como rodar o arquívo main.py?
É muito simples, o código é desenvolvido com _**Python 3.9.6**_. Possui um total de quatro dependências até o momento, tudo que você precisa fazer é utilizar o enviroment e depois executar o código. 😯😄

Caso você esteja no **Windows**, abra um _terminal_ ou _powershell_ no **diretório principal** e execute o comando:
```
.\enviroment\scripts\activate
```

[Imagem do Chat](https://imgur.com/8NRnHLq.png "Uma imagem simples do chat com a aplicação em execução.")