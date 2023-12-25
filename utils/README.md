### Структура тестов API
https://habr.com/ru/amp/publications/669880/

------

### Посоветовал Саша, как сделать авторизацию
@pytest.fixture
def authenticated_client():
    # Создаем пользователя и авторизуем его
    user = User.objects.create_user(
        email='TestUser11@mail.ru',
        password='testpassword',
        username='TestUser'
    )
    client = APIClient()
    client.force_authenticate(user=user)
    return client