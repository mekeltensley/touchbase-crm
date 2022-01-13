from django.test import TestCase
from django.shortcuts import reverse

# File used for testing views 

class LandingPageTest(TestCase):
    
    def test_status_code(self):
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")
