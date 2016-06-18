from .templatetags.total_extras import format_nis
from django.test import TestCase

class ViewTestCase(TestCase):
    def test_format_nis(self):
        """
        Test for the NIS format function.
        """
        sum = 10000
        result = format_nis(sum)
        self.assertEqual(result, "100.00 " + chr(8362))
