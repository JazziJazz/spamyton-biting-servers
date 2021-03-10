import win32api, win32gui, win32con, json
from ..who_is_pythonline import SpamBot


class SpamythonMessage(SpamBot):
    def __init__(self, server_to_shooting: str, message_to_send: str, directory: str='../logs', filename: str='players', on_screen: bool=False):
        super().__init__(directory, filename)
        self.__server_to_shooting = server_to_shooting
        self.__message_to_send = message_to_send

        if on_screen is False:
            self.__on_screen = win32gui.FindWindowEx(None, None, None, self.__get_tibia_window())
        else:
            self.__on_screen = win32gui.FindWindowEx(None, None, None, on_screen)

        self.get_players_from_server(self.__server_to_shooting)


    def __get_tibia_window(self):
        def lista_de_janelas(hwnd, table):
            """Esse método privado tem um único proposito, procurar por todas janelas se existe alguma que contém a palavra Tibia como título.

            Args:
                hwnd ([array]): [Janela]
                table ([array]): [Array de Janelas]
            """
            if win32gui.IsWindowVisible(hwnd):
                table.append(win32gui.GetWindowText(hwnd))

        open_windows = []
        win32gui.EnumWindows(lista_de_janelas, open_windows)

        for window in open_windows:
            if ('Tibia' in window) or ('OTClient' in window):
                return window


    def shooting_messages(self):
        with open(f'{self._directory}/{self._filename}.json') as data_of_players:
            list_of_players = json.loads(data_of_players.read())

        #  Para cada jogador cadastrado dentro do arquívo JSON será executado as instruções abaixo.
        try:
            number_of_players = 0

            for player in list_of_players:
                message_to_send = f'* {player} * {self.__message_to_send}'

                for caracter in message_to_send:
                    win32api.PostMessage(self.__on_screen, win32con.WM_CHAR, ord(caracter), 0)
                    win32api.Sleep(10)

                win32api.PostMessage(self.__on_screen, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
                win32api.PostMessage(self.__on_screen, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

                for caracter in range(0, len(player) + 5):
                    win32api.PostMessage(self.__on_screen, win32con.WM_KEYDOWN, win32con.VK_BACK, 0)
                    win32api.Sleep(10)

                number_of_players += 1
                print(f'Uma mensagem \033[1;31macaba\033[0;0m de ser \033[1;31menviada\033[0;0m para o jogador \033[1;31m{player}\033[0;0m.')
        except KeyboardInterrupt:
            print(f'\nO programa foi \033[1;31mencerrado precocemente\033[0;0m você atingiu um total de \033[1;32m{number_of_players}\033[0;0m jogadores.')
        else:
            print(f'\nA lista de players \033[1;31acabou\033[0;0m, você atingiu um total de \033[1;32m{number_of_players}\033[0;0m jogadores.')
