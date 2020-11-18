import sqlite3
from sqlite3 import Error


class CRUD:

    def __init__(self):
        self.connection = sqlite3.connect('crud.db')
        self.cursor = self.connection.cursor()

    def create(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS records('
            'id Integer PRIMARY KEY AUTOINCREMENT,'
            'name char(30) not null,'
            'self_records text not null default "text")')
        self.connection.commit()

    def insert(self, user_input):
        self.cursor.execute(
            'INSERT INTO records(name, self_records) '
            'VALUES(?, ?)', user_input)
        self.connection.commit()

    def insert_input(self):
        value_1 = input('Ваше имя: ')
        value_2 = input('Ваша запись: ')
        user_input = (value_1, value_2)
        return user_input

    def update_name(self, user_input):
        self.cursor.execute(
            'UPDATE records SET name = ? WHERE id = ?', user_input)
        self.connection.commit()

    def update_input_name(self):
        value_2 = input('Введите ID записи которую нужно изменить: ')
        value_1 = input('Введите новое имя: ')
        user_input = (value_1, int(value_2))
        return user_input

    def update_text(self, user_input):
        self.cursor.execute(
            'UPDATE records SET self_records = ? WHERE id = ?', user_input)
        self.connection.commit()

    def update_input_text(self):
        value_2 = input('Введите ID записи которую нужно изменить: ')
        value_1 = input('Введите новый текст: ')
        user_input = (value_1, int(value_2))
        return user_input

    def select(self):
        self.cursor.execute('select * from records')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def delete(self, user_input):
        try:
            self.cursor.execute(f'DELETE FROM records WHERE id = {user_input}')
        except Error:
            print(Error)
        self.connection.commit()

    def exit(self):
        self.connection.close()
        exit()


class Worker:

    def __init__(self):
        self.work_with_db = CRUD()

    def create(self):
        self.work_with_db.create()
        print('Таблица готова к работе')

    def insert(self):
        while True:
            enter_insert = input('Вставить новые данные в таблицу? Да | Нет: ').lower()
            if enter_insert == 'да':
                try:
                    self.work_with_db.insert(user_input=self.work_with_db.insert_input())
                    break
                except Error:
                    print('Ошибка при вставке данных в таблицу')
                    break
            elif enter_insert == 'нет':
                break
            else:
                continue

    def update_name(self):
        while True:
            enter_update = input('Обновить имя в таблице? Да | Нет: ').lower()
            if enter_update == 'да':
                try:
                    self.work_with_db.update_name(user_input=self.work_with_db.update_input_name())
                    break
                except Error:
                    print('Ошибка при обновление таблицы')
                    break
            elif enter_update == 'нет':
                break
            else:
                continue

    def update_text(self):
        while True:
            enter_update = input('Обновить текст в таблице? Да | Нет: ').lower()
            if enter_update == 'да':
                try:
                    self.work_with_db.update_text(user_input=self.work_with_db.update_input_text())
                    break
                except Error:
                    print('Ошибка при обновление таблицы')
                    break
            elif enter_update == 'нет':
                break
            else:
                continue

    def select(self):
        while True:
            enter_select = input('Вывести все содержимое таблицы? Да | Нет: ').lower()
            if enter_select == 'да':
                try:
                    self.work_with_db.select()
                    break
                except Error:
                    print('Ошибка при выводе содержимого таблицы')
                    break
            elif enter_select == 'нет':
                break
            else:
                continue

    def delete(self):
        while True:
            enter_delete = input('Удалить последнюю запись? Да | Нет: ').lower()
            if enter_delete == 'да':
                value = int(input('Введите номер записи, которую желаете удалить: '))
                try:
                    self.work_with_db.delete(user_input=value)
                    break
                except Error:
                    print('Ошибка при удаление запись')
                    break
            elif enter_delete == 'нет':
                break
            else:
                continue


def main():
    print('Для выхода введите exit\n')
    work_with_db = Worker()
    work_with_db.create()
    while True:
        enter = input('\n'
                      '1 - Вставить данные в таблицу\n'
                      '2 - Обновить данные в таблице\n'
                      '3 - Прочесть таблицу\n'
                      '4 - Удалить запись из таблицы\n'
                      ': ')
        if enter == '1':
            work_with_db.insert()
            continue
        elif enter == '2':
            work_with_db.update_name()
            work_with_db.update_text()
            continue
        elif enter == '3':
            work_with_db.select()
            continue
        elif enter == '4':
            work_with_db.delete()
            continue
        elif enter == 'exit':
            escape = CRUD()
            escape.exit()
        else:
            continue


main()
