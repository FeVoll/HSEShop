from main import Auth as auth
from main import Elements as elements
import csv
import random
import time


users_file = "users.csv"
goods_file = "goods.csv"
delimiter = ","
filename = 'goods.csv'
orders_file = 'orders_file.csv'
users = {}


def new_id():
    id = random.getrandbits(32)
    return id


def check_id():
    while True:
        with open(orders_file, newline='') as cvs:
            py = csv.reader(cvs, delimiter=delimiter)
            a = str(new_id())
            for i in py:
                if str(i[1]) == a:
                    pass
                elif str(i[1]) != a:
                    break
        return a


def check_on_cart():
    with open(orders_file, newline='') as ba:
        orders = csv.reader(ba)
        check = 0
        for y in orders:
            if str(log) == str(y[0]) and str(y[2]) == 'Created':
                check += 1
        if check == 0:
            with open(orders_file, 'a', newline='') as ord:
                write = csv.writer(ord)
                write.writerow([log, str(check_id()), 'Created', '0'])


with open(users_file, encoding='utf-8') as cvs:
    py = csv.reader(cvs, delimiter=delimiter)

    rows = 0

    for row in py:
        if rows != 0:
            users[str(row[0])] = str(row[1])
        rows += 1

log = auth.user(users)
check_on_cart()


def list_of_goods():
    with open(goods_file, newline='') as cvs:
        py = csv.reader(cvs, delimiter=delimiter)
        goods_list = list(py)
    return goods_list


def mainmenu():
    while True:
        print('Доступные действия:')
        print('1)Посмотреть каталог')
        print('2)Просмотр корзины')
        print('3)Мои заказы')
        while True:
            try:
                next_step = int(input("Что вы хотите сделать?\n"))
                break
            except ValueError:
                print('Введите цифру')
        if next_step == 1:
            order()
        elif next_step == 2:
            card()
        elif next_step == 3:
            show_all_orders()
        else:
            print('Неверная команда')


def order():
    while True:
        elements.show()
        print('1) - Добавить в корзину какой-то товар')
        print('2) - Выйти в главное меню')
        next_step = input()
        if next_step == '1':
            add_to_cart()
        elif next_step == '2':
            mainmenu()
        else:
            print('Неверная команда')


def checkonstorage():
    noton = 0
    with open(orders_file, newline='') as ck:
        py = csv.reader(ck, delimiter=delimiter)
        orders = list(py)
    with open(orders_file, newline='') as ck:
        check = csv.reader(ck, delimiter=delimiter)
        n1 = 0
        n2 = 0
        for y in check:
            if n1 == 0:
                pass
            elif n1 != 0:
                if str(y[0]) == str(log) and str(y[2]) == 'Created':
                    with open(goods_file, newline='') as sklad:
                        goods = csv.reader(sklad, delimiter=delimiter)
                        for i in goods:
                            if n2 == 0:
                                pass
                            elif n2 != 0:
                                if i[0] in orders[n1]:
                                    with open(filename, newline='') as cvs:
                                        edit = csv.reader(cvs, delimiter=delimiter)
                                        goods_list = list(edit)
                                    checkrow = 0
                                    for d in goods_list:
                                        if checkrow == 0:
                                            pass
                                        else:
                                            if goods_list[checkrow][0] == i[0]:
                                                if int(goods_list[checkrow][1]) - 1 < 0:
                                                    print(f'{goods_list[checkrow][0]} закончился на складе')
                                                    noton += 1
                                        checkrow += 1
                            n2 += 1
            n1 += 1
    if noton == 0:
        with open(goods_file, newline='') as sklad:
            goods = csv.reader(sklad, delimiter=delimiter)
            for k in goods:

                row = 0
                for d in goods_list:
                    if row == 0:
                        pass
                    else:
                        with open(filename, newline='') as cvs:
                            edit = csv.reader(cvs, delimiter=delimiter)
                            goods_list = list(edit)
                        if goods_list[row][0] == k[0]:
                            goods_list[row][1] = str(int(goods_list[row][1]) - 1)
                    row += 1

                f = open(filename, "w")
                f.truncate()
                f.close()
                rows = goods_list

                with open(filename, 'w', newline='') as f:
                    write = csv.writer(f)
                    write.writerows(rows)
    else:
        print('Ошибка, проверьте наличие товаров')
    return noton


def pay():
    while True:
        with open(orders_file, newline='') as ck:
            check = csv.reader(ck, delimiter=delimiter)
            n1 = 0
            for y in check:
                if n1 == 0:
                    pass
                elif n1 != 0:
                    if str(y[0]) == str(log) and str(y[2]) == 'Created':
                        with open(orders_file, newline='') as cvs:
                            py = csv.reader(cvs, delimiter=delimiter)
                            orders1 = list(py)

                        with open(goods_file, newline='') as sklad:
                            goods = csv.reader(sklad, delimiter=delimiter)
                            n2 = 0
                            for i in goods:
                                if n2 == 0:
                                    n2 += 1
                                else:
                                    if i[0] in orders1:
                                        print(i[0])
                                    n2 += 1


                        f = open(orders_file, "w")
                        f.truncate()
                        f.close()

                        orders1[n1][2] = 'Paid'
                        rows = orders1

                        with open(orders_file, 'w', newline='') as f:
                            write = csv.writer(f)
                            write.writerows(rows)

                        n2 += 1

                    elif str(y[0]) != str(log):
                        pass
                    elif str(y[0]) == str(log) and str(y[2]) == 'Paid':
                        pass
                n1 += 1
        print('Заказ оплачивается...')
        time.sleep(1)
        print('Обработка...')
        time.sleep(1)
        print('Заказ оплачен! Вы можете отследить его статус в разделе "Мои заказы".')
        break


def card():
    while True:
        print('В корзине:')
        with open(orders_file, newline='') as card:
            check = csv.reader(card, delimiter=delimiter)
            n1 = 0
            for i in check:
                if n1 == 0:
                    pass
                elif n1 != 0:
                    if str(i[0]) == str(log) and str(i[2]) == 'Created':
                        orders = []
                        orders.append(i)
                        n2 = 4
                        while n2 != len(orders[0]):
                            print(f'{n2-3}){orders[0][n2]}')
                            n2 += 1
                        if n2 == len(orders[0]):
                            print(f'Общая цена корзины - {orders[0][3]} рублей')
                n1 += 1
        print('1)Удалить вещи из корзины')
        print('2)Оплатить заказ')
        print('3)Вернуться в главное меню')
        next_step = int(input())
        if next_step == 3:
            break
        elif next_step == 2:
            a = checkonstorage()
            if a == 0:
                pay()
            break

        elif next_step == 1:
            remove_item(orders)
    mainmenu()


def remove_item(orders):
    while True:
        try:
            what = int(input('Какой товар вы хотите удалить?\n'))
            break
        except ValueError:
            print('Введите число')
    while True:
        try:
            with open(goods_file, newline='') as v:
                forprice = csv.reader(v, delimiter=delimiter)

                for p in forprice:
                    if str(p[0]) == str(orders[0][what + 3]):
                        delprice = int(p[2])

            with open(orders_file, newline='') as ck:
                check = csv.reader(ck, delimiter=delimiter)
                n1 = 0
                n2 = 0
                for y in check:
                    if n1 == 0:
                        pass
                    elif n1 != 0:
                        if str(y[0]) == str(log) and str(y[2]) == 'Created':
                            with open(orders_file, newline='') as cvs:
                                newlist = csv.reader(cvs, delimiter=delimiter)
                                orders1 = list(newlist)

                            f = open(orders_file, "w")
                            f.truncate()
                            f.close()

                            orders1[n1].remove(str(orders[0][what + 3]))
                            orders1[n1][3] = str(int(orders1[n1][3]) - delprice)
                            rows = orders1

                            with open(orders_file, 'w', newline='') as f:
                                write = csv.writer(f)
                                write.writerows(rows)
                            n2 += 1

                        elif str(y[0]) != str(log):
                            pass
                        elif str(y[0]) == str(log) and str(y[2]) == 'Paid':
                            pass
                    n1 += 1
                break
        except LookupError:
            print('Неверный товар')
            remove_item(orders)


def add_to_cart():
    while True:
        try:
            id = int(input('Какой товар?\n'))
            break
        except ValueError:
            print('Введите число')
    with open(filename, newline='') as cvs:
        py = csv.reader(cvs, delimiter=delimiter)
        n = 0
        for i in py:
            if str(i[1]) != str(0):
                if n == id:
                    with open(orders_file, newline='') as ck:
                        check = csv.reader(ck, delimiter=delimiter)
                        n1 = 0
                        n2 = 0
                        for y in check:
                            if n1 == 0:
                                pass
                            elif n1 != 0:
                                if str(y[0]) == str(log) and str(y[2]) == 'Created':
                                    with open(orders_file, newline='') as cvs:
                                        newlist = csv.reader(cvs, delimiter=delimiter)
                                        orders = list(newlist)

                                    f = open(orders_file, "w")
                                    f.truncate()
                                    f.close()
                                    orders[n1][3] = int(orders[n1][3]) + int(i[2])
                                    orders[n1].append(str(i[0]))
                                    rows = orders

                                    with open(orders_file, 'w', newline='') as f:
                                        write = csv.writer(f)
                                        write.writerows(rows)
                                    n2 += 1

                                elif str(y[0]) != str(log):
                                    pass
                                elif str(y[0]) == str(log) and str(y[2]) == 'Paid':
                                    pass
                            n1 += 1
                        if n2 == 0:
                            with open(orders_file, 'a', newline='') as ord:
                                write = csv.writer(ord)
                                write.writerow([log, str(new_id()), 'Created', i[2], i[0]])
                n += 1
    order()


def show_order():
    while True:
        while True:
            try:
                id = int(input('Какой заказ вы хотите посмотреть?\n'))
                break
            except ValueError:
                print('Введите число')
        with open(orders_file, newline='') as cvs:
            orders = csv.reader(cvs, delimiter=delimiter)
            check = 0
            for f in orders:
                if f[0] == log:
                    check += 1
            if 0 < id <= check:
                n = 0
                with open(orders_file, newline='') as cvs:
                    orders = csv.reader(cvs, delimiter=delimiter)
                    for y in orders:
                        if n == 0:
                            n += 1
                        elif n != 0:
                            if y[0] == log:
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

                                    while True:
                                        print('1)Выйти в список заказов')
                                        print('2)Выйти в меню')
                                        next = input()
                                        if next == '1':
                                            show_all_orders()
                                        if next == '2':
                                            mainmenu()
                                        else:
                                            print('Неверная команда')
            else:
                print('Нет такого заказа')


def show_all_orders():
    while True:
        with open(orders_file, newline='') as cvs:
            orders = csv.reader(cvs, delimiter=delimiter)
            n = 0
            n2 = 0
            print('Ваши заказы:')
            for y in orders:
                if n == 0:
                    n += 1
                elif n != 0:
                    if y[0] == log:
                        print(f'{n})Заказ {y[1]} на сумму {y[3]} рублей')
                        n2 += 1
                        n += 1

            if n2 == 0:
                print('Заказы отсутсвуют')

        print()
        print('1)Посмотреть информацию о заказе')
        print('2)Выйти в меню')
        next = input()
        if next == '1':
            show_order()
        elif next == '2':
            mainmenu()
        else:
            print('Неверная команда')


mainmenu()

