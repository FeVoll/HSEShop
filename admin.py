from main import Auth as auth
from main import Elements as elements
import csv
filename = 'goods.csv'
delimiter = ','
users_file = "admins.csv"
orders_file = 'orders_file.csv'
admins = {}


with open(users_file, encoding='utf-8') as cvs:
    py = csv.reader(cvs, delimiter = delimiter)

    rows = 0

    for row in py:
        if rows != 0:
            admins[str(row[0])] = str(row[1])
        rows += 1

auth.admin(admins)


def clear():
    with open(filename, newline='') as cvs:
        py = csv.reader(cvs, delimiter=',')
        goods_list = list(py)

    f = open(filename, "w")
    f.truncate()
    f.close()
    return goods_list


def edit():
    while True:
        with open(filename, newline='') as cvs:
            py = csv.reader(cvs, delimiter=delimiter)
            goods_list = list(py)

        n = 0
        for i in goods_list:
            if n == 0:
                print('Товары на складе')
                n += 1
            else:
                print(f'{n}) {i[0]} - {i[1]} шт. Цена {i[2]}')
                n += 1
        print('1) Редактировать кол-во')
        print('2) Редактировать цену')
        print('3) Выйти в главное меню')
        next = input()
        if next == '1':
            while True:
                while True:
                    try:
                        item = int(input('Введите товар\n'))
                        new = int(input('Введите кол-во\n'))
                        break
                    except ValueError:
                        print('Вводите только числа')
                try:
                    goods_list[item][1] = new
                    break
                except LookupError:
                    print('Нет такого товара')

            rows = goods_list

            f = open(filename, "w")
            f.truncate()
            f.close()

            with open(filename, 'w', newline='') as f:
                write = csv.writer(f)
                write.writerows(rows)
            print('Changed')

        elif next == '2':
            while True:
                while True:
                    try:
                        item = int(input('Введите товар\n'))
                        new = int(input('Введите новую цену\n'))
                        break
                    except ValueError:
                        print('Вводите только числа')
                try:
                    difference = int(goods_list[item][2]) - int(new)
                    goods_list[item][2] = new
                    break
                except LookupError:
                    print('Нет такого товара')

            rows = goods_list

            f = open(filename, "w")
            f.truncate()
            f.close()

            with open(filename, 'w', newline='') as f:
                write = csv.writer(f)
                write.writerows(rows)

            with open(orders_file, newline='') as ck:
                check = csv.reader(ck, delimiter=delimiter)
                n1 = 0
                for y in check:
                    if n1 == 0:
                        pass
                    elif n1 != 0:
                        if str(y[2]) == 'Created':
                            with open(orders_file, newline='') as cvs:
                                newlist = csv.reader(cvs, delimiter=delimiter)
                                orders1 = list(newlist)
                                n2 = 4
                                while n2 != len(orders1[n1]):
                                    if goods_list[item][0] == y[n2]:
                                        orders1[n1][3] = str(int(orders1[n1][3]) - difference)
                                    n2 += 1
                            f = open(orders_file, "w")
                            f.truncate()
                            f.close()
                            rows = orders1

                            with open(orders_file, 'w', newline='') as f:
                                write = csv.writer(f)
                                write.writerows(rows)
                            n2 += 1
                    n1 += 1
            print('Changed')
        elif next == '3':
            adminmenu()
        else:
            print('Неверная команда')
            edit()


        adminmenu()


def open_orders():
    while True:
        with open(orders_file, newline='') as cvs:
            orders = csv.reader(cvs, delimiter=delimiter)
            n = 0
            n2 = 0
            print('Открытые заказы::')
            for y in orders:
                if n == 0:
                    n += 1
                elif n != 0:
                    if y[2] == 'Paid' or y[2] == 'Send':
                        print(f'{n})Заказ {y[1]} на сумму {y[3]} рублей от пользователя {y[0]}. Статус заказа - {y[2]}')
                        n2 += 1
                        n += 1

            if n2 == 0:
                print('Заказы отсутсвуют')
            print()
            print('1)Редактировать статус заказа')
            print('2)Выйти в меню')
            next = input()
            if next == '1':
                edit_status()
            elif next == '2':
                adminmenu()
            else:
                print('Неверная команда')


def edit_status():
    while True:
        while True:
            try:
                id = int(input('Какой заказ вы хотите посмотреть?'))
                break
            except ValueError:
                print('Введите число')
        with open(orders_file, newline='') as cvs:
            orders = csv.reader(cvs, delimiter=delimiter)
            check = 0
            for f in orders:
                if f[2] == 'Paid' or f[2] == 'Send':
                    check += 1
            if 0 < id <= check:
                n = 0
                with open(orders_file, newline='') as cvs:
                    orders = csv.reader(cvs, delimiter=delimiter)
                    for y in orders:
                        if n == 0:
                            n += 1
                        elif n != 0:
                            if y[2] == 'Paid' or y[2] == 'Send':
                                n += 1
                                if str(id) == str(n - 1):
                                    print('Информация о заказе:')
                                    print()
                                    print('В заказе:')
                                    n2 = 4
                                    while n2 != len(y):
                                        print(y[n2])
                                        n2 += 1
                                    print()
                                    print(f'Общая сумма заказа: {y[3]} руб.')
                                    print()
                                    print(f'Статус заказа - {y[2]}')
                                    print('')

                                    while True:
                                        print('1)Изменить статус')
                                        print('2)Выйти в список заказов')
                                        print('3)Выйти в меню')
                                        next = input('')
                                        if next == '1':
                                            with open(orders_file, newline='') as cvs:
                                                to_list = csv.reader(cvs, delimiter=delimiter)
                                                order_list = list(to_list)
                                            with open(orders_file, newline='') as cvs:
                                                ord = csv.reader(cvs, delimiter=delimiter)
                                                n = 0
                                                n3 = 0
                                                for b in ord:
                                                    if b[2] == 'Paid' or b[2] == 'Send':
                                                        n += 1
                                                    if str(id) == str(n):
                                                        print('Выберите статус заказа:')
                                                        print()
                                                        print('1) Оплачено')
                                                        print('2) Отправлено')
                                                        print('3) Доставлено')
                                                        print()
                                                        print('4) В главное меню')
                                                        next = input()
                                                        if next == '1':
                                                            order_list[n3][2] = 'Paid'
                                                            f = open(orders_file, "w")
                                                            f.truncate()
                                                            f.close()
                                                            rows = order_list

                                                            with open(orders_file, 'w', newline='') as f:
                                                                write = csv.writer(f)
                                                                write.writerows(rows)
                                                            open_orders()
                                                        elif next == '2':
                                                            order_list[n3][2] = 'Send'
                                                            f = open(orders_file, "w")
                                                            f.truncate()
                                                            f.close()
                                                            rows = order_list

                                                            with open(orders_file, 'w', newline='') as f:
                                                                write = csv.writer(f)
                                                                write.writerows(rows)
                                                            open_orders()
                                                        elif next == '3':
                                                            order_list[n3][2] = 'Delivered'
                                                            f = open(orders_file, "w")
                                                            f.truncate()
                                                            f.close()
                                                            rows = order_list

                                                            with open(orders_file, 'w', newline='') as f:
                                                                write = csv.writer(f)
                                                                write.writerows(rows)
                                                            open_orders()
                                                        elif next == '4':
                                                            adminmenu()
                                                    n3 += 1
                                        elif next == '2':
                                            open_orders()
                                        elif next == '3':
                                            adminmenu()
                                        else:
                                            print('Неверная команда')
            else:
                print('Нет такого заказа')


def adminmenu():
    while True:
        print('Вы в админской панеле, что вы хотите сделать?')
        print('1) Редактировать кол-во или цену товаров')
        print('2) Просмотр открытых заказов')
        while True:
            try:
                next_step = str(input())
                break
            except ValueError:
                print('Введите цифру')
        if next_step == '1':
            edit()
            elements.show()
            break
        elif next_step == '2':
            open_orders()
        else:
            print('Неверная команда')

adminmenu()