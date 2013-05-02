from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.template import RequestContext
from mainsite.models import Store, StoreForm
from django.http import HttpResponse

PAGE_URL = "http://127.0.0.1:8000/"

#not using this currently
def index(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    all_stores = Store.objects.all().order_by('name')
    return render_to_response('stores/index.html', {'all_stores': all_stores}, context_instance=RequestContext(request))

#this is used to lookup a store profile
def detail(request, store_display_url):
    s = get_object_or_404(Store, displayurl=store_display_url)

    return render_to_response('stores/detail.html', {'store': s}, context_instance=RequestContext(request))

#this is the home page
#TODO make location specific
def homepage(request):
    l = "Durham"
    return render_to_response('index.html', {'location': l}, context_instance=RequestContext(request))

#this is a basic login page
#TODO make it a dropdown
def loginpage(request):
    return render_to_response('login.html', {}, context_instance=RequestContext(request))

#checks to see if the specific user has a store
def has_store(user):
    if len(Store.objects.filter(owner=user)) > 0:
        return True
    else:
        return False

#This is used to populate a stores basic data
@login_required
def profile(request):
    o_user = request.user
    if has_store(o_user):
        store = Store.objects.get(owner=o_user)
        return render_to_response('profile.html', {'store':store}, context_instance=RequestContext(request))
    
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = o_user
            store.url = PAGE_URL+"site/"+store.displayurl
            store.save()
            return render_to_response('profile.html', {'store':store}, context_instance=RequestContext(request))
    else:
        form = StoreForm()

    return render_to_response('profile.html', {'form':form}, context_instance=RequestContext(request))
    
