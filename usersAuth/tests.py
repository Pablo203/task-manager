from django.test import TestCase

# Create your tests here.
class UrlsTests(TestCase):

    def test_login_url(self):
        response = self.client.get("/auth/login_user/")
        self.assertEqual(response.status_code, 200)

    def test_register_url(self):
        response = self.client.get("/auth/register_user/")
        self.assertEqual(response.status_code, 200)