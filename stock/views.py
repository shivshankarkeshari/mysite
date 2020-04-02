from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def home_page(request):
    return render(request, 'stock/home_page.html')


def background_theme(request):
    return render(request, 'stock/small_blind_dealer.html')


def login(request):
    if request.method == 'POST':

        '''
            some basic of request method

        print("request: ", type(request))
        # request: <class 'django.core.handlers.wsgi.WSGIRequest'>
        print("request: ", (request.POST.keys()))
        # request: dict_keys(['csrfmiddlewaretoken', 'username', 'password'])
        for key, value in request.POST.items():
            print(key, value)
        '''
        user_n = request.POST['username']
        psd = request.POST['password']

        user = auth.authenticate(username=user_n, password=psd)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid Credentials")  # currently not working
            return redirect("login")

    return render(request, 'stock/login.html')


def register(request):
    if request.method == 'POST':
        user_n = request.POST['username']
        psd = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=user_n).exists():
            messages.info(request, "Username Taken")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.info(request, "email Taken")
            return redirect('register')
        else:
            user = User.objects.create_user(username=user_n, password=psd, email=email)
            user.save()
            return redirect('/')
    return render(request, 'stock/register.html')


def logout(request):

    auth.logout(request)
    return redirect('/')
