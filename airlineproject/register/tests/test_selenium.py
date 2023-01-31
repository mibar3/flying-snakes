from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from register.views import index_view, login, dashboard_view, base, help, statistics, seats, statistics_text


# using Chrome Version 109.0.5414.120
# These tests will only run correctly if the webdriver downloaded matches your current Chrome version
# to run tests in this file: python manage.py test register.tests.test_selenium
class Test_page(StaticLiveServerTestCase):
        def setUp(self):
            self.browser = webdriver.Chrome('test_selenium/chromedriver.exe')

        def tearDown(self):
            self.browser.close()

        '''def test_is_displayed(self):
            self.browser.get(self.live_server_url)
            # time.sleep(60)

            # The user requests the page for the first time
            # works to check of an existing class within the code, better for checking text
            alert = self.browser.find_element_by_class_name('navbar navbar-expand-lg bg-body-tertiary bg-dark navbar-dark')
            self.assertEquals(
                alert.find_element_by_tag_name('nav').text,

            ) '''

        '''def test_alert_button_redirects_to_home(self):
            self.browser.get(self.live_server_url)
            # time.sleep(60)

            # The user requests the page for the first time
            add_url = self.live_server_url + reverse('home')
            self.browser.find_element_by_tag_name('a').click()
            self.assertEquals(
                self.browser.current_url,
                add_url
            ) '''
        def test_user_inputs_seat(self):
            self.browser.get(self.live_server_url)

            # The user sees the homepage
            self.assertEquals(
                self.browser.find_element_by_class_name('text-center text-success')
            self.assertEquals(alert.find_element_by_tag_name('div').text, 'Welcome to the Flying Snakes Seat Reservation System!')




