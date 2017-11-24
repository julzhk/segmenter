from django.http import HttpResponse
from editor.models import Segment, BalanceSheetItem, Election
from django.template import loader
from django.http import JsonResponse
from collections import defaultdict

def treemap(request):
    template = loader.get_template('editor/treemap.html')
    context = {}
    return HttpResponse(template.render(context, request))

def electiontreemap(request):
    template = loader.get_template('editor/electiontreemap.html')
    context = {}
    return HttpResponse(template.render(context, request))

def get_tree(root):
    children = Segment.objects.filter(parent_segment=root)
    r = {'name':root.name,
         children:[make_leaf(c) for c in children if c]
         }
    return r

def make_leaf(segment):
    children_list = [make_leaf(c) for c in Segment.objects.filter(parent_segment=segment) if c]
    r = {'name': segment.name,
          }
    if children_list:
        r['children'] = children_list
    else:
        r['size'] = 1
    return r


def segmentsTreemapAPI(request):
    data = {
        "name": "flare",
        "children": [make_leaf(s) for s in Segment.objects.filter(parent_segment=None)]}
    return JsonResponse(data)


def electiontreemapAPI(request):
    groupby_election = defaultdict(list)
    for balancesheetitem in BalanceSheetItem.objects.all():
        groupby_election[balancesheetitem.get_election()].append(balancesheetitem)
    print (groupby_election)
    children = [{'name':e.name,
                 'children': [
                     {'name':i.name,
                      'size': 1
                       } for i in groupby_election[e]]
                 } for e in groupby_election]
    data = {
        "name": "flare",
        "children": children
    }
    return JsonResponse(data)


def index(request):

    template = loader.get_template('editor/index.html')
    logical_segments = Segment.objects.exclude(logic_segment ='')
    context = {
        'segments': Segment.objects.all(),
        'parent_segments': Segment.objects.filter(parent_segment=None),
        'child_segments': Segment.objects.exclude(parent_segment=None),
        'balance_sheet_items_with_segments': BalanceSheetItem.objects.exclude(parent_segment=None),
        'balance_sheet_items_without_segments': BalanceSheetItem.objects.filter(parent_segment=None),
    'logical_segments': logical_segments,
    'balance_sheets': BalanceSheetItem.objects.all(),
    'elections': Election.objects.all()
    }
    return HttpResponse(template.render(context, request))
