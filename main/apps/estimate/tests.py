from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from main.apps.estimate.views import EstimateCreateView
from main.apps.management.models import Equipment
from main.apps.user.models import User


class EstimateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.create_view = EstimateCreateView.as_view()
        cls.superuser = User.objects.create_superuser(
            email='user@example.com',
            password='1234'
        )
        cls.equipment = equipment = Equipment.objects.create(
            name='Cooling Coil',
            price="100.00",
            flag=True,
        )
        cls.equipments = equipments = [
            {
                'equipment': equipment.id,
                'quantity': 5,
                'price_override': "200.00"
            }
        ]
        cls.estimate_data = {
            'note': 'This is a test note for estimate test',
            'archive': True,
            'equipments': equipments
        }
        cls.update_estimate_data = {
            'note': 'This is update note',
            'archive': False,
            'equipments': [{
                'equipment': equipment.id,
                'quantity': 10,
                'price_override': "400.00"
            }]
        }

    def login_superuser(self):
        response = self.client.post(
            '/auth/login/',
            data={
                'email': self.superuser.email,
                'password': '1234'
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def mock_estimate(self):
        self.login_superuser()
        response = self.client.post(
            '/estimate/create/',
            self.estimate_data,
            content_type="application/json"
        )
        self.mock_estimate_data = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_create_estimate(self):
        """ test anonymous user access denied """
        response = self.client.post(
            '/estimate/create/',
            self.estimate_data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.post(
            '/estimate/detail/1/',
            self.estimate_data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_estimate(self):
        """ test superuser can create an estimate """
        self.login_superuser()
        response = self.client.post(
            '/estimate/create/',
            self.estimate_data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_estimate = self.client.get(
            f'/estimate/detail/{response.data["id"]}/',
            content_type="application/json",
        )
        self.assertEqual(created_estimate.status_code, status.HTTP_200_OK)
        self.assertEqual(created_estimate.data['note'], self.estimate_data['note'])
        self.assertEqual(created_estimate.data['archive'], self.estimate_data['archive'])
        for equipment in created_estimate.data['equipments_list']:
            self.assertIn(
                {
                    'equipment': equipment['equipment'],
                    'quantity': equipment['quantity'],
                    'price_override': equipment['price_override'],
                }, self.estimate_data['equipments'])

    def test_update_estimate(self):
        """ test superuser can update an existing estimate """
        self.mock_estimate()
        response = self.client.put(
            f'/estimate/detail/{self.mock_estimate_data.get("id")}/',
            self.update_estimate_data,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_estimate = self.client.get(
            f'/estimate/detail/{self.mock_estimate_data.get("id")}/',
            content_type="application/json",
        )
        self.assertEqual(updated_estimate.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_estimate.data['note'], self.update_estimate_data['note'])
        self.assertEqual(updated_estimate.data['archive'], self.update_estimate_data['archive'])
        for equipment in updated_estimate.data['equipments_list']:
            self.assertIn(
                {
                    'equipment': equipment['equipment'],
                    'quantity': equipment['quantity'],
                    'price_override': equipment['price_override'],
                }, self.update_estimate_data['equipments'])

    def test_delete_estimate(self):
        self.mock_estimate()
        response = self.client.delete(
            f'/estimate/detail/{self.mock_estimate_data["id"]}/',
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
