list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
players_count = len(list_players)
half = int(players_count/2)
team_1 = list_players[0:half]
team_2 = list_players[half:]
print(team_1)
print(team_2)