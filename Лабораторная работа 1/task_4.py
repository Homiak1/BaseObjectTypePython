users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
stat = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
length = len(users)
unique = set(users)
stat["Общее количество"] = length
stat["Уникальные посещения"] = len(list(map(str, unique)))
print(stat)