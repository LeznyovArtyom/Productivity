# import pytest
# import pytest_asyncio
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker
# from models import Base, Task
# from fill_db import populate_initial_data
# from httpx import AsyncClient, ASGITransport
# from main import app, SessionLocal
# from sqlalchemy.future import select
# import main

# TestSessionLocal = None

# @pytest.fixture(scope="module", autouse=True)
# def setup_test_database():
#     global TestSessionLocal
#     # Используем тестовую базу данных
#     TEST_DATABASE_URL = "mysql+pymysql://root:TikTakfoke86!@localhost:3306/test_db"

#     # Создаем новый engine для тестовой базы данных
#     test_engine = create_engine(TEST_DATABASE_URL)

#     # Создаем сессию для тестовой базы данных
#     TestSessionLocal = sessionmaker(bind=test_engine)

#     # Создаем тестовую базу данных перед выполнением тестов
#     Base.metadata.create_all(bind=test_engine)
    
#     # Выполняем команду ALTER TABLE для поля image
#     with test_engine.connect() as connection:
#         connection.execute(text("ALTER TABLE user MODIFY COLUMN image LONGBLOB;"))

#     # Заполняем базу начальными данными
#     session = TestSessionLocal()
#     populate_initial_data(session)
#     session.commit()
    
#     yield
    
#     # Удаляем все таблицы после завершения тестов
#     # Base.metadata.drop_all(bind=test_engine)


# @pytest.fixture(scope="module", autouse=True)
# def override_session_local():
#     original_session_local = main.SessionLocal
#     main.SessionLocal = TestSessionLocal
#     yield
#     main.SessionLocal = original_session_local


# # Фикстура для сессии базы данных
# @pytest.fixture(scope="function")
# async def db_session(setup_test_database):
#     global TestSessionLocal
#     async with TestSessionLocal() as session:
#         yield session


# @pytest.mark.asyncio
# async def test_tests():
#     async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
#         # 0. Регистрация пользователя
#         response = await client.post("/users/register", json={
#             "name": "TestUser",
#             "login": "testuser",
#             "password": "password123",
#         })

#         assert response.status_code == 200

#         # 1. Авторизация
#         response = await client.post("/users/login", json={
#             "login": "testuser",
#             "password": "password123"
#         })
#         assert response.status_code == 200
#         assert "access_token" in response.json()

#         auth_token = response.json()["access_token"]

#         # 2. Получение информации о пользователе
#         await client.get("/users/me", headers={
#             'Content-Type': 'application/json',
#             "Authorization": f"Bearer {auth_token}"
#         })
#         assert response.status_code == 200
#         print(response.json())
#         assert response.json().get("User").get("login") == "testuser"







# # Тест на авторизацию пользователя и получение токена
# @pytest.mark.asyncio
# async def test_user_and_tasks():
#     async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
#         response = await client.post("/users/login", json={
#             "login": "testuser",
#             "password": "password123"
#         })
#         assert response.status_code == 200
#         assert "access_token" in response.json()


# # Тест на получение информации о пользователе с использованием токена
# @pytest.mark.asyncio
# async def test_get_user_info():
#     async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
#         response = await client.post("/users/login", json={
#             "login": "testuser",
#             "password": "password123"
#         })
#         assert response.status_code == 200
#         print(response.json())
#         assert "access_token" in response.json()
#         # auth_token = response.json()["access_token"]

#         # await client.get("/users/me", headers={
#         #     'Content-Type': 'application/json',
#         #     "Authorization": f"Bearer {auth_token}"
#         # })

#         # assert response.status_code == 200
#         # assert response.json()["User"]["login"] == "testuser"


# # # Тест на добавление задачи пользователем
# # @pytest.mark.asyncio
# # async def test_add_task(client, auth_token):
# #     response = await client.post("/users/me/tasks/add", json={
# #         "name": "Test Task",
# #         "description": "Task Description",
# #         "importance_id": 1,
# #         "deadline": "2023-12-31T23:59:59"
# #     }, headers={
# #         "Authorization": f"Bearer {auth_token}"
# #     })
# #     assert response.status_code == 200
# #     assert response.json()["message"] == "Задача успешно добавлена"


# # # Тест на обновление задачи
# # @pytest.mark.asyncio
# # async def test_update_task(client, auth_token, db_session):
# #     # Добавляем задачу перед её обновлением
# #     response = await client.post("/users/me/tasks/add", json={
# #         "name": "Test Task for Update",
# #         "description": "Task Description",
# #         "importance_id": 1,
# #         "deadline": "2023-12-31T23:59:59"
# #     }, headers={
# #         "Authorization": f"Bearer {auth_token}"
# #     })
# #     assert response.status_code == 200

# #     # Получаем ID созданной задачи
# #     async with db_session as session:
# #         result = await session.execute(select(Task).filter(Task.name == "Test Task for Update"))
# #         task = result.scalar_one_or_none()

# #     # Обновляем задачу
# #     response = await client.put(f"/tasks/{task.id}/update", json={
# #         "name": "Updated Task Name",
# #         "description": "Updated Task Description"
# #     }, headers={
# #         "Authorization": f"Bearer {auth_token}"
# #     })
# #     assert response.status_code == 200
# #     assert response.json()["message"] == "Задача успешно обновлена"


# # # Тест на удаление задачи
# # @pytest.mark.asyncio
# # async def test_delete_task(client, auth_token, db_session):
# #     # Добавляем задачу перед её удалением
# #     response = await client.post("/users/me/tasks/add", json={
# #         "name": "Test Task for Deletion",
# #         "description": "Task Description",
# #         "importance_id": 1,
# #         "deadline": "2023-12-31T23:59:59"
# #     }, headers={
# #         "Authorization": f"Bearer {auth_token}"
# #     })
# #     assert response.status_code == 200

# #     # Получаем ID созданной задачи
# #     async with db_session as session:
# #         result = await session.execute(select(Task).filter(Task.name == "Test Task for Deletion"))
# #         task = result.scalar_one_or_none()

# #     # Удаляем задачу
# #     response = await client.delete("/tasks/{task.id}/delete", headers={
# #         "Authorization": f"Bearer {auth_token}"
# #     })
# #     assert response.status_code == 200
# #     assert response.json()["messege"] == "Задача удалена"

# #     # Проверяем, что задача удалена из базы данных
# #     async with db_session as session:
# #         result = await session.execute(select(Task).filter(Task.id == task.id))
# #         task = result.scalar_one_or_none()
# #         assert task is None


import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
import main
from sqlalchemy.future import select
from models import Task


# Создание клиента один раз для всех тестов
@pytest_asyncio.fixture(scope="function")
async def client():
    async with AsyncClient(transport=ASGITransport(app=main.app), base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_tests(client):
    # 1. Регистрация пользователя
    response = await client.post("/users/register", json={
        "name": "TestUser",
        "login": "testuser",
        "password": "password123",
    })
    assert response.status_code == 200


    # 2. Авторизация пользователя
    response = await client.post("/users/login", json={
        "login": "testuser",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    auth_token = response.json()["access_token"]


    # 3. Получение информации о пользователе
    response = await client.get("/users/me", headers={
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {auth_token}"
    })
    assert response.status_code == 200
    assert response.json()["User"]["login"] == "testuser"


    # 4. Добавление задачи пользователем
    response = await client.post("/users/me/tasks/add", json={
        "name": "Test Task",
        "description": "Task Description",
        "importance_id": 1,
        "deadline": "2023-12-31T23:59:59"
    }, headers={
        "Authorization": f"Bearer {auth_token}"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Задача успешно добавлена"


    # 5. Обновление задачи 
    # Добавляем задачу перед её обновлением
    response = await client.post("/users/me/tasks/add", json={
        "name": "Test Task for Update",
        "description": "Task Description",
        "importance_id": 1,
        "deadline": "2023-12-31T23:59:59"
    }, headers={
        "Authorization": f"Bearer {auth_token}"
    })
    assert response.status_code == 200

    # Получаем ID созданной задачи
    async with main.SessionLocal() as session:
        async with session.begin():
            result = await session.execute(select(Task).filter(Task.name == "Test Task for Update"))
            task = result.scalar_one_or_none()

    # Обновляем задачу
    response = await client.put(f"/tasks/{task.id}/update", json={
        "name": "Updated Task Name",
        "description": "Updated Task Description"
    }, headers={
        "Authorization": f"Bearer {auth_token}"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Задача успешно обновлена"


    # 6. Удаление задачи
    # Добавляем задачу перед её удалением
    response = await client.post("/users/me/tasks/add", json={
        "name": "Test Task for Deletion",
        "description": "Task Description",
        "importance_id": 1,
        "deadline": "2023-12-31T23:59:59"
    }, headers={
        "Authorization": f"Bearer {auth_token}"
    })
    assert response.status_code == 200

    # Получаем ID созданной задачи
    async with main.SessionLocal() as session:
        async with session.begin():
            result = await session.execute(select(Task).filter(Task.name == "Test Task for Deletion"))
            task = result.scalar_one_or_none()

    # Удаляем задачу
    response = await client.delete(f"/tasks/{task.id}/delete", headers={
        "Authorization": f"Bearer {auth_token}"
    })
    assert response.status_code == 200
    assert response.json()["messege"] == "Задача удалена"

    # Проверяем, что задача удалена из базы данных
    async with main.SessionLocal() as session:
        async with session.begin():
            result = await session.execute(select(Task).filter(Task.id == task.id))
            task = result.scalar_one_or_none()
            assert task is None


    # 7. Удаляем пользователя
    response = await client.post("/users/me/delete", headers={
        "Authorization": f"Bearer {auth_token}"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Пользователь удален"

# # Регистрация пользователя
# @pytest.mark.asyncio
# async def test_registration(client):
#     response = await client.post("/users/register", json={
#         "name": "TestUser",
#         "login": "testuser",
#         "password": "password123",
#     })
#     assert response.status_code == 200


# # Авторизация пользователя
# @pytest.mark.asyncio
# async def test_authorization(client):
#     response = await client.post("/users/login", json={
#         "login": "testuser",
#         "password": "password123"
#     })
#     assert response.status_code == 200
#     assert "access_token" in response.json()


# # Получение информации о пользователе
# @pytest.mark.asyncio
# async def test_get_user_info(client):
#     # Авторизация
#     response = await client.post("/users/login", json={
#         "login": "testuser",
#         "password": "password123"
#     })
#     auth_token = response.json()["access_token"]


#     response = await client.get("/users/me", headers={
#         'Content-Type': 'application/json',
#         "Authorization": f"Bearer {auth_token}"
#     })
#     assert response.status_code == 200
#     assert response.json()["User"]["login"] == "testuser"


# # Тест на добавление задачи пользователем
# @pytest.mark.asyncio
# async def test_add_task(client):
#     # Авторизация
#     response = await client.post("/users/login", json={
#         "login": "testuser",
#         "password": "password123"
#     })
#     auth_token = response.json()["access_token"]

#     response = await client.post("/users/me/tasks/add", json={
#         "name": "Test Task",
#         "description": "Task Description",
#         "importance_id": 1,
#         "deadline": "2023-12-31T23:59:59"
#     }, headers={
#         "Authorization": f"Bearer {auth_token}"
#     })
#     assert response.status_code == 200
#     assert response.json()["message"] == "Задача успешно добавлена"


# # Тест на обновление задачи
# @pytest.mark.asyncio
# async def test_update_task(client):
#     # Авторизация
#     response = await client.post("/users/login", json={
#         "login": "testuser",
#         "password": "password123"
#     })
#     auth_token = response.json()["access_token"]


#     # Добавляем задачу перед её обновлением
#     response = await client.post("/users/me/tasks/add", json={
#         "name": "Test Task for Update",
#         "description": "Task Description",
#         "importance_id": 1,
#         "deadline": "2023-12-31T23:59:59"
#     }, headers={
#         "Authorization": f"Bearer {auth_token}"
#     })
#     assert response.status_code == 200

#     # Получаем ID созданной задачи
#     async with main.SessionLocal() as session:
#         async with session.begin():
#             result = await session.execute(select(Task).filter(Task.name == "Test Task for Update"))
#             task = result.scalar_one_or_none()

#     # Обновляем задачу
#     response = await client.put(f"/tasks/{task.id}/update", json={
#         "name": "Updated Task Name",
#         "description": "Updated Task Description"
#     }, headers={
#         "Authorization": f"Bearer {auth_token}"
#     })
#     assert response.status_code == 200
#     assert response.json()["message"] == "Задача успешно обновлена"


# # Тест на удаление задачи
# @pytest.mark.asyncio
# async def test_delete_task(client):
#     # Авторизация
#     response = await client.post("/users/login", json={
#         "login": "testuser",
#         "password": "password123"
#     })
#     auth_token = response.json()["access_token"]


#     # Добавляем задачу перед её удалением
#     response = await client.post("/users/me/tasks/add", json={
#         "name": "Test Task for Deletion",
#         "description": "Task Description",
#         "importance_id": 1,
#         "deadline": "2023-12-31T23:59:59"
#     }, headers={
#         "Authorization": f"Bearer {auth_token}"
#     })
#     assert response.status_code == 200

#     # Получаем ID созданной задачи
#     async with main.SessionLocal() as session:
#         async with session.begin():
#             result = await session.execute(select(Task).filter(Task.name == "Test Task for Deletion"))
#             task = result.scalar_one_or_none()

#     # Удаляем задачу
#     response = await client.delete("/tasks/{task.id}/delete", headers={
#         "Authorization": f"Bearer {auth_token}"
#     })
#     assert response.status_code == 200
#     assert response.json()["messege"] == "Задача удалена"

#     # Проверяем, что задача удалена из базы данных
#     async with main.SessionLocal() as session:
#         async with session.begin():
#             result = await session.execute(select(Task).filter(Task.id == task.id))
#             task = result.scalar_one_or_none()
#             assert task is None