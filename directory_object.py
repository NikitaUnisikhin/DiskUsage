import os
import win32security
from ads import get_streams
from progressbar import continue_progress_bar
from pathlib import Path
import platform
import datetime


class DirectoryObject:
    """
    Класс объекта файловой системы (файл/каталог)
    """
    def __init__(self, path: str):
        self.Path = path

    def is_file(self):
        return os.path.isfile(self.Path)

    def is_dir(self):
        return os.path.isdir(self.Path)

    def get_size_byte(self, i):
        """
        Получение объема объекта в байтах с учетом всех вложенных объектов
        """
        continue_progress_bar(i)

        if self.is_file():
            return os.path.getsize(self.Path)
        else:
            summer = 0
            for obj in os.walk(self.Path):
                for file in obj[2]:
                    summer += os.path.getsize(os.path.join(obj[0], file))

            return summer

    def get_time_latest_modification(self):
        return os.path.getmtime(self.Path)

    def get_time_create(self):
        return os.path.getctime(self.Path)

    def get_readable_time_create(self):
        """
        Выводит время создания в формате %H.%M
        """
        return datetime.datetime.fromtimestamp(self.get_time_create()).strftime('%H.%M')

    def get_readable_time_last_change(self):
        """
        Выводит время создания в формате %H.%M
        """
        return datetime.datetime.fromtimestamp(self.get_time_latest_modification()).strftime('%H.%M')

    def get_date_create(self):
        """
        Выводит дату создания в формате %d.%m.%Y
        """
        return datetime.datetime.fromtimestamp(self.get_time_create()).strftime('%d.%m.%Y')

    def get_date_last_change(self):
        """
        Выводит дату создания в формате %d.%m.%Y
        """
        return datetime.datetime.fromtimestamp(self.get_time_latest_modification()).strftime('%d.%m.%Y')

    def get_owner(self):
        if platform.system() == 'Linux':
            return Path(self.Path).owner()
        elif platform.system() == 'Windows':
            sd = win32security.GetFileSecurity(self.Path, win32security.OWNER_SECURITY_INFORMATION)
            owner_sid = sd.GetSecurityDescriptorOwner()
            name, domain, type = win32security.LookupAccountSid(None, owner_sid)
            return name

    def get_metadata(self):
        if self.get_fs_type() == "NTFS":
            return get_streams(self.Path)

    def get_fs_type(self):
        root_type = ""
        for part in psutil.disk_partitions():
            if part.mountpoint == '/':
                root_type = part.fstype
                continue

            if self.Path.startswith(part.mountpoint):
                return part.fstype

        return root_type


