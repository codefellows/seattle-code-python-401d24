from django.test import TestCase
from django.urls import reverse
class ThingTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse("thing_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_list_page_template(self):
        url = reverse("thing_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "thing_list.html")
        self.assertTemplateUsed(response, "base.html")

    ## tests for Detail Page are stretch
