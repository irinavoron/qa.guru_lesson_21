import allure


@allure.id("31888")
@allure.title("Auth via Google(clone)")
@allure.tag("web", "smoke")
@allure.story("External Auth")
@allure.feature("Auth")
@allure.label("msrv", "Auth")
@allure.label("owner", "allure8")
def test_auth_google():
    with allure.step("Открываем главную страницу"):
        pass
    with allure.step("Выбираем способ авторизации через Google"):
        pass
    with allure.step("Авторизуемся как пользователь mr. Random"):
        with allure.step("Вводим логин Eroshenkoam@gmail.com"):
            pass
    with allure.step("Ввводим пароль 12391283213123"):
        pass
    with allure.step("Нажимаем кнопку Войти"):
        pass
    with allure.step("Проверяем, что авторизовались успешно"):
        pass
    with allure.step("Проверяем, что данные профиля обновились из Google"):
        with allure.step("Имя Mr. Random"):
            pass
    with allure.step("Email Eroshenkoam@gmail.com"):
        pass