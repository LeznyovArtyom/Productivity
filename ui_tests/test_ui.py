from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pytest


link = "http://127.0.0.1:8000"


@pytest.mark.registration
class TestRegistration():

    def test_success_registration(self, browser):
        browser.get(link)
        to_registration_button = browser.find_element(By.CSS_SELECTOR, ".buttons :nth-child(2)")
        to_registration_button.click()

        name_input = browser.find_element(By.ID, "name")
        name_input.send_keys("user")
        login_input = browser.find_element(By.ID, "login")
        login_input.send_keys("username")
        password_input = browser.find_element(By.ID, "password")
        password_input.send_keys("123456")
        confirmPassword_input = browser.find_element(By.ID, "confirmPassword")
        confirmPassword_input.send_keys("123456")

        registration_button = browser.find_element(By.ID, "registration_button")
        registration_button.click()

        try:
            browser.find_element(By.CLASS_NAME, "description")
        except:
            assert False, "Элемент описания не присутствует после успешной регистрации"


    def test_delete_account(self, browser):
        browser.get(link)
        to_authorization_button = browser.find_element(By.CSS_SELECTOR, ".buttons :nth-child(1)")
        to_authorization_button.click()

        login_input = browser.find_element(By.ID, "login")
        login_input.send_keys("username")
        password_input = browser.find_element(By.ID, "password")
        password_input.send_keys("123456")

        authorization_button = browser.find_element(By.ID, "authorization_button")
        authorization_button.click()

        link_to_settings = browser.find_element(By.CLASS_NAME, "settings_title")
        link_to_settings.click()

        # Удаляем аккаунт
        delete_account_button = browser.find_element(By.ID, "delete_account_button")
        delete_account_button.click()
        deleteButton = browser.find_element(By.ID, "deleteButton")
        deleteButton.click()
        try:
            browser.find_element(By.CLASS_NAME, "description")
        except:
            assert False, "Элемент описания не присутствует после удаления аккаунта"

        # Проверка на несуществование аккаунта
        to_authorization_button = browser.find_element(By.CSS_SELECTOR, ".buttons :nth-child(1)")
        to_authorization_button.click()

        login_input = browser.find_element(By.ID, "login")
        login_input.send_keys("username")
        password_input = browser.find_element(By.ID, "password")
        password_input.send_keys("123456")

        authorization_button = browser.find_element(By.ID, "authorization_button")
        authorization_button.click()

        try:
            error = browser.find_element(By.CLASS_NAME, "alert-danger")
            assert error.text == "Неправильный логин или пароль"
        except:
            assert False, "Был произведен вход в удаленный аккаунт"


    def test_fail_registration(self, browser):
        browser.get(link)
        to_registration_button = browser.find_element(By.CSS_SELECTOR, ".buttons :nth-child(2)")
        to_registration_button.click()

        # Все поля пустые
        registration_button = browser.find_element(By.ID, "registration_button")
        registration_button.click()
        try:
            browser.find_element(By.ID, "registration_title")
        except:
            assert False, "Регистрация при пустых полях прошла, но не должна"

        browser.refresh()

        # Поле имени пустое
        login_input = browser.find_element(By.ID, "login")
        password_input = browser.find_element(By.ID, "password")
        confirmPassword_input = browser.find_element(By.ID, "confirmPassword")
        registration_button = browser.find_element(By.ID, "registration_button")
        login_input.send_keys("username")
        password_input.send_keys("123456")
        confirmPassword_input.send_keys("123456")
        registration_button.click()
        try:
            browser.find_element(By.ID, "registration_title")
        except:
            assert False, "Регистрация при пустом поле имени прошла, но не должна"

        browser.refresh()
        
        # Поле логина пустое
        name_input = browser.find_element(By.ID, "name")
        password_input = browser.find_element(By.ID, "password")
        confirmPassword_input = browser.find_element(By.ID, "confirmPassword")
        registration_button = browser.find_element(By.ID, "registration_button")
        name_input.send_keys("user")
        password_input.send_keys("123456")
        confirmPassword_input.send_keys("123456")
        registration_button.click()
        try:
            browser.find_element(By.ID, "registration_title")
        except:
            assert False, "Регистрация при пустом поле логина прошла, но не должна"

        browser.refresh()

        # Поле пароля пустое
        name_input = browser.find_element(By.ID, "name")
        login_input = browser.find_element(By.ID, "login")
        confirmPassword_input = browser.find_element(By.ID, "confirmPassword")
        registration_button = browser.find_element(By.ID, "registration_button")
        name_input.send_keys("user")
        login_input.send_keys("username")
        confirmPassword_input.send_keys("123456")
        registration_button.click()
        try:
            browser.find_element(By.ID, "registration_title")
        except:
            assert False, "Регистрация при пустом поле пароля прошла, но не должна"

        browser.refresh()

        # Поле подтверждения пароля пустое
        name_input = browser.find_element(By.ID, "name")
        login_input = browser.find_element(By.ID, "login")
        password_input = browser.find_element(By.ID, "password")
        registration_button = browser.find_element(By.ID, "registration_button")
        name_input.send_keys("user")
        login_input.send_keys("username")
        password_input.send_keys("123456")
        registration_button.click()
        try:
            browser.find_element(By.ID, "registration_title")
        except:
            assert False, "Регистрация при пустом поле подтверждения пароля прошла, но не должна"

        browser.refresh()

        # 2 символа в поле логина
        name_input = browser.find_element(By.ID, "name")
        login_input = browser.find_element(By.ID, "login")
        password_input = browser.find_element(By.ID, "password")
        confirmPassword_input = browser.find_element(By.ID, "confirmPassword")
        registration_button = browser.find_element(By.ID, "registration_button")
        name_input.send_keys("user")
        login_input.send_keys("us")
        password_input.send_keys("123456")
        confirmPassword_input.send_keys("123456")
        registration_button.click()
        try:
            browser.find_element(By.ID, "registration_title")
        except:
            assert False, "Регистрация при 2 символах в поле логина прошла, но не должна"

        browser.refresh()

        # 3 символа и специальный символ в поле логина
        name_input = browser.find_element(By.ID, "name")
        login_input = browser.find_element(By.ID, "login")
        password_input = browser.find_element(By.ID, "password")
        confirmPassword_input = browser.find_element(By.ID, "confirmPassword")
        registration_button = browser.find_element(By.ID, "registration_button")
        name_input.send_keys("user")
        login_input.send_keys("use#")
        password_input.send_keys("123456")
        confirmPassword_input.send_keys("123456")
        registration_button.click()
        try:
            browser.find_element(By.ID, "registration_title")
        except:
            assert False, "Регистрация при 3 символах и специальном символе в поле логина прошла, но не должна"
        
        browser.refresh()

        # 5 символов в поле пароля
        name_input = browser.find_element(By.ID, "name")
        login_input = browser.find_element(By.ID, "login")
        password_input = browser.find_element(By.ID, "password")
        confirmPassword_input = browser.find_element(By.ID, "confirmPassword")
        registration_button = browser.find_element(By.ID, "registration_button")
        name_input.send_keys("user")
        login_input.send_keys("username")
        password_input.send_keys("12345")
        confirmPassword_input.send_keys("12345")
        registration_button.click()
        try:
            browser.find_element(By.ID, "registration_title")
        except:
            assert False, "Регистрация при 5 символах в поле пароля прошла, но не должна"

        browser.refresh()

        # Неодинаковый пароль в подтверждение пароля
        name_input = browser.find_element(By.ID, "name")
        login_input = browser.find_element(By.ID, "login")
        password_input = browser.find_element(By.ID, "password")
        confirmPassword_input = browser.find_element(By.ID, "confirmPassword")
        registration_button = browser.find_element(By.ID, "registration_button")
        name_input.send_keys("user")
        login_input.send_keys("username")
        password_input.send_keys("123456")
        confirmPassword_input.send_keys("12345")
        registration_button.click()
        try:
            browser.find_element(By.ID, "registration_title")
        except:
            assert False, "Регистрация при неодинаковом пароле в подтверждении пароля прошла, но не должна"


@pytest.mark.authorization
class TestAuthorization():

    def test_success_authorization(self, browser):
        browser.get(link)
        to_authorization_button = browser.find_element(By.CSS_SELECTOR, ".buttons :nth-child(1)")
        to_authorization_button.click()

        login_input = browser.find_element(By.ID, "login")
        login_input.send_keys("testuser")
        password_input = browser.find_element(By.ID, "password")
        password_input.send_keys("testpassword")

        authorization_button = browser.find_element(By.ID, "authorization_button")
        authorization_button.click()

        try:
            browser.find_element(By.CLASS_NAME, "filter_text")
        except:
            assert False, "Элемент фильтрации не присутствует после авторизации"


    def test_fail_authorization(self, browser):
        browser.get(link)
        to_authorization_button = browser.find_element(By.CSS_SELECTOR, ".buttons :nth-child(1)")
        to_authorization_button.click()

        # Несуществующий логин и пароль
        login_input = browser.find_element(By.ID, "login")
        password_input = browser.find_element(By.ID, "password")
        authorization_button = browser.find_element(By.ID, "authorization_button")
        login_input.send_keys("abrakadabra")
        password_input.send_keys("domnadereve")
        authorization_button.click()
        try:
            error = browser.find_element(By.CLASS_NAME, "alert-danger")
            assert error.text == "Неправильный логин или пароль"
        except:
            assert False, "Авторизация при несуществующих данных прошла, хотя не должна"

        # Существующий логин и неправильный пароль
        login_input = browser.find_element(By.ID, "login")
        password_input = browser.find_element(By.ID, "password")
        authorization_button = browser.find_element(By.ID, "authorization_button")
        login_input.send_keys("testuser")
        password_input.send_keys("domnadereve")
        authorization_button.click()
        try:
            error = browser.find_element(By.CLASS_NAME, "alert-danger")
            assert error.text == "Неправильный логин или пароль"
        except:
            assert False, "Авторизация при существующем логине и неправильном прошла, хотя не должна"


@pytest.mark.tasks
class TestTasks():

    def test_task_list(self, browser):
        browser.get(link)
        browser = authorization(browser)


        ######## Страница 'Мои задачи' ########

        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        for task in tasks:
            # Проверка на наличие изображения важности задачи
            importance_image = task.find_element(By.CLASS_NAME, "importance")
            assert importance_image.get_attribute("src"), "Изображение важности отсутствует на странице 'Мои задачи'"

            # Проверка на наличие названия задачи
            task_name = task.find_element(By.CLASS_NAME, "task_name")
            assert task_name.text, "Название задачи отсутствует на странице 'Мои задачи'"

            # Проверка на наличие дедлайна задачи
            task_deadline = task.find_element(By.CLASS_NAME, "task_deadline")
            assert task_deadline.text, "Дедлайн задачи отсутствует на странице 'Мои задачи'"

            # Проверка на наличие описания задачи
            task_description = task.find_element(By.CLASS_NAME, "task_description")
            assert task_description.text, "Описание задачи отсутствует на странице 'Мои задачи'"

            # Проверка на наличие и допустимые значения статуса задачи
            task_status = task.find_element(By.CLASS_NAME, "task_status")
            assert task_status.text in ["Открытая", "В процессе"], "Недопустимый статус задачи на странице 'Мои задачи'"

        # Проверка на переход на страницу задачи со страницы 'Мои задачи'
        task_name.click()
        try:
            browser.find_element(By.ID, "deleteTaskButton")
        except:
            assert False, "Переход на страницу задачи со страницы 'Мои задачи' не выполнен"


        ######## Страница 'Завершенные' ########
        link_to_complete_tasks = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(2) .nav-link")
        link_to_complete_tasks.click()

        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        for task in tasks:
            # Проверка на наличие изображения важности задачи
            importance_image = task.find_element(By.CLASS_NAME, "importance")
            assert importance_image.get_attribute("src"), "Изображение важности отсутствует на странице 'Завершенные'"

            # Проверка на наличие названия задачи
            task_name = task.find_element(By.CLASS_NAME, "task_name")
            assert task_name.text, "Название задачи отсутствует на странице 'Завершенные'"

            # Проверка на наличие дедлайна задачи
            task_deadline = task.find_element(By.CLASS_NAME, "task_deadline")
            assert task_deadline.text, "Дедлайн задачи отсутствует на странице 'Завершенные'"

            # Проверка на наличие описания задачи
            task_description = task.find_element(By.CLASS_NAME, "task_description")
            assert task_description.text, "Описание задачи отсутствует на странице 'Завершенные'"

            # Проверка наличия кнопки 'Возобновить'
            resume_button = task.find_element(By.CLASS_NAME, "resume_button")
            assert resume_button.text == "Возобновить", "Кнопка 'Возобновить' отсутствует на странице 'Завершенные'"

            # Проверка наличия кнопки 'В корзину'
            trash_button = task.find_element(By.CLASS_NAME, "trash_button")
            assert trash_button.text == "В корзину", "Кнопка 'В корзину' отсутствует на странице 'Завершенные'"

        # Проверка на переход на страницу задачи со страницы 'Завершенные'
        task_name.click()
        try:
            browser.find_element(By.ID, "deleteTaskButton")
        except:
            assert False, "Переход на страницу задачи со страницы 'Завершенные' не выполнен"


        ######## Страница 'Корзина' ########
        link_to_trash = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(3) .nav-link")
        link_to_trash.click()

        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        for task in tasks:
            # Проверка на наличие изображения важности задачи
            importance_image = task.find_element(By.CLASS_NAME, "importance")
            assert importance_image.get_attribute("src"), "Изображение важности отсутствует на странице 'Корзина'"

            # Проверка на наличие названия задачи
            task_name = task.find_element(By.CLASS_NAME, "task_name")
            assert task_name.text, "Название задачи отсутствует на странице 'Корзина'"

            # Проверка на наличие дедлайна задачи
            task_deadline = task.find_element(By.CLASS_NAME, "task_deadline")
            assert task_deadline.text, "Дедлайн задачи отсутствует на странице 'Корзина'"

            # Проверка на наличие описания задачи
            task_description = task.find_element(By.CLASS_NAME, "task_description")
            assert task_description.text, "Описание задачи отсутствует на странице 'Корзина'"

            # Проверка наличия кнопки 'Возобновить'
            resume_button = task.find_element(By.CLASS_NAME, "resume_button")
            assert resume_button.text == "Возобновить", "Кнопка 'Возобновить' отсутствует на странице 'Корзина'"

            # Проверка наличия кнопки 'В завершенные'
            in_complete_button = task.find_element(By.CLASS_NAME, "in_complete_button")
            assert in_complete_button.text == "В завершенные", "Кнопка 'В завершенные' отсутствует на странице 'Корзина'"

        # Проверка на переход на страницу задачи со страницы 'Завершенные'
        task_name.click()
        try:
            browser.find_element(By.ID, "deleteTaskButton")
        except:
            assert False, "Переход на страницу задачи со страницы 'Завершенные' не выполнен"


    def test_task_info(self, browser):
        browser.get(link)
        browser = authorization(browser)

        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        # Переход на страницу задачи
        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        link_to_task = tasks[0].find_element(By.CLASS_NAME, "task_name")
        link_to_task.click()

        # Проверка присутствия информации о задаче
        task_name = browser.find_element(By.ID, "task_name")
        assert task_name.get_attribute("value"), "Название задачи отсутствует на странице задачи"
        importance_image = browser.find_element(By.ID, "importance_image")
        assert importance_image.get_attribute("src"), "Изображение важности отсутствует на странице задачи"
        importance_select = browser.find_element(By.ID, "importance_value")
        assert importance_select.get_attribute("value"), "Значение важности не выбрано на странице задачи"
        status_image = browser.find_element(By.ID, "status_filling")
        assert status_image.get_attribute("class"), "Цвет статуса отсутствует на странице задачи"
        status_select = browser.find_element(By.ID, "status_value")
        assert status_select.get_attribute("value"), "Значение статуса не выбрано на странице задачи"
        deadline = browser.find_element(By.ID, "deadline_value")
        assert deadline.get_attribute("value"), "Значение дедлайна отсутствует на странице задачи"
        description = browser.find_element(By.ID, "task_description")
        assert description.text, "Описание отсутствует на странице задачи"


    def test_add_task(self, browser):
        browser.get(link)
        browser = authorization(browser)

        add_task_button = browser.find_element(By.CLASS_NAME, "add_task")
        add_task_button.click()

        task_name_input = browser.find_element(By.ID, "task_name")
        task_name_input.send_keys("Протестировать приложение")
        task_description_input = browser.find_element(By.ID, "task_description")
        task_description_input.send_keys("Написать ui тесты для веб-приложения 'Productivity'")
        task_importance_select = Select(browser.find_element(By.ID, "task_importance"))
        task_importance_select.select_by_value("2")
        task_deadline_input = browser.find_element(By.ID, "task_deadline")
        task_deadline_input.send_keys("25.08.2024")

        add_task_button = browser.find_element(By.CLASS_NAME, "add_task")
        add_task_button.click()

        try:
            browser.find_element(By.CLASS_NAME, "filter_text")
        except:
            assert False, "Не произведен переход на страницу 'Мои задачи' после добавления задачи"

        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        # Проверяем, что задача добавилась
        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        name_of_added_task = tasks[-1].find_element(By.CLASS_NAME, "task_name")
        assert name_of_added_task.text == "Протестировать приложение", "Задача не была добавлена"


    def test_delete_task(self, browser):
        browser.get(link)
        browser = authorization(browser)

        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        # Переход на страницу задачи
        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        link_to_last_task = tasks[-1].find_element(By.CLASS_NAME, "task_name")
        link_to_last_task.click()

        deleteTaskButton = browser.find_element(By.ID, "deleteTaskButton")
        deleteTaskButton.click()
        deleteButton = browser.find_element(By.ID, "deleteButton")
        deleteButton.click()

        # Проверяем, что задача появилась в корзине
        link_to_trash = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(3) .nav-link")
        link_to_trash.click()

        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        name_of_delete_task = tasks[-1].find_element(By.CLASS_NAME, "task_name")
        assert name_of_delete_task.text == "Протестировать приложение", "Задача не была удалена"


    def test_change_task(self, browser):
        browser.get(link)
        browser = authorization(browser)

        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        # Переход на страницу задачи
        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        link_to_task = tasks[0].find_element(By.CLASS_NAME, "task_name")
        link_to_task.click()

        task_name_input = browser.find_element(By.ID, "task_name")
        task_name_input.clear()
        task_name_input.send_keys("Новая задача")
        importance_select = Select(browser.find_element(By.ID, "importance_value"))
        importance_select.select_by_value("5")
        status_select = Select(browser.find_element(By.ID, "status_value"))
        status_select.select_by_value("2")
        deadline_input = browser.find_element(By.ID, "deadline_value")
        deadline_input.clear()
        deadline_input.send_keys("15.09.2024")
        task_description_input = browser.find_element(By.ID, "task_description")
        task_description_input.clear()
        task_description_input.send_keys("Новое описание задачи")

        save_button = browser.find_element(By.ID, "saveTaskButton")
        save_button.click()

        # Проверяем, что произведен переход на страницу 'Мои задачи'
        try:
            browser.find_element(By.CLASS_NAME, "filter_text")
        except:
            assert False, "Элемент фильтрации не присутствует после авторизации"

        # Проверяем, что задача изменилась
        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        task = tasks_container.find_elements(By.CLASS_NAME, "task")[0]
        
        try:
            assert task.find_element(By.CLASS_NAME, "task_name").text == "Новая задача"
            assert task.find_element(By.CLASS_NAME, "importance").get_attribute("src") == f"{link}/images/very_low_importance.jpg"
            assert task.find_element(By.CLASS_NAME, "task_deadline").text == "15 September 2024"
            assert task.find_element(By.CLASS_NAME, "task_description").text == "Новое описание задачи"
            assert task.find_element(By.CLASS_NAME, "task_status").text == "В процессе"
        except:
            assert False, "Информация о задаче не изменилась"


        # Возвращаем задачу в исходное состояние
        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        # Переход на страницу задачи
        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        link_to_task = tasks[0].find_element(By.CLASS_NAME, "task_name")
        link_to_task.click()

        task_name_input = browser.find_element(By.ID, "task_name")
        task_name_input.clear()
        task_name_input.send_keys("Сделать проект")
        importance_select = Select(browser.find_element(By.ID, "importance_value"))
        importance_select.select_by_value("1")
        status_select = Select(browser.find_element(By.ID, "status_value"))
        status_select.select_by_value("1")
        deadline_input = browser.find_element(By.ID, "deadline_value")
        deadline_input.clear()
        deadline_input.send_keys("25.08.2024")
        task_description_input = browser.find_element(By.ID, "task_description")
        task_description_input.clear()
        task_description_input.send_keys("Нарисовать дизайн, сверстать на HTML, CSS, JS, серверную часть реализовать на Python + Starlette + Jinja 2 с подходом MVT и базой данных MySQL.")

        save_button = browser.find_element(By.ID, "saveTaskButton")
        save_button.click()


@pytest.mark.user_info
class TestUserInfo():
    
    def test_header(self, browser):
        browser.get(link)
        browser = authorization(browser)

        ######## Страница 'Мои задачи' ########
        user_image = browser.find_element(By.ID, "user_image")
        assert user_image.get_attribute("src"), "Изображение пользователя отсутствует на странице 'Мои задачи'"
        user_name = browser.find_element(By.ID, "user_name")
        assert user_name.text == "user", "Имя пользователя отсутствует на странице 'Мои задачи'"
        user_role = browser.find_element(By.ID, "user_role")
        assert user_role.text == "Пользователь", "Роль пользователя отсутствует на странице 'Мои задачи'"


        ######## Страница 'Завершенные' ########
        link_to_complete_tasks = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(2) .nav-link")
        link_to_complete_tasks.click()

        user_image = browser.find_element(By.ID, "user_image")
        assert user_image.get_attribute("src"), "Изображение пользователя отсутствует на странице 'Завершенные'"
        user_name = browser.find_element(By.ID, "user_name")
        assert user_name.text == "user", "Имя пользователя отсутствует на странице 'Завершенные'"
        user_role = browser.find_element(By.ID, "user_role")
        assert user_role.text == "Пользователь", "Роль пользователя отсутствует на странице 'Завершенные'"


        ######## Страница 'Корзина' ########
        link_to_trash = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(3) .nav-link")
        link_to_trash.click()

        user_image = browser.find_element(By.ID, "user_image")
        assert user_image.get_attribute("src"), "Изображение пользователя отсутствует на странице 'Корзина'"
        user_name = browser.find_element(By.ID, "user_name")
        assert user_name.text == "user", "Имя пользователя отсутствует на странице 'Корзина'"
        user_role = browser.find_element(By.ID, "user_role")
        assert user_role.text == "Пользователь", "Роль пользователя отсутствует на странице 'Корзина'"


        ######## Страница 'Настройки' ########
        link_to_settings = browser.find_element(By.CLASS_NAME, "settings_title")
        link_to_settings.click()

        user_image = browser.find_element(By.ID, "user_image")
        assert user_image.get_attribute("src"), "Изображение пользователя отсутствует на странице 'Настройки'"
        user_name = browser.find_element(By.ID, "user_name")
        assert user_name.text == "user", "Имя пользователя отсутствует на странице 'Настройки'"
        user_role = browser.find_element(By.ID, "user_role")
        assert user_role.text == "Пользователь", "Роль пользователя отсутствует на странице 'Настройки'"


        ######## Страница 'Добавить задачу' ########
        link_to_my_tasks = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(1) .nav-link")
        link_to_my_tasks.click()
        link_to_add_task = browser.find_element(By.CLASS_NAME, "add_task")
        link_to_add_task.click()

        user_image = browser.find_element(By.ID, "user_image")
        assert user_image.get_attribute("src"), "Изображение пользователя отсутствует на странице 'Добавить задачу'"
        user_name = browser.find_element(By.ID, "user_name")
        assert user_name.text == "user", "Имя пользователя отсутствует на странице 'Добавить задачу'"
        user_role = browser.find_element(By.ID, "user_role")
        assert user_role.text == "Пользователь", "Роль пользователя отсутствует на странице 'Добавить задачу'"


        ######## Страница 'Задача' ########
        link_to_my_tasks = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(1) .nav-link")
        link_to_my_tasks.click()

        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        # Переход на страницу задачи
        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        link_to_task = tasks[0].find_element(By.CLASS_NAME, "task_name")
        link_to_task.click()

        user_image = browser.find_element(By.ID, "user_image")
        assert user_image.get_attribute("src"), "Изображение пользователя отсутствует на странице 'Задача'"
        user_name = browser.find_element(By.ID, "user_name")
        assert user_name.text == "user", "Имя пользователя отсутствует на странице 'Задача'"
        user_role = browser.find_element(By.ID, "user_role")
        assert user_role.text == "Пользователь", "Роль пользователя отсутствует на странице 'Задача'"


    def test_settings(self, browser):
        browser.get(link)
        browser = authorization(browser)

        link_to_settings = browser.find_element(By.CLASS_NAME, "settings_title")
        link_to_settings.click()
        
        user_name_input = browser.find_element(By.ID, "text_name")
        assert user_name_input.get_attribute("placeholder") == "user", "Имя пользователя не отображается в настройках"
        user_login_input = browser.find_element(By.ID, "text_login")
        assert user_login_input.get_attribute("placeholder") == "testuser", "Логин пользователя не отображается в настройках"
        user_role_select = browser.find_element(By.ID, "role_select")
        assert user_role_select.get_attribute("value") == "1", "Роль пользователя некорректная в настройках"
        profile_image = browser.find_element(By.ID, "profile_image")
        assert profile_image.get_attribute("src"), "Изображение пользователя не отображается в настройках"


    def test_change_user_info(self, browser):
        browser.get(link)
        browser = authorization(browser)

        link_to_settings = browser.find_element(By.CLASS_NAME, "settings_title")
        link_to_settings.click()

        # Проверка изменения имени пользователя
        user_name_input = browser.find_element(By.ID, "text_name")
        user_name_input.send_keys("Person")
        user_name_change = browser.find_element(By.ID, "changeName")
        user_name_change.click()
        assert browser.find_element(By.ID, "text_name").get_attribute("placeholder") == "Person", "Имя пользователя после изменения некорректное"
        
        # Проверка изменения логина пользователя
        user_login_input = browser.find_element(By.ID, "text_login")
        user_login_input.send_keys("Person")
        user_login_change = browser.find_element(By.ID, "changeLogin")
        user_login_change.click()
        assert browser.find_element(By.ID, "text_login").get_attribute("placeholder") == "Person", "Логин пользователя после изменения некорректный"

        # Отправка пароля на изменение
        user_password_input = browser.find_element(By.ID, "text_password")
        user_password_input.send_keys("testPerson")
        user_password_change = browser.find_element(By.ID, "changePassword")
        user_password_change.click()
        settings_title = browser.find_element(By.CLASS_NAME, "page_title")
        assert settings_title.text == "Настройки", "Произошла ошибка при изменении пароля"

        # Проверка изменения роли пользователя
        user_role_select = Select(browser.find_element(By.ID, "role_select"))
        user_role_select.select_by_value("10")
        user_role_change = browser.find_element(By.ID, "changeRole")
        user_role_change.click()
        assert Select(browser.find_element(By.ID, "role_select")).first_selected_option.text == "Аналитик", "Роль пользователя после изменения некорректная"


        # Возвращаем данные обратно
        user_name_input = browser.find_element(By.ID, "text_name")
        user_name_input.send_keys("user")
        user_name_change = browser.find_element(By.ID, "changeName")
        user_name_change.click()
        user_login_input = browser.find_element(By.ID, "text_login")
        user_login_input.send_keys("testuser")
        user_login_change = browser.find_element(By.ID, "changeLogin")
        user_login_change.click()
        user_password_input = browser.find_element(By.ID, "text_password")
        user_password_input.send_keys("testpassword")
        user_password_change = browser.find_element(By.ID, "changePassword")
        user_password_change.click()
        user_role_select = Select(browser.find_element(By.ID, "role_select"))
        user_role_select.select_by_value("1")
        user_role_change = browser.find_element(By.ID, "changeRole")
        user_role_change.click()


@pytest.mark.features
class TestFeatures():

    def test_current_date(self, browser):
        browser.get(link)
        browser = authorization(browser)

        ######## Страница 'Мои задачи' ########
        current_date = browser.find_element(By.ID, "current_date")
        assert current_date.text, "Текущая дата у страницы 'Мои задачи' в шапке отсутствует"

        ######## Страница 'Завершенные' ########
        link_to_complete_tasks = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(2) .nav-link")
        link_to_complete_tasks.click()
        current_date = browser.find_element(By.ID, "current_date")
        assert current_date.text, "Текущая дата у страницы 'Завершенные' в шапке отсутствует"

        ######## Страница 'Корзина' ########
        link_to_trash = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(3) .nav-link")
        link_to_trash.click()
        current_date = browser.find_element(By.ID, "current_date")
        assert current_date.text, "Текущая дата у страницы 'Корзина' в шапке отсутствует"

        ######## Страница 'Настройки' ########
        link_to_settings = browser.find_element(By.CLASS_NAME, "settings_title")
        link_to_settings.click()
        current_date = browser.find_element(By.ID, "current_date")
        assert current_date.text, "Текущая дата у страницы 'Настройки' в шапке отсутствует"

        ######## Страница 'Добавить задачу' ########
        link_to_my_tasks = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(1) .nav-link")
        link_to_my_tasks.click()
        link_to_add_task = browser.find_element(By.CLASS_NAME, "add_task")
        link_to_add_task.click()
        current_date = browser.find_element(By.ID, "current_date")
        assert current_date.text, "Текущая дата у страницы 'Добавить задачу' в шапке отсутствует"

        ######## Страница 'Задача' ########
        link_to_my_tasks = browser.find_element(By.CSS_SELECTOR, ".nav .nav-item:nth-child(1) .nav-link")
        link_to_my_tasks.click()

        # Ожидаем загрузки списка задач
        tasks_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "tasks_container"))
        )

        # Переход на страницу задачи
        tasks = tasks_container.find_elements(By.CLASS_NAME, "task")
        link_to_task = tasks[0].find_element(By.CLASS_NAME, "task_name")
        link_to_task.click()

        current_date = browser.find_element(By.ID, "current_date")
        assert current_date.text, "Текущая дата у страницы 'Задача' в шапке отсутствует"


def authorization(browser):
    to_authorization_button = browser.find_element(By.CSS_SELECTOR, ".buttons :nth-child(1)")
    to_authorization_button.click()

    login_input = browser.find_element(By.ID, "login")
    login_input.send_keys("testuser")
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("testpassword")

    authorization_button = browser.find_element(By.ID, "authorization_button")
    authorization_button.click()
    return browser