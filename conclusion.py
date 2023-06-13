def get_readable_output_size(size):
    """
    Приводит размер из байтов в более читаемый вид
    """
    if size > 1e+9 + 73741824:
        return f"{round(size / (1e+9 + 73741824), 1)}G"
    elif size > 1e+6 + 48576:
        return f"{round(size / (1e+6 + 48576), 1)}M"
    elif size > 1024:
        return f"{round(size / 1024, 1)}K"
    return 0


def make_conclusion(args, output):
    """
    Конечный вывод в консоль с учетом параметра human_readable
    """
    if len(output) == 0:
        print("No files")
        return

    if args.human_readable:
        max_len_size = max([len(str(get_readable_output_size(i[0]))) for i in output])
        for obj in output:
            size = str(get_readable_output_size(obj[0]))
            print(f"{size}{' ' * (max_len_size - len(size))}    {obj[1].Path}")
    else:
        max_len_size = max([len(str(i[0])) for i in output])
        for obj in output:
            size = str(obj[0])
            print(f"{obj[0]}{' ' * (max_len_size - len(size))}    {obj[1].Path}")
