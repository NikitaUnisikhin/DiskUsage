import time


def continue_progress_bar(i):
    if i > 100:
        return
    elif i == 100:
        print(i, end='\n\r')
    elif i > 51:
        print(i, end='\r')
    else:
        print(i, '=' * i, end='\r')
    time.sleep(0.1)
