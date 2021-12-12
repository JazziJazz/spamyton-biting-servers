from ..whoIsPyth import *


class ServerFactory(ABC):
    def __init__(self, server_name) -> None:
        self.server = self.get_server_info(server_name)

    @staticmethod
    def get_server_info(server_name: str) -> Server:
        if (server_name == "Kaldrox"):
            return KaldroxStrategy()
        elif (server_name == "IceWar"):
            return IceWarStrategy()
        elif (server_name == "Demolidores"):
            return DemolidoresStrategy()
        elif (server_name == "Ilusions"):
            return IlusionsStrategy()
        elif (server_name == "NewTibia"):
            return NewTibiaStrategy()
        elif (server_name == "Canob"):
            return CanobStrategy()
        elif (server_name == "Pbot"):
            return PbotStrategy()
        elif (server_name == "Ziron"):
            return ZironStrategy()
        elif (server_name == "Pesadao"):
            return PesadaoStrategy()
        elif (server_name == "Underwar"):
            return UnderwarStrategy()
        else:
            assert 0, f"\n\n\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\nServidor não encontrado na base de dados.\n— Verifique se você digitou corretamente."

    def get_players_online(self, randomized_list: bool = False):
        self.server.get_players_online(randomized_list)
