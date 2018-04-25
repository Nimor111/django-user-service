from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from faker import Factory

from django.urls import reverse_lazy

from user.models import User
from user.factories import UserFactory

faker = Factory.create()


class UserAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()

    def test_can_get_all_users(self):
        response = self.client.get(reverse_lazy('user:users-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertContains(response, self.user.email)

    def test_can_get_a_single_user(self):
        other_user = UserFactory()

        response = self.client.get(
            reverse_lazy(
                'user:get-user',
                kwargs={'email': self.user.email})
            )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.email)
        self.assertNotContains(response, other_user.email)

    def test_can_create_user(self):
        user_count = User.objects.count()
        data = {
            'first_name': faker.name(),
            'last_name': faker.name(),
            'password': faker.password(),
            'email': faker.email(),
        }

        response = self.client.post(
            reverse_lazy('user:create-user'),
            data=data
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), user_count + 1)

    def test_can_update_user(self):
        new_first_name = faker.name()
        data = {
            'first_name': new_first_name
        }

        response = self.client.patch(
            reverse_lazy(
                'user:update-user',
                kwargs={'email': self.user.email}
            ),
            data=data
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.first().first_name, new_first_name)

    def test_can_delete_user(self):
        user_count = User.objects.count()

        response = self.client.delete(
            reverse_lazy(
                'user:delete-user',
                kwargs={'email': self.user.email}
                )
            )

        self.assertEqual(response.status_code, 204)
        self.assertEqual(User.objects.count(), user_count - 1)
