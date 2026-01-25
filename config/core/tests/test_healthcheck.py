from django.test import TestCase
from django.urls import reverse


class HealthcheckTests(TestCase):
    def test_healthcheck(self):
        response = self.client.get(reverse("core:health"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
