from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Car
# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        car = Car.objects.create(
            author = test_user,
            title = 'ferrari enzo',
            body = 'amazing car through the years'
        )
        car.save() # Save the object to mock Database

    def test_blog_content(self):
        car = Car.objects.get(id=1)
        actual_author = str(car.author)
        actual_title = str(car.title)
        actual_body = str(car.body)
        self.assertEqual(actual_author, 'testuser')
        self.assertEqual(actual_title, 'ferrari enzo')
        self.assertEqual(actual_body, 'amazing car through the years')
