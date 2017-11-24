from django.test import TestCase
from editor.models import BalanceSheetItem

class BalanceSheetItemTestCase(TestCase):

    def test_first(self):
        bs1 = BalanceSheetItem.objects.create(name="lion")
