from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from mainsite.models import Store
from django.http import HttpResponse

def index(request):
    all_stores = Store.objects.all().order_by('name')
    return render_to_response('stores/index.html', {'all_stores': all_stores})

def detail(request, store_id):
    s = get_object_or_404(Store, pk=store_id)

    return render_to_response('stores/detail.html', {'store': s})

def homepage(request):
    l = "Durham"
    
    return render_to_response('index.html', {'location': l}, context_instance=RequestContext(request))
