from django.test import SimpleTestCase
from django.urls import reverse, resolve
from register.views import index_view, login_user, register_view, dashboard_view, logout_user, base, help, \
    statistics, seats, statistics_text

# python manage.py test register to run the tests
# or python manage.py test register.tests to run the tests
# or python manage.py test register.tests.test_urls.TestUrls.test_home_url_is_resolved depending if we want to run all tests or
# just one

# Can use SimpleTestCase any time we do not have to interact with the database

# QUESTIONS: how to get rid of the ResolverMatch in the terminal when running a test
class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self): # Takes in the self parameter
        url = reverse('home')
        print(resolve(url)) # Use resolve function to parse url and see which view django is going to call
        self.assertEquals(resolve(url).func, index_view) # Making sure that the resolve url is equal to index_view

    def test_login_url_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)

    def test_register_url_resolves(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_view)

    def test_dashboard_url_resolves(self):
        url = reverse('dashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard_view)

    '''def test_logout_user_url_resolves(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_user)'''

    def test_base_url_resolves(self):
        url = reverse('base')
        print(resolve(url))
        self.assertEquals(resolve(url).func, base)
    def test_help_url_resolves(self):
        url = reverse('help')
        print(resolve(url))
        self.assertEquals(resolve(url).func, help)

    def test_statistics_url_resolves(self):
        url = reverse('statistics')
        print(resolve(url))
        self.assertEquals(resolve(url).func, statistics)

    def test_seats_url_resolves(self):
        url = reverse('seats')
        print(resolve(url))
        self.assertEquals(resolve(url).func, seats)

    def test_statistics_text_url_resolves(self):
        url = reverse('statistics_text')
        print(resolve(url))
        self.assertEquals(resolve(url).func, statistics_text)