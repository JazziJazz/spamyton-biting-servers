import os
import re
import json
import random
import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class PlayersNotFoundError(Exception):
    pass


class Server(ABC):
    @abstractmethod
    def get_players_online(self, randomized_list: bool = False) -> None: pass


class KaldroxStrategy(Server):
    def get_players_online(self, randomized_list: bool = False) -> None:
        body = requests.get(
            "https://www.kaldrox.com/?subtopic=whoisonline").content
        soup = BeautifulSoup(body, "html.parser")
        data = {"player": [], "online": 0}

        try:
            for error in soup.find_all("h3"):
                if ("Error occured!" in error.get_text()):
                    raise PlayersNotFoundError

            for player in soup.find_all("a"):
                if (player.get_text() != "" and "?subtopic=characters&name=" in player.get("href")):
                    if (re.match("\d", player.get_text().strip())):
                        player_name = player.get_text(
                        ).strip().split("-")[1].strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1
                    else:
                        player_name = player.get_text().strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1

            if randomized_list:
                random.shuffle(data["player"], random.random)

            print(
                f"\u2705 Requisição efetuada com sucesso:\n\n— Há um total de: \033[1;32m{ data['online'] }\033[0m jogadores online nesse servidor.\nCorram para plataforma 9¾!")

            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\..\..\..\logs")) + "\players.json"

            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except PlayersNotFoundError:
            print(
                f"\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\n— Nenhum player pode ser encontrado, o documento não foi atualizado.\nIsso só pode ser obra do 😈.")


class IceWarStrategy(Server):
    def get_players_online(self, randomized_list: bool = False) -> None:
        body = requests.get(
            "https://baiak-icewar.com/?subtopic=whoisonline").content
        soup = BeautifulSoup(body, "html.parser")
        data = {"player": [], "online": 0}

        try:
            for error in soup.find_all("h3"):
                if ("Error occured!" in error.get_text()):
                    raise PlayersNotFoundError

            for player in soup.find_all("a"):
                if (player.get_text() != "" and "?subtopic=characters&name=" in player.get("href")):
                    if (re.match("\d", player.get_text().strip())):
                        player_name = player.get_text(
                        ).strip().split("-")[1].strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1
                    else:
                        player_name = player.get_text().strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1

            if randomized_list:
                random.shuffle(data["player"], random.random)

            print(
                f"\u2705 Requisição efetuada com sucesso:\n\n— Há um total de: \033[1;32m{ data['online'] }\033[0m jogadores online nesse servidor.\nCorram para plataforma 9¾!")

            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\..\..\..\logs")) + "\players.json"

            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except PlayersNotFoundError:
            print(
                f"\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\n— Nenhum player pode ser encontrado, o documento não foi atualizado.\nIsso só pode ser obra do 😈.")


class DemolidoresStrategy(Server):
    def get_players_online(self, randomized_list: bool = False) -> None:
        body = requests.get(
            "https://www.demolidores.com.br/?subtopic=whoisonline").content
        soup = BeautifulSoup(body, "html.parser")
        data = {"player": [], "online": 0}

        try:
            for error in soup.find_all("h3"):
                if ("Error occured!" in error.get_text()):
                    raise PlayersNotFoundError

            for player in soup.find_all("a"):
                if (player.get_text() != "" and "?subtopic=characters&name=" in player.get("href")):
                    if (re.match("\d", player.get_text().strip())):
                        player_name = player.get_text(
                        ).strip().split("-")[1].strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1
                    else:
                        player_name = player.get_text().strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1

            if randomized_list:
                random.shuffle(data["player"], random.random)

            print(
                f"\u2705 Requisição efetuada com sucesso:\n\n— Há um total de: \033[1;32m{ data['online'] }\033[0m jogadores online nesse servidor.\nCorram para plataforma 9¾!")

            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\..\..\..\logs")) + "\players.json"

            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except PlayersNotFoundError:
            print(
                f"\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\n— Nenhum player pode ser encontrado, o documento não foi atualizado.\nIsso só pode ser obra do 😈.")


class IlusionsStrategy(Server):
    def get_players_online(self, randomized_list: bool = False) -> None:
        body = requests.get(
            "https://www.baiak-ilusion.com/?subtopic=whoisonline").content
        soup = BeautifulSoup(body, "html.parser")
        data = {"player": [], "online": 0}

        try:
            for error in soup.find_all("h3"):
                if ("Error occured!" in error.get_text()):
                    raise PlayersNotFoundError

            for player in soup.find_all("a"):
                if (player.get_text() != "" and "?subtopic=characters&name=" in player.get("href")):
                    if (re.match("\d", player.get_text().strip())):
                        player_name = player.get_text(
                        ).strip().split("-")[1].strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1
                    else:
                        player_name = player.get_text().strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1

            if randomized_list:
                random.shuffle(data["player"], random.random)

            print(
                f"\u2705 Requisição efetuada com sucesso:\n\n— Há um total de: \033[1;32m{ data['online'] }\033[0m jogadores online nesse servidor.\nCorram para plataforma 9¾!")

            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\..\..\..\logs")) + "\players.json"

            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except PlayersNotFoundError:
            print(
                f"\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\n— Nenhum player pode ser encontrado, o documento não foi atualizado.\nIsso só pode ser obra do 😈.")


class NewTibiaStrategy(Server):
    def get_players_online(self, randomized_list: bool = False) -> None:
        body = requests.get(
            "https://www.newtibia.com/?subtopic=whoisonline").content
        soup = BeautifulSoup(body, "html.parser")
        data = {"player": [], "online": 0}

        try:
            for error in soup.find_all("h3"):
                if ("Error occured!" in error.get_text()):
                    raise PlayersNotFoundError

            for player in soup.find_all("a"):
                if (player.get_text() != "" and "?subtopic=characters&name=" in player.get("href")):
                    if (re.match("\d", player.get_text().strip())):
                        player_name = player.get_text(
                        ).strip().split("-")[1].strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1
                    else:
                        player_name = player.get_text().strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1

            if randomized_list:
                random.shuffle(data["player"], random.random)

            print(
                f"\u2705 Requisição efetuada com sucesso:\n\n— Há um total de: \033[1;32m{ data['online'] }\033[0m jogadores online nesse servidor.\nCorram para plataforma 9¾!")

            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\..\..\..\logs")) + "\players.json"

            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except PlayersNotFoundError:
            print(
                f"\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\n— Nenhum player pode ser encontrado, o documento não foi atualizado.\nIsso só pode ser obra do 😈.")


class CanobStrategy(Server):
    def get_players_online(self, randomized_list: bool = False) -> None:
        body = requests.get(
            "https://tibiacanob.com/onlinelist").content
        soup = BeautifulSoup(body, "html.parser")
        data = {"player": [], "online": 0}

        try:
            for error in soup.find_all("h3"):
                if ("Error occured!" in error.get_text()):
                    raise PlayersNotFoundError

            for player in soup.find_all("a"):
                if (player.get_text() != "" and "characterprofile.php?name=" in player.get("href")):
                    if (re.match("\d", player.get_text().strip())):
                        player_name = player.get_text(
                        ).strip().split("-")[1].strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1
                    else:
                        player_name = player.get_text().strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1


            if randomized_list:
                random.shuffle(data["player"], random.random)

            print(
                f"\u2705 Requisição efetuada com sucesso:\n\n— Há um total de: \033[1;32m{ data['online'] }\033[0m jogadores online nesse servidor.\nCorram para plataforma 9¾!")

            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\..\..\..\logs")) + "\players.json"

            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except PlayersNotFoundError:
            print(
                f"\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\n— Nenhum player pode ser encontrado, o documento não foi atualizado.\nIsso só pode ser obra do 😈.")


class PbotStrategy(Server):
    def get_players_online(self, randomized_list: bool = False) -> None:
        body = requests.get(
            "https://pbotwars.com.br/?subtopic=whoisonline").content
        soup = BeautifulSoup(body, "html.parser")
        data = {"player": [], "online": 0}

        try:
            for error in soup.find_all("h3"):
                if ("Error occured!" in error.get_text()):
                    raise PlayersNotFoundError

            for player in soup.find_all("a"):
                if (player.get_text() != "" and "?subtopic=characters&name=" in player.get("href")):
                    if (re.match("\d", player.get_text().strip())):
                        player_name = player.get_text(
                        ).strip().split("-")[1].strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1
                    else:
                        player_name = player.get_text().strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1

            if randomized_list:
                random.shuffle(data["player"], random.random)

            print(
                f"\u2705 Requisição efetuada com sucesso:\n\n— Há um total de: \033[1;32m{ data['online'] }\033[0m jogadores online nesse servidor.\nCorram para plataforma 9¾!")

            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\..\..\..\logs")) + "\players.json"

            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except PlayersNotFoundError:
            print(
                f"\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\n— Nenhum player pode ser encontrado, o documento não foi atualizado.\nIsso só pode ser obra do 😈.")


class ZironStrategy(Server):
    def get_players_online(self, randomized_list: bool = False) -> None:
        body = requests.get(
            "http://baiakziron.com/?subtopic=whoisonline").content
        soup = BeautifulSoup(body, "html.parser")
        data = {"player": [], "online": 0}

        try:
            for error in soup.find_all("h3"):
                if ("Error occured!" in error.get_text()):
                    raise PlayersNotFoundError

            for player in soup.find_all("a"):
                if (player.get_text() != "" and "?subtopic=characters&name=" in player.get("href")):
                    if (re.match("\d", player.get_text().strip())):
                        player_name = player.get_text(
                        ).strip().split("-")[1].strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1
                    else:
                        player_name = player.get_text().strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1

            if randomized_list:
                random.shuffle(data["player"], random.random)

            print(
                f"\u2705 Requisição efetuada com sucesso:\n\n— Há um total de: \033[1;32m{ data['online'] }\033[0m jogadores online nesse servidor.\nCorram para plataforma 9¾!")

            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\..\..\..\logs")) + "\players.json"

            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except PlayersNotFoundError:
            print(
                f"\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\n— Nenhum player pode ser encontrado, o documento não foi atualizado.\nIsso só pode ser obra do 😈.")


class PesadaoStrategy(Server):
    def get_players_online(self, randomized_list: bool = False) -> None:
        body = requests.get(
            "https://baiakpesadao.com/?subtopic=whoisonline").content
        soup = BeautifulSoup(body, "html.parser")
        data = {"player": [], "online": 0}

        try:
            for error in soup.find_all("h3"):
                if ("Error occured!" in error.get_text()):
                    raise PlayersNotFoundError

            for player in soup.find_all("a"):
                if (player.get_text() != "" and "?subtopic=characters&name=" in player.get("href")):
                    if (re.match("\d", player.get_text().strip())):
                        player_name = player.get_text(
                        ).strip().split("-")[1].strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1
                    else:
                        player_name = player.get_text().strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1

            if randomized_list:
                random.shuffle(data["player"], random.random)

            print(
                f"\u2705 Requisição efetuada com sucesso:\n\n— Há um total de: \033[1;32m{ data['online'] }\033[0m jogadores online nesse servidor.\nCorram para plataforma 9¾!")

            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\..\..\..\logs")) + "\players.json"

            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except PlayersNotFoundError:
            print(
                f"\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\n— Nenhum player pode ser encontrado, o documento não foi atualizado.\nIsso só pode ser obra do 😈.")


class UnderwarStrategy(Server):
    def get_players_online(self, randomized_list: bool = False) -> None:
        body = requests.get(
            "https://www.underwar.org/?subtopic=community&page=whoisonline").content
        soup = BeautifulSoup(body, "html.parser")
        data = {"player": [], "online": 0}

        try:
            for error in soup.find_all("h3"):
                if ("Error occured!" in error.get_text()):
                    raise PlayersNotFoundError

            for player in soup.find_all("a"):
                if (player.get_text() != "" and "?subtopic=community&page=characters&server=UnderWar&name=" in player.get("href") and "[" not in player.get_text() and "]" not in player.get_text()):
                    if (re.match("\d", player.get_text().strip())):
                        player_name = player.get_text(
                        ).strip().split("-")[1].strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1
                    else:
                        player_name = player.get_text().strip()

                        data["player"].append({"name": player_name})
                        data["online"] += 1

            if randomized_list:
                random.shuffle(data["player"], random.random)

            print(
                f"\u2705 Requisição efetuada com sucesso:\n\n— Há um total de: \033[1;32m{ data['online'] }\033[0m jogadores online nesse servidor.\nCorram para plataforma 9¾!")

            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\..\..\..\logs")) + "\players.json"

            with open(path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except PlayersNotFoundError:
            print(
                f"\u274E \033[1;31mAlgo deu errado na requisição\033[0m:\n\n— Nenhum player pode ser encontrado, o documento não foi atualizado.\nIsso só pode ser obra do 😈.")
