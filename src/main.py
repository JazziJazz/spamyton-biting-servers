from modules.spamBot import SpamBot
from modules.pythOnline.factory import ServerFactory


if __name__ == "__main__":
    # server = ServerFactory("IceWar")
    # server.get_players_online(randomized_list=True)

    message = "Isso é um teste de algo que estou programando, por favor não responda, ignore a mensagem. Obrigado pela atenção."
    spamBot = SpamBot(message, 1, 30)
    spamBot.start_send_message()
