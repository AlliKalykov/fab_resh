from rest_framework import status
from rest_framework.reverse import reverse

from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    profile_list_url = reverse('all-profiles')

    def setUp(self):
        # создание нового пользователя, запросом к конечной точке djoser
        self.user = self.client.post('/auth/users/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        # получить веб-токен JSON для вновь созданного пользователя
        response = self.client.post('/auth/jwt/create/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    # получить список всех профилей пользователей во время аутентификации пользователя запроса
    def test_userprofile_list_authenticated(self):
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # получить список всех профилей пользователей, пока запрос пользователя не прошел проверку подлинности
    def test_userprofile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # TODO
