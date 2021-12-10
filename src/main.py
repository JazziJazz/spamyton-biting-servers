from modules.spamBot import SpamBot


if __name__ == "__main__":
    message = "Isso é um teste!"

    spamBot = SpamBot(message, 1, 30)
    spamBot.start_send_message()
