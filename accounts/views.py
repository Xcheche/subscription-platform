from django.shortcuts import render, redirect

from accounts.forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate,login as auth_login

# Create your views here.
#Home
def home(request):
    return render(request, "accounts/index.html")



# Register
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_view")
    else:
        form = CreateUserForm()

    return render(request, "accounts/register.html", {"form": form})








# Login
def login_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')  # Username / Email
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_writer:
                login(request, user)
                return redirect('writer-dashboard')
            if user is not None and not user.is_writer:
                login(request, user)
                return redirect('client-dashboard')
    context = {'form': form}
    return render(request, 'accounts/login.html', context)




# Logout
def logout_view(request):

    logout(request)

    return redirect("login_view")
