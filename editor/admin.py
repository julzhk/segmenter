from django.contrib import admin
from django import forms
from editor.models import Segment, BalanceSheetItem, Election
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

class SegmentForm(forms.ModelForm):

    class Meta:
        model = Segment
        exclude = ['id',]

    def __init__(self, *args, **kwargs):
        super(SegmentForm, self).__init__(*args, **kwargs)
        self.fields['parent_segment'].queryset = Segment.is_published.exclude(
            id__exact=self.instance.id)

class BalanceSheetInline(admin.StackedInline):
    model = BalanceSheetItem
    verbose_name = 'Explicit Balance Sheet Items in this segment'

class SegmentInline(admin.StackedInline):
    model = Segment
    verbose_name = 'child segments'


class BalanceSheetItemAdmin(admin.ModelAdmin):
    list_display = ['name','parent_segment','get_election']
    model = BalanceSheetItem

class SegmentAdmin(admin.ModelAdmin):
    list_display = ['name','parent_segment','election','logic_segment']
    model = Segment
    form = SegmentForm
    inlines = [
        SegmentInline,
        BalanceSheetInline,

    ]


admin.site.register(Segment, SegmentAdmin)
admin.site.register(BalanceSheetItem, BalanceSheetItemAdmin)
admin.register(Election)(admin.ModelAdmin)
