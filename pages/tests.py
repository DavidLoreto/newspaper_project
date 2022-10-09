from webbrowser import get
from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class HomePageTest(SimpleTestCase):
    def test_home_page_status_code(self):
        request = self.client.get(reverse('home'))

        self.assertEqual(request.status_code, 200)

    def test_home_page_template(self):
        request = self.client.get(reverse('home'))

        self.assertTemplateUsed(request, 'home.html')

class SignUpPageTest(TestCase):
    username = 'test'
    email = 'test@mail.com'

    def test_signup_page_status_code(self):
        request = self.client.get(reverse('signup'))

        self.assertEqual(request.status_code, 200)

    def test_signup_page_template(self):
        request = self.client.get(reverse('signup'))

        self.assertTemplateUsed(request, 'signup.html')

    def test_signup_form(self):
        newuser = get_user_model().objects.create_user(
            self.username, self.email
        )

        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
