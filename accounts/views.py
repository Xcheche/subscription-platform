from django.shortcuts import render, redirect

from accounts.forms import CreateUserForm
from django.contrib import messages
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
            messages.success(request, "Your account has been created successfully.")
            return redirect("login_view")
        else:
            messages.error(request, "There was an error creating your account.")

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
            # Checks if the user is a writer or not and redirects accordingly
            if user is not None and user.is_writer:
                login(request, user)
                messages.info(request, "You have been logged in as a writer.")
                return redirect('writer-dashboard')
            # If the user is not a writer, redirect to client dashboard
            if user is not None and not user.is_writer:
                login(request, user)
                messages.info(request, "You have been logged in as a client.")
                return redirect('client-dashboard')
            
    context = {'form': form}
    return render(request, 'accounts/login.html', context)




# Logout
def logout_view(request):

    logout(request)
    messages.info(request, "You have been logged out.")

    return redirect("login_view")
