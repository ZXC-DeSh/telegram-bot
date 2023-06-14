import sqlite3

# with sqlite3.connect('data.db') as cursor: 
#     command = '''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         surname TEXT,
#         gender TEXT);
#     '''
#     cursor.execute(command)

# try:
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
# except sqlite3.DatabaseError:
#     print('Неудалось подключиться к базе данных')
# finally:
#     connection.close()

class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


def create_table_user(cursor):
    command = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            gender TEXT);
        """
    cursor.execute(command)


def add_user(cursor, user):
    command = """
    INSERT INTO users (name, surname, gender) VALUES (?, ?, ?);
    """
    cursor.execute(command, (user.name, user.surname, user.gender))


def get_users_list(cursor):
    command = """
    SELECT * FROM users;
    """
    users = cursor.execute(command).fetchall()
    print(users)

def get_users_list_for_gender(cursor,gender_id):
    command = """
    SELECT * FROM users WHERE gender = ?;
    """
    users = cursor.execute(command, (gender_id,)).fetchall()
    print(users)


def get_user(cursor, user_id):
    command = """
    SELECT * FROM users WHERE id = ?;
    """
    user = cursor.execute(command, (user_id,)).fetchall()
    print(user)


def update_user_name(cursor, user_id, new_name):
    command = """
    UPDATE users SET name = ? WHERE id = ?;
    """
    cursor.execute(command, (new_name, user_id))

def delete_users(cursor):
    command = """
    DELETE FROM users;
    """
    cursor.execute(command)

def delete_user(cursor,user_id):
    command = """
    DELETE FROM users WHERE id = ?;
    """
    cursor.execute(command,(user_id,)).fetchall()

if __name__ == '__main__':
    with sqlite3.connect('data.db') as cursor:
        create_table_user(cursor)
        delete_users(cursor)
        add_user(cursor, User('Максим', 'Иванов', 'male'))
        add_user(cursor, User('Владимир', 'Петров', 'male'))
        add_user(cursor, User('Екатерина', 'Кузнецова', 'female'))
        get_users_list(cursor)
        get_users_list_for_gender(cursor, 'male')
        delete_user(cursor,3)
        get_user(cursor, 2)
        update_user_name(cursor, 2, 'Павел')
        get_user(cursor, 2)
        get_users_list(cursor)
