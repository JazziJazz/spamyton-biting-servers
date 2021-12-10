import os
import json
import win32api
import win32gui
import win32con
from time import sleep
from abc import ABC, abstractmethod


class Bot:
    @abstractmethod
    def __find_tibia_window(self) -> None:
        pass

    @abstractmethod
    def start_send_message(self) -> None:
        pass


class SpamBot(Bot):
    def __init__(self, message_to_send: str, seconds_beetween_message: int, ms_speed: int = 2) -> None:
        self.message = message_to_send
        self.time = seconds_beetween_message
        self.speed = ms_speed
        self.__tibia_window = win32gui.FindWindowEx(
            None, None, None, self.__find_tibia_window())

    def __find_tibia_window(self) -> None:
        def list_of_windows(hwnd, table):
            if win32gui.IsWindowVisible(hwnd):
                table.append(win32gui.GetWindowText(hwnd))

        opened_windows = []
        win32gui.EnumWindows(list_of_windows, opened_windows)

        for window in opened_windows:
            if ('Tibia' in window) or ('OTC' in window):
                return window

    def start_send_message(self) -> None:
        path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "../..")) + "/players.json"
        messages_sent = 0

        with open(path) as data:
            players_data = json.loads(data.read())

        try:
            # Para cada jogador dentro do JSON.
            for player in players_data["player"]:
                message = f"*{player['name']}* {self.message}"

                """Para cada caracter dentro da mensagem ele vai escrever e depois dormir. Esse tempo que
                ele passa ocioso é necessário para que computadores com processadores fracos não percam
                dados da mensagem durante o processo de escrita."""
                for caracter in message:
                    win32api.PostMessage(
                        self.__tibia_window, win32con.WM_CHAR, ord(caracter), 0)
                    win32api.Sleep(self.speed)

                # Enter é pressionado.
                win32api.PostMessage(
                    self.__tibia_window, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
                win32api.PostMessage(self.__tibia_window,
                                     win32con.WM_KEYUP, win32con.VK_RETURN, 0)

                """Pressionamos a tecla de deleção (backspace) o número total de vezes de caracteres que
                há no nome do jogador. Ele aperta mais cinco vezes só para ter garantia que a caixa de
                escrita está limpa antes de digitar a próxima mensagem."""
                for caracter in range(0, len(player["name"]) + 5):
                    win32api.PostMessage(
                        self.__tibia_window, win32con.WM_KEYDOWN, win32con.VK_BACK, 0)
                    win32api.PostMessage(
                        self.__tibia_window, win32con.WM_KEYUP, win32con.VK_BACK, 0)
                    win32api.Sleep(self.speed)

                messages_sent += 1
                print(
                    f"✔️  Uma mensagem foi enviada com sucesso para o jogador {player['name']}. ")
                sleep(self.time)
        except:
            print(f"\n💀 Programa encerrado subitamente!\nUm total de {messages_sent} jogadores foram atingidos antes que o programa fosse encerrado.\n\n— Erro 404: O programa pode ter sido encerrado pelo próprio usuário do sistema ou devido ao banimento do personagem dentro do servidor, ou porquê a janela do seu client não foi encontrada.")

            return None
        else:
            print(
                f"\n❤️ O programa atingiu seu objetivo com sucesso! ☆ (✿◠‿◠) ٩(̃-.-)۶ ٩(-̮̮̃•-)۶ ☆\n um total de {messages_sent} foram atingidos com sucesso, a lista de jogadores chegou ao fim e esse foi o término do programa.")

            return None
