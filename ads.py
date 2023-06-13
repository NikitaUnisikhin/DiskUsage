"""
Ниже используется код из проекта пользователя RobinDavid
Ссылка на GitHub репозиторий: https://github.com/RobinDavid/pyADS
"""

from ctypes import *

kernel32 = windll.kernel32

LPSTR = c_wchar_p
DWORD = c_ulong
LONG = c_ulong
WCHAR = c_wchar * 296
LONGLONG = c_longlong


class LargeIntegerUnion(Structure):
    _fields_ = [
        ("LowPart", DWORD),
        ("HighPart", LONG)]


class LargeInteger(Union):
    _fields_ = [
        ("large1", LargeIntegerUnion),
        ("large2", LargeIntegerUnion),
        ("QuadPart",    LONGLONG)]


class Win32FindStreamData(Structure):
    _fields_ = [
        ("StreamSize", LargeInteger),
        ("cStreamName", WCHAR)]


def get_streams(path: str):
    file_inf = Win32FindStreamData()
    stream_list = list()

    findFirstStreamW = kernel32.FindFirstStreamW
    findFirstStreamW.restype = c_void_p

    my_handler = kernel32.FindFirstStreamW(LPSTR(path), 0, byref(file_inf), 0)

    p = c_void_p(my_handler)

    if file_inf.cStreamName:
        stream_name = file_inf.cStreamName.split(":")[1]
        if stream_name:
            stream_list.append(path + ":" + stream_name)

        while kernel32.FindNextStreamW(p, byref(file_inf)):
            stream_list.append(path + ":" + file_inf.cStreamName.split(":")[1])

    kernel32.FindClose(p)

    return stream_list
