'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Views File

'''

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

#View function for user registration
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("calendarApp:dashboard")
    else:
        form = UserRegisterForm()
    return render(request, "registration/register.html", {"form": form})

#View Function for user login
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("calendarApp:dashboard") # if login is successful, logs user in
    return render(request, "registration/login.html") # redirect to login page

#View Function for user logout
def logout_view(request):
    logout(request)
    return redirect("accounts:login") # redirect to login page
