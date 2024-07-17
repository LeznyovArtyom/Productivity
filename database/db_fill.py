import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="TikTakfoke86!",
    database="Productivity"
)

cursor = connection.cursor()

importances = [("Критическая",), ("Высокая",), ("Средняя",), ("Низкая",), ("Очень низкая",)]
cursor.executemany("INSERT INTO importance (name) VALUES (%s)", importances)

statuses = [("Открытая",), ("В процессе",), ("Выполнено",), ("Удалено",)]
cursor.executemany("INSERT INTO status (name) VALUES (%s)", statuses)

roles = [("Пользователь",), ("Веб-разработчик",), ("Дизайнер",), ("Архитектор",), ("Фотограф",), ("Администратор",), ("Проектный менеджер",), ("Контент-менеджер",), ("Тестировщик",), 
         ("Аналитик",), ("SEO-специалист",), ("Маркетолог",), ("Системный администратор",), ("Редактор",), ("Копирайтер",)]

connection.commit()
cursor.close()
connection.close()