import requests, json
from bs4 import BeautifulSoup


class SpamBot:
    def __init__(self, directory: str='../logs', filename: str='players'):
        self._directory = directory
        self._filename = filename


    def get_players_from_server(self, server_name):
        my_server = []

        for server in self.get_servers_list():
            if server_name.title() in server:
                my_server.append(server)
                break

        if my_server:
            html_to_analyze = requests.get(my_server[0][1]).content
            my_soup = BeautifulSoup(html_to_analyze, 'html.parser')
            table_containing_players = my_soup.find_all('table', {"width": "100%"})[1]

            dados_do_player, total_of_players = {}, 0

            for tr in table_containing_players.find_all('tr')[1::]:
                string_to_return = []
                total_of_players += 1

                for td in tr:
                    player = td.text.replace("\u00a0", " ")
                    if player[-1] == " ":
                        player = player[:-1]

                    string_to_return.append(player)

                dados_do_player[string_to_return[0]] = [{"level": string_to_return[1], "vocation": string_to_return[2]}]
        else:
            return print(f"O servidor informado por você se chama \033[1;31m{server_name}\033[0;0m. Ele \033[1;31mnão está cadastrado\033[0;0m em nosso banco de dados, verifique se você digitou o nome corretamente.")

        directory_to_send = self._directory + "/" + self._filename + ".json"

        with open(directory_to_send, 'w') as json_file:
            json.dump(dados_do_player, json_file, indent=4)

        return print(f"Arquívo \033[1;32mJSON\033[0;0m criado!\nHá um total de \033[1;32m{total_of_players}\033[0;0m players online no servidor \033[1;32m{server_name}\033[0;0m.\n")


    def get_servers_list(self, typeS=None):
        list_of_servers = [['Baiak Illusions', 'https://baiak-ilusion.com/?subtopic=whoisonline']]
        string_to_return = "Os servidores disponíveis são: "

        for server in list_of_servers:
            string_to_return += f'\033[1;32m{server[0]}\033[0;0m, '

        string_to_return = string_to_return[:-2]

        if typeS is not None:
            return print(string_to_return + ".")
        else:
            return list_of_servers


    def get_information_about_servers(self):
        string_of_information = f'Nós temos um total de \033[1;31m{len(self.getServersList())}\033[0;0m servidor(es) cadastrado(s) em nosso sistema. Para receber um \033[1;31mJSON\033[0;0m de players online de algum servidor basta rodar o método \033[1;32mgetPlayersFromServer()\033[0;0m utilizando como argumento para o parâmetro o nome do servidor.'

        return print(string_of_information)
