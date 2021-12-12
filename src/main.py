from modules.spamBot import SpamBot
from modules.pythOnline.factory import ServerFactory


if __name__ == "__main__":
    """
        Lista de servidores disponíveis para coleta de dados (nome, método de coleta):
          • Baiak IceWar, IceWar
          • Kaldrox Net, Kaldrox
          • Demolidores, Demolidores
          • Baiak Ilusions, Ilusions
          • New Tibia, NewTibia
          • Tibia Canob, Canob
          • Pbot Wars, Pbot
          • Baiak Ziron, Ziron
          • Baiak Pesadão, Pesadao
          • Underwar, Underwar

        Para gerar a lista de servidores basta descomentar o código abaixo, escolher o servidor e
        chamar a factory com o método de coleta.

        Caso você queira gerar a lista de maneira desornedada basta que você crie a lista de maneira
        randomizada, como exibido no código comentado abaixo. Caso você não se importe com isso, basta
        remover completamente o parâmetro e chamar o método get_players_online vazio.
    """

    #  Descomentar o código abaixo para gerar um JSON do servidor a sua escolha.
    # server = ServerFactory("IceWar")
    # server.get_players_online(randomized_list=True)

    message = "Isso é um teste de algo que estou programando, por favor não responda, ignore a mensagem. Obrigado pela atenção."
    spamBot = SpamBot(message, 1, 30)
    spamBot.start_send_message()
