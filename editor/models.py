from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey


class BalanceSheetItem(models.Model):
    name = models.CharField(max_length=20)
    parent_segment = models.ForeignKey('Segment', blank=True, null=True)

    def __str__(self):
        return self.name or '-'

    def get_election(self):
        try:
            return self.parent_segment.get_election()
        except AttributeError:
            pass
        for logical_segment in Segment.objects.exclude(logic_segment=''):
            if self in logical_segment.computed_balance_sheet_items():
                return logical_segment.get_election()
        return '-'

class Election(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name or '-'


class Segment(models.Model):
    name = models.CharField(max_length=20)
    parent_segment = models.ForeignKey('self',
                                 verbose_name='parent segment',
                                 on_delete=models.CASCADE,blank=True, null=True)
    logic_segment = models.TextField(blank=True)
    election = models.ForeignKey('Election',
                                 on_delete=models.CASCADE,
                                  blank=True,
                                  null=True)


    def computed_balance_sheet_items(self):
        return eval(self.logic_segment)

    def get_election(self):
        if self.election:
            return self.election
        if self.parent_segment:
            return self.parent_segment.get_election()


    def __str__(self):
        return self.name or '-'
