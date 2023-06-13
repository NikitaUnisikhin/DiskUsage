import argparse

from ads import get_streams
from conclusion import make_conclusion, get_readable_output_size
from directory_object import DirectoryObject
from file import File
from directory import Directory
from handle_base_options import handle_base_options, handle_separate_dirs
from handle_sort_options import make_sort
from handle_group_options import make_group


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", action='store_true')
    parser.add_argument("-r", "--human-readable", action='store_true')
    parser.add_argument("-s", "--summarize", action='store_true')
    parser.add_argument("-S", "--separate-dirs", action='store_true')
    parser.add_argument("-q", "--sort", type=int)
    parser.add_argument("-ge", "--group-extension", type=str)
    parser.add_argument("-go", "--group-owner", type=str)
    parser.add_argument("-gn", "--group-nesting", type=int)
    parser.add_argument("-gdc", "--group-date-create", type=str)
    parser.add_argument("-gtc", "--group-time-create", type=str)
    parser.add_argument("-gdl", "--group-date-last-change", type=str)
    parser.add_argument("-gtl", "--group-time-last-change", type=str)
    parser.add_argument("-ads", "--alternate-data-streams", action='store_true')
    parser.add_argument('path')
    args = parser.parse_args()

    progressbar_counter = 0

    target = DirectoryObject(args.path)
    if target.is_file():
        if args.alternate_data_streams:
            output_obj = [DirectoryObject(i) for i in get_streams(args.path)]
            output_obj.append(DirectoryObject(args.path))
            output, progressbar_counter = handle_separate_dirs(args, output_obj, progressbar_counter)
            return make_conclusion(args, output)
        file = File(target)
        progressbar_counter += 1
        size = file.get_size_byte(progressbar_counter)
        if args.human_readable:
            print(get_readable_output_size(size))
        else:
            print(size)
        return
    elif target.is_dir():
        dir = Directory(target)
    else:
        print("По данному пути ничего не найдено")
        return

    # Обработка параметров
    output_obj = handle_base_options(args, dir)

    # Сбор вывода
    output, progressbar_counter = handle_separate_dirs(args, output_obj, progressbar_counter)

    # Группировка
    output = make_group(args, output)

    # Сортировка
    make_sort(args, output)

    # Вывод
    make_conclusion(args, output)


if __name__ == '__main__':
    main()
