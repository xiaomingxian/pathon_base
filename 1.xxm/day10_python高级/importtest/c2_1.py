from common import clist
from common import cflag


def change():
    global cflag
    cflag = True
    clist.append(1)
