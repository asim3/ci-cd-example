from django.test import TestCase


class AsimTestCase(TestCase):
    data = "asim"

    def test_my_data(self):
        self.assertEqual(self.data, "asim")
        self.assertIsInstance(self.data, str)
