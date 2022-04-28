from django.test import TestCase

from django.urls import reverse


class MainViewsTest(TestCase):
    def test_home_page_shows_correct_template(self):
        response = self.client.get(reverse('index'))

        self.assertTemplateUsed(response, 'main/home_page.html')

    def test_community_shows_correct_template(self):
        response = self.client.get(reverse('community view'))

        self.assertTemplateUsed(response, 'main/community_view.html')

