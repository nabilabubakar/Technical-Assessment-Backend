from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Item
from .Serializers import ItemSerializer

# Create your tests here.


class ItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Item.objects.create(
            name="Item 1", description="First item description")
        self.item2 = Item.objects.create(
            name="Item 2", description="Second item description")
        self.item3 = Item.objects.create(
            name="Item 3", description="Third item description")
        self.valid_payload = {
            'name': 'New Item',
        }

        # Test List (GET) Operation:
    def test_get_all_items(self):
        response = self.client.get(reverse('list-items'))
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # Test Retrieve (GET) Operation:
    def test_get_valid_single_item(self):
        response = self.client.get(
            reverse('get-item', kwargs={'pk': self.item1.pk}))
        item = Item.objects.get(pk=self.item1.pk)
        serializer = ItemSerializer(item)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_item(self):
        response = self.client.get(reverse('get-item', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test Create (POST) Operation:

    def test_create_valid_item(self):
        response = self.client.post(
            reverse('list-items'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_item(self):
        response = self.client.post(
            reverse('list-items'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test Update (PUT) Operation:

    def test_update_valid_item(self):
        response = self.client.put(reverse('get-item', kwargs={'pk': self.item1.pk}), data={
                                   'name': 'Updated Item', 'description': 'Updated description'})
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_update_invalid_item(self):
        response = self.client.put(reverse('get-item', kwargs={'pk': self.item1.pk}), data={
                                   'name': '', 'description': 'Updated description'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test Delete (DELETE) Operation:
    def test_delete_valid_item(self):
        response = self.client.delete(
            reverse('get-item', kwargs={'pk': self.item1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_item(self):
        response = self.client.delete(reverse('get-item', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test Pagination
    def test_pagination_is_working(self):
        response = self.client.get(reverse('list-items'), {'page': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)


# Test Filtering


    def test_filter_items_by_name(self):
        response = self.client.get(reverse('list-items'), {'name': 'Item 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Item 1')

# Test Searching:

    def test_search_items_by_description(self):
        response = self.client.get(
            reverse('list-items'), {'search': 'First item description'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]
                         ['description'], 'First item description')
