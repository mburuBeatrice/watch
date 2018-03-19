from . models import Neighbourhood,Business,UserProfile,Contacts,Posts
from .forms import NeighbourhoodForm,NewPostForm,BusinessForm,UserProfileForm
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
   
    businesses = Business.objects.all()
    posts = Posts.objects.all()
    contact = Contacts.objects.all()
    profile = UserProfile.objects.all()
    context = {
        "businesses": businesses,
        "posts": posts,
        "contact":contact,
        "profile":profile
    }

    return render(request, 'home.html', context)
def neighbourhood(request):
    hoods = Neighbourhood.objects.all()
    context = {
      "hoods":hoods,  
    }
    return render(request, 'hoods.html', context)

def neighbourhood_details(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    context ={
        "hood": hood
    }

    return render(request, 'hood_details.html', context)

def profile(request, id):

    profile = get_object_or_404(UserProfile, id=id)
    context ={
        "new_profile": profile
    }
    return render(request, 'profile.html', context)
def find_neighbourhood(request, id):

    hood = get_object_or_404(Neighbourhood, id=id)
    context = {
        "hood": hood,
    
    }
    return render(request, 'search.html', context)

def find_contact(request):

    contact = Contacts.objects.all()
    context = {
        "contact": contact
    }
    return render(request, 'contact.html', context)


@login_required(login_url='/accounts/login/')
def new_post(request):
    # if request.method == 'POST':
    form = NewPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.save()
        messages.success(request, "Successfully created")
        return redirect('/')
    else:
        messages.error(request, "Not successfully created")

    context = {
        "form" : form,
    }

    return render(request, 'post_form.html', context)
@login_required(login_url='/accounts/login/')
def new_neighbourhood(request,id=None):
    instance= get_object_or_404(Neighbourhood, id=id)
    form = NeighbourhoodForm(request.POST or None, instance=instance)
    if form.is_valid():
        new_neighbourhood = form.save(commit=False)
        new_neighbourhood.save()
        messages.success(request, "Successfully created")
        return redirect('/')
    else:
        messages.error(request, "Not successfully created")

    context = {
        "form" : form,
    }

    return render(request, 'neighbourhood_forms.html', context)
login_required(login_url='/accounts/login/')
def new_profile(request):
    # if request.method == 'POST':
    form = UserProfileForm(request.POST or None)
        # current_user = request.user
    if form.is_valid():
        new_profile= form.save(commit=False)
        new_profile.save()
        messages.success(request, "Successfully created")
        return redirect('/')
    else:
        messages.error(request, "Not successfully created")

    context = {
        "form" : form,
    }

    return render(request, 'profile_form.html', context)
# def find_business(request):
 
#     search_term = request.GET.get("business")
#     searched_business = Business.search_business(search_term)
#     message = f"{search_term}"

#     return render(request, 'search.html',{"message":message,"businesses":searched_business})

        

