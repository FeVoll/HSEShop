import csv

filename = 'goods.csv'
delimiter = ','
orders_file = 'orders_file.csv'


class Auth:

    def __init__(self):
        pass

    def admin(users):
        while True:
            print('Вход в админ-панель:')
            log = str(input('Логин:\n'))
            pasw = str(input('Пароль:\n'))
            if log in users and users[log] == pasw:
                print('Админская панель')
                break
            else:
                print('Неверый логин или пароль')

    def user(users):
        while True:
            print('Вход в магазин:')
            log = str(input('Логин:\n'))
            pasw = str(input('Пароль:\n'))
            if log in users and users[log] == pasw:
                print('Магазин')
                break
            else:
                print('Неверый пароль')
        return log


class Elements:
    def __init__(self):
        pass

    def show():
        with open(filename, newline='') as cvs:
            py = csv.reader(cvs, delimiter=delimiter)
            n = 0
            for i in py:
                if n == 0:
                    print('Товары на складе')
                    n += 1
                else:
                    if str(i[1]) != str(0):
                        print(f'{n}) {i[0]} - {i[1]} шт. Цена: {i[2]}')
                        n += 1
                    else:
                        print(f'{i[0]} нет на складе.')


