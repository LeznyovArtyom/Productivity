from models import engine, Importance, Status, Role
from sqlalchemy.orm import sessionmaker

# Создание сессии для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Заполнение базы данных начальными данными
def populate_initial_data(session):
    importances = [("Критическая",), ("Высокая",), ("Средняя",), ("Низкая",), ("Очень низкая",)]
    for name in importances:
        session.add(Importance(name=name[0]))

    statuses = [("Открытая",), ("В процессе",), ("Выполнено",), ("Удалено",)]
    for name in statuses:
        session.add(Status(name=name[0]))

    roles = [("Пользователь",), ("Веб-разработчик",), ("Дизайнер",), ("Архитектор",), ("Фотограф",), ("Администратор",), 
             ("Проектный менеджер",), ("Контент-менеджер",), ("Тестировщик",), ("Аналитик",), ("SEO-специалист",), 
             ("Маркетолог",), ("Системный администратор",), ("Редактор",), ("Копирайтер",)]
    for name in roles:
        session.add(Role(name=name[0]))

    # Применение изменений
    session.commit()

populate_initial_data(session)