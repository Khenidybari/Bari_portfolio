from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect(reverse("base:cms"))
        else:
            print("can't login")
    return render(request, 'login.html')

@login_required(login_url="/auth/login")
def signout(request):
    logout(request)
    return redirect(reverse("backend:signin"))

@login_required(login_url="/auth/login")
def forgetpass(request):
    if request.method == "POST":
        user = request.user
        password = request.POST.get("password", user.password)
        user.set_password()
        user.save()
    return redirect(reverse("base:backend"))