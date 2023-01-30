from django.test import SimpleTestCase
from django.urls import reverse, resolve
from register.views import index_view, login_user, register_view

# python manage.py test register to run the tests
# or python manage.py test register.tests to run the tests
# or python manage.py test register.tests.TestUrls.test_home_url_is_resolved depending if we want to run all tests or
# just one

# QUESTIONS: how to get rid of the ResolverMatch in the terminal when running a test
class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index_view)

    def test_login_url_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_user)

    def test_register_url_resolves(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_view)

        # MISSING TESTING THE OTHER URLS