from directory_object import DirectoryObject


class File(DirectoryObject):
    """
    Класс файла
    """
    def __init__(self, directory_object: DirectoryObject):
        super().__init__(directory_object.Path)
