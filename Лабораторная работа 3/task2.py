# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator = ','):
    first_group_splited = first_group.split(separator)
    second_group_splited = second_group.split(separator)
    intersection_list = list(set(first_group_splited).intersection(set(second_group_splited)))
    intersection_list.sort()
    return intersection_list
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
intersection_list = find_common_participants(participants_first_group, participants_second_group)
print(intersection_list)