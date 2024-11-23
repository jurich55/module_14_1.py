import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER)
''')
# Создание индекса по email
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

    # Создание  таблицы БД  в цикле с началом счета от 1 и с шагом 10 для возраста
for i in range(1, 11):
     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                    (f"user{i}", f"example{i}@gmail.com",  10 * i, 1000))
                 # Обновление balance у каждой второй записи, начиная с первой
cursor.execute('''
    UPDATE Users    SET balance = 500    WHERE (id % 2) = 1
''')
                # Удаление каждой третьей записи, начиная с первой
for id in range(1, 11, 3):
    cursor.execute('''DELETE FROM Users WHERE id = ?''', (id,))

# Выполнение запроса для выборки всех записей, где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
t_ext = cursor.fetchall()        # применение  fetchall()

# Вывод результатов в консоль в формате:
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
for t_ext in t_ext:
    username, email, age, balance = t_ext
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()