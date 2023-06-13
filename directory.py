import os
from directory_object import DirectoryObject


class Directory(DirectoryObject):
    """
    Класс каталога
    """
    def __init__(self, directory_object: DirectoryObject):
        super().__init__(directory_object.Path)

    def get_deep_list_directory_objects(self):
        """
        Получение всех файлов/каталогов каталога (в том числе все вложенные)
        """
        all_files = os.walk(self.Path)
        output = list()
        for obj in all_files:
            output.append(obj[0])
            for file in obj[2]:
                output.append(os.path.join(obj[0], file))

        return [DirectoryObject(i) for i in output]

    def get_list_directory_objects(self):
        """
        Получение всех каталогов в каталоге (без вложенных)
        """
        return [DirectoryObject(i) for i in os.listdir(self.Path)]

    def get_size_without_nested_directories(self, j):
        """
        Получение размера каталога без учета вложенных файлов/каталогов
        """
        return sum([i.get_size_byte(j) for i in self.get_list_directory_objects() if i.is_file()])

