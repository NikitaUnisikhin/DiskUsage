from ads import get_streams
from directory import Directory
from directory_object import DirectoryObject


def handle_separate_dirs(args, output_obj, progressbar_counter):
    output = list()
    if args.separate_dirs:
        for obj in output_obj:
            progressbar_counter += 1
            if obj.is_dir():
                obj = Directory(obj)
                output.append((obj.get_size_without_nested_directories(progressbar_counter), obj))
            else:
                output.append((obj.get_size_byte(progressbar_counter), obj))
    else:
        for obj in output_obj:
            progressbar_counter += 1
            output.append((obj.get_size_byte(progressbar_counter), obj))

    return output, progressbar_counter


def handle_base_options(args, dir):
    """
    Обработка базовых опций (все, кроме сортировок и группировок)
    """
    list_files = dir.get_deep_list_directory_objects()

    # выводим только размер
    if args.summarize:
        return [dir]

    # при наличии параметра рассматриваем и файлы и катологи (без - только каталоги)
    if args.all:
        output_obj = list_files
    else:
        output_obj = [i for i in list_files if not i.is_file()]

    # при налчии параметра в список файлов/каталогов добавляем все их метаданные
    if args.alternate_data_streams:
        meta_data = list()
        for obj in output_obj:
            streams = get_streams(obj.Path)
            if len(streams) != 0:
                for stream in streams:
                    meta_data.append(DirectoryObject(stream))
        output_obj += meta_data

    return output_obj
