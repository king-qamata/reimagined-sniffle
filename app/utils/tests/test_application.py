import pycodestyle
from django.test import TestCase


class TestApplication(TestCase):

    def test_style(self):
        """
        Test PEP8 conventions
        """

        style = pycodestyle.StyleGuide(ignore=['E501'])
        result = style.check_files(['utils/'])
        self.assertEqual(result.total_errors, 0)
