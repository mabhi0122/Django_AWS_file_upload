from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import ProfileForm, UserRegisterForm, UserLoginForm
from .models import Profile
# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserRegisterForm()
    return render(request, 'MainApp/register.html', {'form':form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password= password)

            if user is not None:
                login(request,user)
                return redirect('upload_files')
            else:
                form.add_error(None, 'Invalid username / password')
        else:
            form.add_error(None, "form is Invalid!")

    form = UserLoginForm()
    return render(request, 'MainApp/login.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')


def upload_files(request):

    # Get the Profile object associated with the logged-in user
    try:
        profile_instance = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile_instance = None


    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile_instance)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Uploaded Successfully...')
            return redirect('upload_files')
        else:
            messages.warning(request, 'invalid form')
    form = ProfileForm(instance=profile_instance) # request.POST, request.FILES
    return render(request, 'MainApp/upload_files.html', {'form':form})


def user_dashboard(request):
    try:
        data = Profile.objects.get(user = request.user)
    except Profile.DoesNotExist:
        data = None
    return render(request, 'MainApp/dashboard.html', {'data':data})