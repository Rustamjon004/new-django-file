from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


def home_page(request):

    if not request.user.is_authenticated:
        return redirect("/login/")

    return render(request=request,
                  template_name="index.html")


def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            user = None

        if user and user.check_password(raw_password=password):
            login(request, user)
            return redirect("/")

    return render(request=request,
                  template_name="login.html")


def logout_page(request):
    logout(request)
    return redirect("/login/")


def registration_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if username and password1 and password2:
            if password1 == password2:
                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.set_password(raw_password=password2)
                user.save()
                return redirect("/login/")

    return render(request=request,
                  template_name="registration.html")

# Create your views here.
