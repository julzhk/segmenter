from django.core.management.base import BaseCommand, CommandError
from editor.models import BalanceSheetItem, Election, Segment


from editor.management.commands.rand_names import names
from random import sample, randint
class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(0,300):
            name = ' '. join( sample(names, randint(1, 4)))
            BalanceSheetItem.objects.create(name=name,)

        self.stdout.write(self.style.SUCCESS('Successfully made bs items '))