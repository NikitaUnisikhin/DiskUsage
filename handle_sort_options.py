def make_sort(args, output):
    """
    Обработка параметров сортировки
    """
    sort_keys = {
        # сортировка по size
        1: size_sort_key,
        # сортировка по путю (название)
        2: name_sort_key,
        # сортировка по времени последнего изменения
        3: time_latest_modification_sort_key,
        # сортировка по времени создания
        4: time_create_sort_key
    }

    if args.sort:
        for code, sort_key in sort_keys.items():
            if args.sort == code and code == 1:
                output.sort(key=sort_key, reverse=True)
            elif args.sort == code:
                output.sort(key=sort_key)


def size_sort_key(a):
    return a[0]


def name_sort_key(a):
    return a[1].Path


def time_latest_modification_sort_key(a):
    return a[1].get_time_latest_modification()


def time_create_sort_key(a):
    return a[1].get_time_create()