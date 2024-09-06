from sqlalchemy import create_engine, text, Column , Integer, String, ForeignKey, DateTime, Text, LargeBinary
from sqlalchemy.orm import relationship, sessionmaker, declarative_base


# Строка подключения к серверу MySQL (без указания базы данных)
DATABASE_SERVER_URL = "mysql+pymysql://root:TikTakfoke86!@localhost:3306/"


# Имя базы данных
DATABASE_NAME = "Productivity"

# Создание соединения с сервером MySQL
engine = create_engine(DATABASE_SERVER_URL)

# Создание базы данных, если она не существует
def create_database(engine, database_name):
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))
        connection.execute(text(f"USE {database_name}"))

create_database(engine, DATABASE_NAME)


# Строка подключения к вновь созданной базе данных
DATABASE_URL = f"{DATABASE_SERVER_URL}{DATABASE_NAME}"


# Создание нового engine для подключения к созданной базе данных
engine = create_engine(DATABASE_URL)

# Создание базового класса для всез моделей
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    login = Column(String(30))
    password = Column(String(100))
    image = Column(LargeBinary)
    # ALTER TABLE user MODIFY COLUMN image LONGBLOB;
    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship("Role")
    tasks = relationship("Task", cascade="all, delete-orphan", back_populates="user")  # Добавлено каскадное удаление задач

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text)
    importance_id = Column(Integer, ForeignKey('importance.id'))
    status_id = Column(Integer, ForeignKey('status.id'))
    deadline = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="tasks")
    importance = relationship("Importance")
    status = relationship("Status")

class Importance(Base):
    __tablename__ = 'importance'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))


# Создание всех таблиц в базе данных, определенных моделями
Base.metadata.create_all(engine)