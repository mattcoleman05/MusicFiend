from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from .forms import *


def index(request):

    return render(request, 'homepage.html')

def signuppage(request):
    return render(request, 'signuppage.html')

def login(request):

    loggedin_user = User.objects.filter(email= request.POST['email'])
    if len(loggedin_user) > 0:
        loggedin_user = loggedin_user[0]
        if loggedin_user.password == request.POST['password']:
            request.session['artistname'] = loggedin_user.artistname
            request.session['fname'] = loggedin_user.fname
            request.session['lname'] = loggedin_user.lname
            request.session['id'] = loggedin_user.id
            return redirect('/mainpage')
    return redirect('/')


def signup(request):

    errors = User.objects.basic_validator(request.POST) 
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    new_user = User.objects.create(artistname = request.POST ['artistname'],fname = request.POST['fname'], lname= request.POST['lname'], email=request.POST['email'], password= request.POST['password'])
    request.session['artistname'] = new_user.artistname
    request.session['fname'] = new_user.fname
    request.session['lname'] = new_user.lname
    request.session['id'] = new_user.id

    messages.success(request, (f"{new_user.fname} ,You've successfully registered as {new_user.artistname}. Now you may login below."))
    return redirect('/mainpage')


def mainpage(request):
    if 'fname' not in request.session:
        return redirect('/')
    else:
    
        request.session['id']
        context = {
        'artist' : ArtistInfo.objects.all().order_by('-created_at'),
        'user' : User.objects.all(),
    } 
   
    return render(request, 'mainpage.html', context)



def editpage(request, id):
    if 'fname' not in request.session:
        return redirect('/')
  
    context = {
        'user' : User.objects.get(id=id)
    }
    context = {}
    context['form'] = ArtistLinkForm()
    context['imgform'] = ArtistImageForm()

    return render(request, 'editartistpage.html',context)



def create(request):
    

    
    return redirect('/mainpage')


def update_artist(request):
    ArtistInfo.objects.create(genre = request.POST['genre'], profile = request.POST['profile'], members = request.POST['members'], city = request.POST['city'],link = request.POST['link'], record_label = request.POST['record_label'],user =User.objects.get(id=request.session['id']))
    return redirect('/create')




def artistpage(request, id):
    if 'fname' not in request.session:
        return redirect('/')
    context = {
            'artist' : User.objects.get(id=id),
 
    }
    return render(request, 'artistpage.html', context)

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/')


    
    
    
    



























def artist_image_view(request): 
  
    if request.method == 'POST': 
        imgform = ArtistImageForm(request.POST, request.FILES) 
  
        if imgform.is_valid(): 
            imgform.save() 
            return redirect('success') 
    else: 
        imgform = ArtistImageForm() 
    return render(request, 'hotel_image_form.html', {'imgform' : imgform}) 

def success(request):
        return render(request, 'editartistpage.html') 



  
  










