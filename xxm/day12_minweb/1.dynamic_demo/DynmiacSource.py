def application(head):
    if head == 'login.py':
        return login()
    if head == 'register.py':
        return register()
    else:
        return "no source"


def login():
    return 'login';


def register():
    return 'register'
