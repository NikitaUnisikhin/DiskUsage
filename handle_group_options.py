import os
import datetime


def make_group(args, output):
    """
    Обработка параметров группировки
    """
    if args.group_extension:
        # расширение
        extension = args.group_extension
        output = [i for i in output if f'.{extension}' in i[1].Path]

    if args.group_owner:
        # владелец
        owner = args.group_owner
        output = [i for i in output if i[1].get_owner() == owner]

    if args.group_nesting:
        # уровень вложенности
        nesting = args.group_nesting
        sep = os.sep
        count_sep_in_path = args.path.count(sep)
        output = [i for i in output if i[1].Path.count(sep) == (count_sep_in_path + nesting)]

    if args.group_date_create:
        # дата создания
        data = args.group_date_create
        try:
            datetime.datetime.strptime(data, '%d.%m.%Y')
            output = [i for i in output if i[1].get_date_create() == data]
        except ValueError:
            print("Неверный формат даты (d.m.Y). Сортировка по дате создания не произведена")

    if args.group_time_create:
        # время создания с точностью до минут
        time = args.group_time_create
        try:
            datetime.datetime.strptime(time, '%H.%M')
            output = [i for i in output if i[1].get_readable_time_create() == time]
        except ValueError:
            print("Неверный формат времени (H.M). Сортировка по времени создания не произведена")

    if args.group_date_last_change:
        # дата последнего изменения
        data = args.group_date_last_change
        try:
            datetime.datetime.strptime(data, '%d.%m.%Y')
            output = [i for i in output if i[1].get_date_last_change() == data]
        except ValueError:
            print("Неверный формат даты (d.m.Y). Сортировка по дате создания не произведена")

    if args.group_time_last_change:
        # время последнего изменения с точностью до минут
        time = args.group_time_last_change
        try:
            datetime.datetime.strptime(time, '%H.%M')
            output = [i for i in output if i[1].get_readable_time_last_change() == time]
        except ValueError:
            print("Неверный формат времени (H.M). Сортировка по времени создания не произведена")

    return output
