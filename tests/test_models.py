from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(
            name='bevarage and food', slug='bevarage and food')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model defaulty name
        """
        data = self.data1
        self.assertEqual(str(data), 'bevarage and food')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='beverage and food',
                                slug='beverage and food')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create
                                            (category_id=1, 
                                            title='beverage and food water',
                                            created_by_id=1, 
                                            slug='beverage and food-water',
                                            price='10.00', image='water1')

    def test_products_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'beverage and food water')
